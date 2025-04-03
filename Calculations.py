##Calculations
#Buying Amount for Sell Flow
def Buying_Amount_Sell_Flow(selling_amount, inverted_rate):
    buying_amount_sell_flow = round(selling_amount * inverted_rate, 2)
    return buying_amount_sell_flow

#Selling Amount for Buy Flow
def Selling_Amount_Buy_Flow(buying_amount, fxts_rate):
    selling_amount_buy_flow = round(buying_amount * fxts_rate, 2)
    return selling_amount_buy_flow

#Selling Amount * Inverted Rate
def Selling_Times_Inverted_Rate(selling_amount, inverted_rate):
    selling_times_inverted_rate = selling_amount * inverted_rate
    return selling_times_inverted_rate

#Selling Amount * Rounded Up Inverted Rate
def Selling_Times_Rounded_Up_Inverted_Rate(selling_amount, rounded_up_inverted_rate):
    selling_times_rounded_up_inverted_rate = selling_amount * rounded_up_inverted_rate
    return selling_times_rounded_up_inverted_rate

#Selling Amount * Discarded Inverted Rate
def Selling_Times_Discarded_Inverted_Rate(selling_amount, discarded_inverted_rate):
    selling_times_discarded_inverted_rate = selling_amount * discarded_inverted_rate
    return selling_times_discarded_inverted_rate

#Selling Amount / FXTS Rate
def Selling_Divide_FXTS_Rate(selling_amount, fxts_rate):
    selling_divide_fxts_rate = selling_amount / fxts_rate 
    return selling_divide_fxts_rate

#Buying Amount / Inverted Rate
def Buying_Divide_Inverted_Rate(buying_amount, inverted_rate):
    buying_divide_inverted_rate = buying_amount / inverted_rate
    return buying_divide_inverted_rate

#Buying Amount / Rounded Up Inverted Rate
def Buying_Divide_Rounded_Up_Inverted_Rate(buying_amount, rounded_up_inverted_rate):
    buying_divide_rounded_up_inverted_rate = buying_amount / rounded_up_inverted_rate
    return buying_divide_rounded_up_inverted_rate

#Buying Amount / Discarded Inverted Rate
def Buying_Divide_Discarded_Inverted_Rate(buying_amount, discarded_inverted_rate):
    buying_divide_discarded_inverted_rate = buying_amount / discarded_inverted_rate
    return buying_divide_discarded_inverted_rate