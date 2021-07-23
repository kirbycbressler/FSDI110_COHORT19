from data import data

#list of dictionaries
products = data



def test1():
  print("**Print each product title")
  for prod in products:
      title = prod["title"]

def test2():
  print("-- sum of all prices")

  sum = 0 
  for prod in products:
      price = prod["price"]
      sum += price

  print(f"the sum is: {sum}")

def test3():
  print("Products with prices over $13")
  for prod in products:
      price = prod["price"]
      title = prod["title"]

      if price >= 11.13:
        print({title})

def test4():
  print("Total amount in stock")

  sum = 0
  for prod in products:
    val = prod["stock"] * prod["price"]
    sum += val

  print (f"there are {sum} products in stock")

def test5():
  print("**These are the unique categories")
  unique_categories = []
  for prod in products:
    cat = prod["category"]
    if cat not in unique_categories:
      unique_categories.append(cat)
      print(cat)

def run_tests():
  print("**Starting tests")

  test1()
  test2()
  test3()
  test4()

run_tests()



# test 3
# print the title of products with price greater than 11.13
# test 4
# print stock value total (price * stock)





