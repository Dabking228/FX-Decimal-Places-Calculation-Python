#Problem Statement: To find out which method of handling the decimal places of the fx rates display. Round Up or Discard/Hide?
#Objective: To analyze which rate will achieve the closest value to the final settlement amount
#Exception Handling: Allow ±0.01 discrepancy in displayed amounts and actual amounts

#Solution: Build a program to automatically insert payment amounts from different ranges then perform the necessary calculations
#          and export to CSV file
#          Accept user input: Selling currency, Buying currency, FXTS Rate (Raw rate)

import json
import openpyxl
import csv
from Currency_Pair import *
from Rates import *
from Payment_Amount import *
from Calculations import *
from Sell_Flow import *
from Buy_Flow import *


#Determine Sell Flow or Buy Flow (Not Using This Function For Now)
def Sell_Or_Buy_Flow():
    while(True):
        try:
            print("S = Sell Flow    B = Buy Flow")
            flow = input("Sell or Buy Flow: ").upper()
            if flow == "S":
                return flow
            elif flow == "B":
                return flow
            else:
                print("Enter S or B only!")
        except:
            print("Enter S or B only!")

def Export_To_CSV_File(sell_currency, buy_currency):
    with open(f"C:/APU/Projects/FX Decimal Places Calculation/CSV Files/{sell_currency} To {buy_currency}.csv",
               mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Sell Flow"])
        writer.writerow(["Selling Amount", "Buying Amount", "FXTS Rate", "Inverted Rate",
                         "Rounded Up Inverted Rate", "Discarded Inverted Rate", "Selling Amount * Inverted Rate",
                         "Selling Amount * Rounded Up Inverted Rate", "Selling Amount * Discarded Inverted Rate",
                         "Selling Amount / FXTS Rate", "Buying Amount / Inverted Rate",
                         "Buying Amount / Rounded Up Inverted Rate", "Buying Amount / Discarded Inverted Rate"])
        writer.writerows(sell_data_csv)
        writer.writerow([])
        writer.writerow([])
        writer.writerow([])
        writer.writerow(["Buy Flow"])
        writer.writerow(["Selling Amount", "Buying Amount", "FXTS Rate", "Inverted Rate",
                         "Rounded Up Inverted Rate", "Discarded Inverted Rate", "Selling Amount * Inverted Rate",
                         "Selling Amount * Rounded Up Inverted Rate", "Selling Amount * Discarded Inverted Rate",
                         "Selling Amount / FXTS Rate", "Buying Amount / Inverted Rate",
                         "Buying Amount / Rounded Up Inverted Rate", "Buying Amount / Discarded Inverted Rate"])
        writer.writerows(buy_data_csv)
    print(f"Data successfully exported to {sell_currency} To {buy_currency}.csv")

def Main():
    while(True):
        sell_data_csv.clear()
        buy_data_csv.clear()
        Currency_List()
        sell_currency = Selling_Currency()
        if sell_currency == "E":
            exit()
        buy_currency = Buying_Currency()
        if buy_currency == "E":
            exit()
        fxts_rate = FXTS_Rate(sell_currency, buy_currency)
        Get_Sell_Flows(fxts_rate)
        Get_Buy_Flows(fxts_rate)
        Export_To_CSV_File(sell_currency, buy_currency)

Main()    