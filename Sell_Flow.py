from Rates import *
from Payment_Amount import *
from Calculations import *

sell_data_csv = []

##Sell Flow
def Sell_Flow(selling_amount, fxts_rate):
    rates = getRates(fxts_rate)
    buying_amount_sell_flow = Buying_Amount_Sell_Flow(selling_amount, rates[0])
    selling_times_inverted_rate = Selling_Times_Inverted_Rate(selling_amount, rates[0])
    selling_times_rounded_up_inverted_rate = Selling_Times_Rounded_Up_Inverted_Rate(selling_amount, rates[1])
    selling_times_discarded_inverted_rate = Selling_Times_Discarded_Inverted_Rate(selling_amount, rates[2])
    selling_divide_fxts_rate = Selling_Divide_FXTS_Rate(selling_amount, fxts_rate)
    buying_divide_inverted_rate = Buying_Divide_Inverted_Rate(buying_amount_sell_flow, rates[0])
    buying_divide_rounded_up_inverted_rate = Buying_Divide_Rounded_Up_Inverted_Rate(buying_amount_sell_flow, rates[1])
    buying_divide_discarded_inverted_rate = Buying_Divide_Discarded_Inverted_Rate(buying_amount_sell_flow, rates[2])
    return(
        rates, buying_amount_sell_flow, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
        selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate, 
        buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate
    )

def Selling_Thousand(fxts_rate):
    for i in range(10):
        random_thousand_amount = Random_Thousand_Amount()
        sell_flow = Sell_Flow(random_thousand_amount, fxts_rate)
        selling_amount = random_thousand_amount
        buying_amount = sell_flow[1]
        fxts_rate = fxts_rate
        inverted_rate = sell_flow[0][0]
        rounded_up_inverted_rate = sell_flow[0][1]
        discarded_inverted_rate = sell_flow[0][2]
        selling_times_inverted_rate = sell_flow[2]
        selling_times_rounded_up_inverted_rate = sell_flow[3]
        selling_times_discarded_inverted_rate = sell_flow[4]
        selling_divide_fxts_rate = sell_flow[5]
        buying_divide_inverted_rate = sell_flow[6]
        buying_divide_rounded_up_inverted_rate = sell_flow[7]
        buying_divide_discarded_inverted_rate = sell_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        sell_data_csv.append(row)

def Selling_Ten_Thousand(fxts_rate):
    for i in range(10):
        random_ten_thousand_amount = Random_Ten_Thousand_Amount()
        sell_flow = Sell_Flow(random_ten_thousand_amount, fxts_rate)
        selling_amount = random_ten_thousand_amount
        buying_amount = sell_flow[1]
        fxts_rate = fxts_rate
        inverted_rate = sell_flow[0][0]
        rounded_up_inverted_rate = sell_flow[0][1]
        discarded_inverted_rate = sell_flow[0][2]
        selling_times_inverted_rate = sell_flow[2]
        selling_times_rounded_up_inverted_rate = sell_flow[3]
        selling_times_discarded_inverted_rate = sell_flow[4]
        selling_divide_fxts_rate = sell_flow[5]
        buying_divide_inverted_rate = sell_flow[6]
        buying_divide_rounded_up_inverted_rate = sell_flow[7]
        buying_divide_discarded_inverted_rate = sell_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        sell_data_csv.append(row)

def Selling_Hundred_Thousand(fxts_rate):
    for i in range(10):
        random_hundred_thousand_amount = Random_Hundred_Thousand_Amount()
        sell_flow = Sell_Flow(random_hundred_thousand_amount, fxts_rate)
        selling_amount = random_hundred_thousand_amount
        buying_amount = sell_flow[1]
        fxts_rate = fxts_rate
        inverted_rate = sell_flow[0][0]
        rounded_up_inverted_rate = sell_flow[0][1]
        discarded_inverted_rate = sell_flow[0][2]
        selling_times_inverted_rate = sell_flow[2]
        selling_times_rounded_up_inverted_rate = sell_flow[3]
        selling_times_discarded_inverted_rate = sell_flow[4]
        selling_divide_fxts_rate = sell_flow[5]
        buying_divide_inverted_rate = sell_flow[6]
        buying_divide_rounded_up_inverted_rate = sell_flow[7]
        buying_divide_discarded_inverted_rate = sell_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        sell_data_csv.append(row)

def Selling_Million(fxts_rate):
    for i in range(10):
        random_million_amount = Random_Million_Amount()
        sell_flow = Sell_Flow(random_million_amount, fxts_rate)
        selling_amount = random_million_amount
        buying_amount = sell_flow[1]
        fxts_rate = fxts_rate
        inverted_rate = sell_flow[0][0]
        rounded_up_inverted_rate = sell_flow[0][1]
        discarded_inverted_rate = sell_flow[0][2]
        selling_times_inverted_rate = sell_flow[2]
        selling_times_rounded_up_inverted_rate = sell_flow[3]
        selling_times_discarded_inverted_rate = sell_flow[4]
        selling_divide_fxts_rate = sell_flow[5]
        buying_divide_inverted_rate = sell_flow[6]
        buying_divide_rounded_up_inverted_rate = sell_flow[7]
        buying_divide_discarded_inverted_rate = sell_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        sell_data_csv.append(row)

def Get_Sell_Flows(fxts_rate):
    Selling_Thousand(fxts_rate)
    Selling_Ten_Thousand(fxts_rate)
    Selling_Hundred_Thousand(fxts_rate)
    Selling_Million(fxts_rate)