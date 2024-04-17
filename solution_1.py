def get_name():
    x=input("Your Name please:")
    return x 
def get_tshirt():
    x=get_name()
    y=input("What brand are you looking for:")
    a=["puma","nike","peter england","louis viton"]
    for i in a:
        if i==y:
            print("Hii"+" "+x+","+"the brand you are looking for is available in our store ")
            break 
        elif i!=y:
            continue
    else:
        print("Hii"+" "+x+","+"Unfortunately the brand you are looking for is not available in our store ")      
get_tshirt()  
