print("---------------------------------")
print("     Welcome to Stock Portfolio  ")
print("---------------------------------")
print("   Welcome to our stock portfolio tracker")

stock_prices = {
    "apple": 180,
    "banana": 60,
    "grapes": 100,
    "rice": 200,
    "google": 500,
    "bz mor": 600,
}

portfolio = {}
total_value = 0

while True:
    stock_symbol = input("Enter stock symbol (or 'done' to finish): ").lower().strip()

    if stock_symbol == 'done':
        print("\nPortfolio Summary:")
        with open("portfolio_summary.txt", "w") as file:
            file.write("Portfolio Summary:\n")
            for symbol, quantity in portfolio.items():
                price = stock_prices[symbol]
                investment_value = price * quantity

                print(f"stock : {symbol}")
                print(f"quantity : {quantity}")
                print(f"price per share : {price}")
                print(f"investment value : {investment_value}")
                print("-----------------------------")

                file.write(f"stock : {symbol}\n")
                file.write(f"quantity : {quantity}\n")
                file.write(f"price per share : {price}\n")
                file.write(f"investment value : {investment_value}\n")
                file.write("-----------------------------\n")

            file.write(f"Total investment value: {total_value}\n")

        print(f"Total investment value: {total_value}")
        break

    elif stock_symbol in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock_symbol}: "))
            if quantity > 0:
                portfolio[stock_symbol] = portfolio.get(stock_symbol, 0) + quantity

                price = stock_prices[stock_symbol]
                investment_value = price * quantity
                total_value += investment_value

                print(f"\nstock : {stock_symbol}")
                print(f"quantity : {quantity}")
                print(f"price per share : {price}")
                print(f"investment value : {investment_value}")
            else:
                print("Please enter a quantity greater than 0")
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
    else:
        print("Please enter a valid stock symbol")