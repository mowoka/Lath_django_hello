# Return all customers from customer table
customers = Customer.objects.all()
# Return first customer in table
firstCustomer = customers.objects.first()
# Return  last customer in table
lastCustomer = Customer.objects.last()
# Return single customer by name
CustomerByName = Customer.objects.get(name="Giofanny Mowoka")
# Return single customer by name
CustomerById = Customer.objects.get(id="2")
# Return all Order related to customer 
firstCustomer.order_set.all()
# return orders customer name
order = Order.objects.first()
parentName = order.customer.name
# Return products from products table with val of "Out Door" in category atribute
products = Product.objects.filter(category="Out Door")
# Order/Sort Object by id
lastToGreatest = Product.objects.all().order_by('id')
GreatesToLast = Product.objects.all().order_by('-id')
# Return all product with tag of "Sports" (Query Many to Many Fields)
productFiltered = Product.objects.filter(tags__name="Sports")
# Return the total count for number of time a "Ball" was ordered by the first customer
ballOrder = firstCustomer.order_set.filter(product__name="Ball").count()
# return total count for each product ordered
allOrders = {}

for order in firstCustomer.ordered_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Related Set Example
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModle(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length = 200, null=True)

parent = ParentModel.objects.first()
parent.childmodel_set.all()
