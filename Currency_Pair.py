#Displaying the Available Currencies
currency_list = ["GBP", "USD", "EUR", "HKD", "SGD", "CNY", "AED", "JPY"]
def Currency_List():
    currency_display = "["
    for i in range(len(currency_list)):
        currency_display += currency_list[i]
        if i < len(currency_list) - 1:
            currency_display += ", "
    currency_display += "]"
    print(currency_display)

#Determine the Selling Currency
def Selling_Currency(): 
    while(True):
        try:
            sell_currency = input("Enter selling currency or E to exit: ")
            sell_currency = sell_currency.upper()
            if sell_currency == "E":
                return sell_currency
            elif sell_currency not in currency_list:
                print("Enter a valid currency!")
            else:
                return sell_currency
        except:
            print("Enter a valid currency!")

#Determine the Buying Currency
def Buying_Currency(): 
    while(True):
        try:
            buy_currency = input("Enter buying currency or E to exit: ")
            buy_currency = buy_currency.upper()
            if buy_currency == "E":
                return buy_currency            
            elif buy_currency not in currency_list:
                print("Enter a valid currency!")
            else:
                return buy_currency
        except:
            print("Enter a valid currency!")