def total_price(price,height,width):
    area=height*width
    return f"The total price is: ${area*price}"




if __name__=="__main__":
    price=float(input("Please provide the price per square meter: "))
    height=float(input("Please provide the height: "))
    width=float(input("Please provide the width: "))
    print(total_price(price,height,width))