# standard libraries
from typing import Any


class Fact:
    """
    A Fact is a data structure that stores an arbitrary number of attributes.
    """

    def __init__(self, **kwargs: Any):  # noqa: D107
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"


class Stock(Fact):
    """
    A Stock is a Fact that stores the attributes of a stock.
    """

    def __init__(  # noqa: D107
        self,
        name: str,
        ticker: str,
        price: float,
        pe: float,
        dividend_yield: float,
        volume: int,
        market_cap: float,
        earnings_growth: float,
        sector_growth: float,
        sector: str,
        debt_equity_ratio: float,
        roe: float,
    ):
        super().__init__(
            name=name,
            ticker=ticker,
            price=price,
            pe=pe,
            dividend_yield=dividend_yield,
            volume=volume,
            market_cap=market_cap,
            earnings_growth=earnings_growth,
            sector_growth=sector_growth,
            sector=sector,
            debt_equity_ratio=debt_equity_ratio,
            roe=roe,
        )

        def __repr__(self) -> str:
            return (
                f"Stock:{self.name},\n"
                f"\tTicker: {self.ticker},\n"
                f"\tPrice: {self.price},\n"
                f"\tP/E Ratio: {self.pe},\n"
                f"\tDividend Yield: {self.dividend_yield},\n"
                f"\tVolume: {self.volume},\n"
                f"\tMarket Cap: {self.market_cap},\n"
                f"\tEarnings Growth: {self.earnings_growth},\n"
                f"\tSector Growth: {self.sector_growth},\n"
                f"\tSector: {self.sector},\n"
                f"\tDebt/Equity Ratio: {self.debt_equity_ratio},\n"
                f"\tReturn on Equity: {self.roe}\n"
            )
