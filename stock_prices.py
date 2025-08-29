stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3200,
    "MSFT": 230
}

def get_stock_portfolio():
    portfolio = {}
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").upper()
        if stock_name.lower() == 'done':
            break
        if stock_name not in stock_prices:
            print(f"Stock {stock_name} not found. Please try again.")
            continue
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    return portfolio

def calculate_total_investment(portfolio):
    total_investment = 0
    print("\nStock Portfolio:")
    print("----------------")
    for stock, quantity in portfolio.items():
        stock_value = stock_prices[stock] * quantity
        total_investment += stock_value
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${stock_value}")
    return total_investment

def save_portfolio(portfolio, total_investment):
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio:\n")
        f.write("----------------\n")
        for stock, quantity in portfolio.items():
            stock_value = stock_prices[stock] * quantity
            f.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${stock_value}\n")
        f.write(f"\nTotal Investment: ${total_investment}")
    print("Portfolio saved to portfolio.txt")

def main():
    print("Stock Portfolio Tracker")
    print("------------------------")
    portfolio = get_stock_portfolio()
    total_investment = calculate_total_investment(portfolio)
    print(f"\nTotal Investment: ${total_investment}")
    save = input("Save portfolio to file? (yes/no): ").lower()
    if save == 'yes':
        save_portfolio(portfolio, total_investment)

if _name_ == "_main_":
    main()