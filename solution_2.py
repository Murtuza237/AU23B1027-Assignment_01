def get_name():
    x=input("Your Name please:")
    return x 
def get_tshirt():
    x=get_name()
    y=input("which brand do you want:")
    size=input("Which size do you want:")
    a=["puma","nike","peter england","louis viton"]
    b=["l","xl","xxl"]
    for i in a:
        for ele in b:
            if i!=y or ele!=size:
                continue
            elif i==y and ele==size:
                print("Hii"+" "+x+","+"the brand you are looking for with size "+size+" is available in our store ")
                break  
            else:
                print("Hii"+" "+x+","+"Unfortunately the brand you are looking for with size "+size+" is not available in our store ") 
                break
get_tshirt()
