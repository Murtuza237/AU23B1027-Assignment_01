def get_order(n=[]):
    m=list(reversed(n))
    o=list(reversed(n))
    for i in range(len(m)): 
        print("Preparing Your Order - "+m.pop())
    print("The following orders have been dispatched.")
    for i in range(len(o)):
        print(o.pop()) 
         
              
x=int(input("how many orders woukd you like to do:"))
order=[]
for i in range(x):
    if x>1:
        y=input("enter item to order:")
        order.append(y)
    else:
       print("No orders found") 
       break   
get_order(order)
