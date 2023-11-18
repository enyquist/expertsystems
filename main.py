# standard libraries
from typing import List

# third party libraries
import pandas as pd

# expert systems libraries
from expertsystems.actions import advise_undervalued_stocks
from expertsystems.conditions import undervalued_condition
from expertsystems.expert_system import ExpertSystem
from expertsystems.fact import Stock


def load_data() -> List[Stock]:
    """
    Load data from CSV file and return a list of Stock objects.
    """
    df = pd.read_csv("data/stocks.csv")
    return [Stock(**row) for _, row in df.iterrows()]


def interactive_engine():
    """Main Function"""
    es = ExpertSystem()

    # Define the rules with names
    @es.rule(undervalued_condition, name="advise_undervalued")
    def advise_undervalued(engine: ExpertSystem):
        advise_undervalued_stocks(engine)

    # Start interaction
    print("Welcome to the Stock Investment Expert System!\n\n")

    # Load data
    es.facts.extend(load_data())

    # Enable Rules  TODO - make this interactive
    es.enable_rule("advise_undervalued")

    # Make recommendation based on the enabled rules
    es.run()

    # Allow user to ask questions
    while True:
        answer = input("Do you want details on a specific recommendation? (y/n) ")
        if answer.lower() in ["y", "yes"]:
            answer = input("Which stock do you want details on? Enter the Ticker Symbol: ")
            for stock in es.facts:
                if stock.ticker == answer:
                    print()
                    for key, value in stock.__dict__.items():
                        if key == "price":
                            print(f"{key}: ${value:0.2f}")
                        elif key in ["dividend_yield", "earnings_growth", "sector_growth", "debt_equity_ratio", "roe"]:
                            print(f"{key}: {value:0.2%}")
                        elif key == "market_cap":
                            print(f"{key}: ${value:0.2f} billion")
                        elif key == "volume":
                            print(f"{key}: {value:,}")
                        else:
                            print(f"{key}: {value}")
                    print()
        else:
            print("Thank you for using the Stock Investment Expert System. Goodbye.")
            break


if __name__ == "__main__":
    interactive_engine()
