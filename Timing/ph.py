from datetime import date
ph_test = date(2026, 9, 10)
today = date.today()
days_left = (ph_test - today).days   
print(f"{days_left} days left until the test.") 
