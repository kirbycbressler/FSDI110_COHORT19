from flask import Flask, abort, request, render_template
from pymongo.message import insert
from data import data
import json
from flask_cors import CORS
from config import db, parse_json

app = Flask(__name__)
CORS(app)

# dictionary
me = {
    "name" : "Kirby",
    "last" : "Bressler",
    "email" : "kirbycbressler@icloud.com",
}

# list
products = data


@app.route("/")
@app.route("/home")
def index():
  return "hello there, from flask"


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/about/name")
def name():
  return me["name"]


@app.route("/about/fullname")
def fullName():
  return me["name"] +" " + me["last"]


@app.route("/api/catalog")
def get_catalog():
  cursor = db.products.find({})
  catalog = [item for item in cursor]


  return parse_json(catalog)

# create post endpoint
# to register new products
@app.route("/api/catalog", methods=["POST"])
def save_product():
  prod = request.get_json()
  db.products.insert(prod)
  return parse_json(prod)

@app.route("/api/catalog/<category>")
def get_product_by_category(category):
  data = db.products.find({"category": category})
  results = [item for item in data]
  return parse_json(results)

@app.route("/api/discountCode/<code>")
def get_discount(code):
  data = db.couponCodes.find({"code": code})
  for code in data:
    return parse_json(code)

  return parse_json({"error":True, "reason":"invalid code"})



@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
  for prod in products:
    if(prod["_id"] == id):
      return json.dumps(prod)

  abort(404)


# get the cheapest product
# /api/catalog/cheapest

@app.route("/api/catalog/cheapest")
def get_cheapest():
  cheapest = products[0]
  for prod in products:
    if (prod["price"] < cheapest["price"]):
      cheapest = prod
    
  return json.dumps(cheapest)
      



@app.route("/api/categories")
def get_categories():
  data = db.products.find({})
  unique_categories = []
  #do the magic
  for prod in data:
    cat = prod["category"]
    if cat not in unique_categories:
      unique_categories.append(cat)
      print(cat)
  return parse_json(unique_categories)



@app.route("/api/test")
def test_data_manipulation():

  test_data = db.test.find({})
  print(test_data)

  

  return parse_json(test_data[0])

@app.route("/test/populatecodes")
def test_populate_codes():
  db.couponCodes.insert({"code": "qwerty", "discount": 10})
  db.couponCodes.insert({"code": "7off", "discount": 7})
  db.couponCodes.insert({"code": "5off", "discount": 5})
  db.couponCodes.insert({"code": "20off", "discount": 20})

  return "Coupon registered"

# if __name__ == '__main__':
#   app.run(debug=True) 
# git add.
# git commit -m "<a message>"
# git push
# aaaaadd code... fix erything

