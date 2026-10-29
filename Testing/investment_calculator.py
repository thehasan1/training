#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Companies = ["apple", "microsoft", "gigabet", "amazon", "meta"]

Companies_Worth = {
    "apple": 3000000000000,
    "microsoft": 4000000000000,
    "gigabet": 2500000000000,
    "amazon": 200000000000,
    "meta": 100000000000
}

Companies_stock_price = {
    "apple": 150,
    "microsoft": 300,
    "gigabet": 200,
    "amazon": 250,
    "meta": 180
}

print("=" * 70)
print("💼 Stock Investment Portfolio Calculator 💼")
print("=" * 70)
print()

print("📊 Available Companies:")
print("-" * 70)
for idx, company in enumerate(Companies, 1):
    print(f"{idx}. {company.capitalize():20} - Worth: ${Companies_Worth[company]:,} | Stock Price: ${Companies_stock_price[company]}")
print("-" * 70)
print()

favourite_company = input("Which Company do you want to buy their stocks: ").lower()

if favourite_company not in Companies:
    print(f"❌ {favourite_company} is not in our list. Please try again.")
else:
    print(f"✅ You have selected {favourite_company.upper()}.")
    print(f"📈 {favourite_company.capitalize()} is worth ${Companies_Worth[favourite_company]:,}.")
    print()
    
    Companies_stock_buying = int(input("How many stocks do you want to buy: "))
    
    print()
    print("=" * 70)
    print("📊 Investment Results 📊")
    print("=" * 70)
    print(f"Company Selected:     {favourite_company.upper()}")
    print(f"Stock Price:          ${Companies_stock_price[favourite_company]:,}")
    print(f"Number of Stocks:     {Companies_stock_buying:,}")
    print("-" * 70)
    
    your_Shares_value = Companies_stock_buying * Companies_stock_price[favourite_company]
    your_Shares_percentage = (Companies_stock_buying / Companies_Worth[favourite_company]) * 100
    
    print(f"💰 Your Net Worth:               ${your_Shares_value:,.2f}")
    print(f"📊 Your Ownership Percentage:    {your_Shares_percentage:.4f}%")
    print("=" * 70)
    print()
    
    print("Thank you for using the Investment Calculator! 👋")
