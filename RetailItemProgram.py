import RetailItemClass as ri

item1 = ri.RetailItem('Jacket', 12, 59.95)
item2 = ri.RetailItem('Designer Jeans', 40, 34.95)
item3 = ri.RetailItem('Shirt', 20, 24.95)

print('        Description          Units in inventory          Price')
print(f"Item #1 {item1.get_description()}               {item1.get_units()}                          {item1.get_price()}") 
print(f"Item #2 {item2.get_description()}       {item2.get_units()}                          {item2.get_price()}") 
print(f"Item #3 {item3.get_description()}                {item3.get_units()}                          {item3.get_price()}") 