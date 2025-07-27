import sys
print("Python executable being used:")
print(sys.executable)

try:
    import matplotlib.pyplot as plt
    print("matplotlib is installed and imported successfully!")
except ModuleNotFoundError:
    print("matplotlib is NOT installed in this Python environment.")

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore: RED = GREEN = YELLOW = RESET = ''
    class Style: BRIGHT = NORMAL = ''

print("Python executable being used:")
print(sys.executable)

# Step 1: Define current prices and purchase prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330
}

purchase_prices = {
    "AAPL": 150,
    "TSLA": 300,
    "GOOGL": 2500,
    "MSFT": 350
}

# Step 2: Take user input
portfolio = {}
print("\n📥 Enter your stock holdings (type 'done' when finished):")
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        try:
            custom_price = float(input(f"{stock} not found. Enter its current price: $"))
            stock_prices[stock] = custom_price
            purchase_price = float(input(f"Enter your purchase price for {stock}: $"))
            purchase_prices[stock] = purchase_price
        except ValueError:
            print(Fore.RED + "❌ Invalid price. Try again.")
            continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print(Fore.RED + "❌ Invalid quantity. Try again.")
