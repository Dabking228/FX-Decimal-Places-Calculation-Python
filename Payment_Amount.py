import random

##Getting payment amount
#Getting a random amount between 1000.00 to 9999.99
def Random_Thousand_Amount():
    random_thousand_amount = round(random.uniform(1000.00, 9999.99), 2)
    return random_thousand_amount

#Getting a random amount between 10000.00 to 99999.99
def Random_Ten_Thousand_Amount():
    random_ten_thousand_amount = round(random.uniform(10000.00, 99999.99), 2)
    return random_ten_thousand_amount

#Getting a random amount between 100000.00 to 999999.99
def Random_Hundred_Thousand_Amount():
    random_hundred_thousand_amount = round(random.uniform(100000.00, 999999.99), 2)
    return random_hundred_thousand_amount

#Getting a random amount between 1000000.00 to 5000000.00
def Random_Million_Amount():
    random_million_amount = round(random.uniform(1000000.00, 5000000.00), 2)
    return random_million_amount