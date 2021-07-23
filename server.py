from flask import Flask, abort, request, render_template
from data import data
import json
from flask_cors import CORS

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
  return json.dumps(products)

# create post endpoint
# to register new products
@app.route("/api/catalog", methods=["POST"])
def save_product():
  prod = request.get_json()
  products.append(prod)
  return json.dumps(prod)


@app.route("/api/catalog/<category>")
def get_product_by_category(category):

  results = []
  for prod in products:
    if(prod["category"].lower() == category.lower()):
      results.append(prod)

  return json.dumps(results)

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
  unique_categories = []
  #do the magic
  for prod in products:
    cat = prod["category"]
    if cat not in unique_categories:
      unique_categories.append(cat)
      print(cat)
  return json.dumps(unique_categories)



@app.route("/api/test")
def test():

    # add
    products.append("strawberry")
    products.append("dragon fruit")

    # length
    print(f"You have: {len(products)} products in your catalog" )

    # iterate
    for fruit in products:
      print(fruit)


    # print the name 10 times
    for i in range(0,10,1):
      print(me["name"])

    # remove apple from products
    # print the list

    products.remove("apple")
    for f in products:
        print(f)
    



    return "Check your terminal"


# if __name__ == '__main__':
#   app.run(debug=True) 

# add code... fix erything