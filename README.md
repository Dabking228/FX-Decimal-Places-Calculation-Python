# FX-Decimal-Places-Calculation-Python

## Purpose
 
- Generate a random record of FX calculations between two currencies into a CSV file.

- Compare different types of exchange rates handling method by using different types of calculations
- Types of Exchange Rates: Inverted Rate (Without rounding up), Round up the inverted rate to 8 decimal places, Discard/Hide/Truncate the decimal places beyond the 8th place of the inverted rate
- Types of Calculations: 

## Required inputs

- Two currencies (e.g. USD, GBP, MYR), and the FX rate (the conversion rate)

## Code modification

- Modify the number of records that you want to generate

### Go to Sell_Flow.py

- Modify the number in the for loop ```for i in range(number)``` for the following functions: 
1. Selling_Thousand(fxts_rate)
2. Selling_Ten_Thousand(fxts_rate)
3. Selling_Hundred_Thousand(fxts_rate)
4. Selling_Million(fxts_rate)

### Go to Buy_Flow.py

- Modify the number in the for loop ```for i in range(number)``` for the following functions: 
1. Buying_Thousand(fxts_rate)
2. Buying_Ten_Thousand(fxts_rate)
3. Buying_Hundred_Thousand(fxts_rate)
4. Buying_Million(fxts_rate)
