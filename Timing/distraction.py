from datetime import date


# first goal is : take off addicted on porn for my neuroal health and for my future 
# Dates that you started working on your goals 
start_dates = {  " Goal": date(2026, 8, 18),
    }

target_days = 180  # Target of 6 months
today = date.today()

print(f"--- Achievement Control Panel({today}) ---")

for goal, start_date in start_dates.items():
    days_passed = (today - start_date).days
    days_left = target_days - days_passed
    
    print(f"\n[ {goal} ]")
    print(f"✅ {days_passed} day")
 
    
    if days_left > 0:
        print(f"⏳ {days_left} day")
        progress = (days_passed / target_days) * 100
        print(f"📊 {progress:.1f}%")
    else:
        print("🎉 Congratulations!")

print("\n" + "="*30)
print("Continue focusing on Python and building your future.")



