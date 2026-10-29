import random
from tkinter import Y


Salary_Monthly =float(input("What is your salary monthly: $ "))
Salary_Annoual = Salary_Monthly * 12 
print(f"Then your salary annoual is : {Salary_Annoual} ")
Answer = (input("Did you want to invest your money: (Y/N)").capitalize())
while Answer == "Y":
    Amount_Invest = float(input("How much do you want to invest: $ "))
    Interest_Rate = random.uniform(5, 15)  # Random interest rate between 5% and 15%
    print(f"The interest rate is: {Interest_Rate:.2f}%")
    Time_Period = float(input("How many years do you want to invest: "))
    Future_Value = Amount_Invest * (1 + Interest_Rate/100) ** Time_Period
    future_net_worth = Salary_Annoual + Future_Value
    print(f"Your future net worth is: ${future_net_worth:.2f}")
    if Salary_Annoual < 50000:break
else:
        print("Okay, have a nice day!")
        Answer = input("Did you want to build a tech idea by using your money: (Y/N)").capitalize()
        #elon musk invest in your idea and it will be worth 100 times more than your salary annoual
if Answer == "Y":
            Future_Net_Worth = Salary_Annoual * 100
            print(f"Your future net worth is: ${Future_Net_Worth:.2f}")
else:
            print("Okay, have a nice day!")
        

    





