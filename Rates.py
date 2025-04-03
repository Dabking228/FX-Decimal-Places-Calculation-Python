from decimal import Decimal, getcontext, ROUND_DOWN

#Enter the FXTS Rate for the Specific Currency Pair
def FXTS_Rate(sell_currency, buy_currency):
    while(True):
        try:
            fxts_rate = float(input(f"Enter FXTS Rate for {sell_currency}-{buy_currency}: "))
            return fxts_rate
        except:
            print("Enter a valid FXTS rate!")

##Different types of exchange rates
#Inverted Rate (Without rounding up)
def Inverted_Rate(fxts_rate):
    inverted_rate = round(1 / fxts_rate, 10)
    return inverted_rate

#Round up the inverted rate to 8 decimal places
def Rounded_Up_Inverted_Rate(inverted_rate):
    rounded_up_inverted_rate = round(inverted_rate, 8)
    return rounded_up_inverted_rate

#Discard/Hide/Truncate the decimal places beyond the 8th place of the inverted rate
def Discarded_Inverted_Rate(inverted_rate):
    inverted_rate = Decimal(f'{inverted_rate}')
    discarded_inverted_rate = float(inverted_rate.quantize(Decimal('1.00000000'), rounding = ROUND_DOWN))
    return discarded_inverted_rate

#Get all rates
def getRates(fxts_rate):
    inverted_rate = Inverted_Rate(fxts_rate)
    rounded_up_inverted_rate = Rounded_Up_Inverted_Rate(inverted_rate)
    discarded_inverted_rate = Discarded_Inverted_Rate(inverted_rate)
    return inverted_rate, rounded_up_inverted_rate, discarded_inverted_rate 