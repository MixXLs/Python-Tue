keep_going = 'y'
while keep_going.lower() == 'y':
    retail_price = float(input('Enter the amount of sales: '))
    price = retail_price * 2.5
    print(f"Retail price ${price:.2f}",)
    keep_going = input('Do you want to calulate anther' + '\ncommission (Enteer y for n): ')