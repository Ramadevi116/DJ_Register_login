#***(1)Returns all customers from customer table
# objects.all()

#(2)Returns first customer in table
# objects.first()

#(3)Returns last customer in table
# objects.last()

#(4)Returns single customer by name
# objects.get(num1)

#***(5)Returns single customer by name
# .objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
# order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
# objects.first() 
# customer.name

#(8)***Returns products from products table with value of "Out Door" in category attribute
# objects.filter(category="Out Door")

#(9)***Order/Sort Objects by id
#leastToGreatest = Product.objects.all().order_by('id') 
#greatestToLeast = Product.objects.all().order_by('-id') 


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
#productsFiltered = Product.objects.filter(tags__name="Sports