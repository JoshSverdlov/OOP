import CellPhoneClass as c

def main():

    cellphone = c.CellPhone('Apple', 'iPhone 15', '$1099')
    retail_price = input('Enter the retail price: ')
    cellphone.set_retail_price(retail_price)

    print(f"The manufacturer is {cellphone.get_manufact()}")
    print(f"The model is {cellphone.get_model()}")
    print(f"The retail price is ${cellphone.get_retail_price()}")

main()