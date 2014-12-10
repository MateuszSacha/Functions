# Mateusz Sacha
# 24-11-2014
# total pay code
def calculate_pay():
    hours, rate = get_hours_and_rate()
    total = calculate_total_pay(hours,rate)
    display_total_pay(total)
    

def get_hours_and_rate():
    hours = int(input("Enter the number of hours:"))
    rate = int(input("Enter the rate:"))
    return hours, rate

def calculate_overtime_pay(hours,rate):
    overtime_pay = hours - 40
    basic_pay = 40 * rate
    overtime_pay = overtime_pay * rate * 1.5
    total = overtime_pay + basic_pay
    return total

def calculate_basic_pay(hours,rate):
    total = hours * rate 
    return total

def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate_basic_pay(hours,rate)
    else:
        total = calculate_overtime_pay(hours,rate)
    return total

def display_total_pay(total):
    print(total)
    
calculate_pay()

