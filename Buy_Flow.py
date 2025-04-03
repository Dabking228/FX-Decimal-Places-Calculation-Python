from Rates import *
from Payment_Amount import *
from Calculations import *

buy_data_csv = []

##Buy Flow
def Buy_Flow(buying_amount, fxts_rate):
    rates = getRates(fxts_rate)
    selling_amount_buy_flow = Selling_Amount_Buy_Flow(buying_amount, fxts_rate)
    selling_times_inverted_rate = Selling_Times_Inverted_Rate(selling_amount_buy_flow, rates[0])
    selling_times_rounded_up_inverted_rate = Selling_Times_Rounded_Up_Inverted_Rate(selling_amount_buy_flow, rates[1])
    selling_times_discarded_inverted_rate = Selling_Times_Discarded_Inverted_Rate(selling_amount_buy_flow, rates[2])
    selling_divide_fxts_rate = Selling_Divide_FXTS_Rate(selling_amount_buy_flow, fxts_rate)
    buying_divide_inverted_rate = Buying_Divide_Inverted_Rate(buying_amount, rates[0])
    buying_divide_rounded_up_inverted_rate = Buying_Divide_Rounded_Up_Inverted_Rate(buying_amount, rates[1])
    buying_divide_discarded_inverted_rate = Buying_Divide_Discarded_Inverted_Rate(buying_amount, rates[2])
    return(
        rates, selling_amount_buy_flow, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
        selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate, 
        buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate
    )

def Buying_Thousand(fxts_rate):
    for i in range(10):
        random_thousand_amount = Random_Thousand_Amount()
        buy_flow = Buy_Flow(random_thousand_amount, fxts_rate)
        selling_amount = buy_flow[1]
        buying_amount = random_thousand_amount
        fxts_rate = fxts_rate
        inverted_rate = buy_flow[0][0]
        rounded_up_inverted_rate = buy_flow[0][1]
        discarded_inverted_rate = buy_flow[0][2]
        selling_times_inverted_rate = buy_flow[2]
        selling_times_rounded_up_inverted_rate = buy_flow[3]
        selling_times_discarded_inverted_rate = buy_flow[4]
        selling_divide_fxts_rate = buy_flow[5]
        buying_divide_inverted_rate = buy_flow[6]
        buying_divide_rounded_up_inverted_rate = buy_flow[7]
        buying_divide_discarded_inverted_rate = buy_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        buy_data_csv.append(row)

def Buying_Ten_Thousand(fxts_rate):
    for i in range(10):
        random_ten_thousand_amount = Random_Ten_Thousand_Amount()
        buy_flow = Buy_Flow(random_ten_thousand_amount, fxts_rate)
        selling_amount = buy_flow[1]
        buying_amount = random_ten_thousand_amount
        fxts_rate = fxts_rate
        inverted_rate = buy_flow[0][0]
        rounded_up_inverted_rate = buy_flow[0][1]
        discarded_inverted_rate = buy_flow[0][2]
        selling_times_inverted_rate = buy_flow[2]
        selling_times_rounded_up_inverted_rate = buy_flow[3]
        selling_times_discarded_inverted_rate = buy_flow[4]
        selling_divide_fxts_rate = buy_flow[5]
        buying_divide_inverted_rate = buy_flow[6]
        buying_divide_rounded_up_inverted_rate = buy_flow[7]
        buying_divide_discarded_inverted_rate = buy_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        buy_data_csv.append(row)

def Buying_Hundred_Thousand(fxts_rate):
    for i in range(10):
        random_hundred_thousand_amount = Random_Hundred_Thousand_Amount()
        buy_flow = Buy_Flow(random_hundred_thousand_amount, fxts_rate)
        selling_amount = buy_flow[1]
        buying_amount = random_hundred_thousand_amount
        fxts_rate = fxts_rate
        inverted_rate = buy_flow[0][0]
        rounded_up_inverted_rate = buy_flow[0][1]
        discarded_inverted_rate = buy_flow[0][2]
        selling_times_inverted_rate = buy_flow[2]
        selling_times_rounded_up_inverted_rate = buy_flow[3]
        selling_times_discarded_inverted_rate = buy_flow[4]
        selling_divide_fxts_rate = buy_flow[5]
        buying_divide_inverted_rate = buy_flow[6]
        buying_divide_rounded_up_inverted_rate = buy_flow[7]
        buying_divide_discarded_inverted_rate = buy_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        buy_data_csv.append(row)

def Buying_Million(fxts_rate):
    for i in range(10):
        random_million_amount = Random_Million_Amount()
        buy_flow = Buy_Flow(random_million_amount, fxts_rate)
        selling_amount = buy_flow[1]
        buying_amount = random_million_amount
        fxts_rate = fxts_rate
        inverted_rate = buy_flow[0][0]
        rounded_up_inverted_rate = buy_flow[0][1]
        discarded_inverted_rate = buy_flow[0][2]
        selling_times_inverted_rate = buy_flow[2]
        selling_times_rounded_up_inverted_rate = buy_flow[3]
        selling_times_discarded_inverted_rate = buy_flow[4]
        selling_divide_fxts_rate = buy_flow[5]
        buying_divide_inverted_rate = buy_flow[6]
        buying_divide_rounded_up_inverted_rate = buy_flow[7]
        buying_divide_discarded_inverted_rate = buy_flow[8]
        row = [selling_amount, buying_amount, fxts_rate, inverted_rate, rounded_up_inverted_rate,
               discarded_inverted_rate, selling_times_inverted_rate, selling_times_rounded_up_inverted_rate,
               selling_times_discarded_inverted_rate, selling_divide_fxts_rate, buying_divide_inverted_rate,
               buying_divide_rounded_up_inverted_rate, buying_divide_discarded_inverted_rate]
        buy_data_csv.append(row)

def Get_Buy_Flows(fxts_rate):
    Buying_Thousand(fxts_rate)
    Buying_Ten_Thousand(fxts_rate)
    Buying_Hundred_Thousand(fxts_rate)
    Buying_Million(fxts_rate)