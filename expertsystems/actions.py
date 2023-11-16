# expert systems libraries
from expertsystems.expert_system import ExpertSystem
from expertsystems.sme_utils import (
    DEBT_EQUITY_THRESHOLD,
    EARNINGS_GROWTH_THRESHOLD,
    EPSILON,
    LOW_PEGY_RATIO_THRESHOLD,
    VALUE_DIV_YIELD_THRESHOLD,
    VALUE_PE_THRESHOLD,
)


def advise_undervalued_stocks(engine: ExpertSystem) -> None:
    """Advise on undervalued stocks based on the following criteria:"""
    print("Evaluating undervalued stocks...\n")
    stocks_with_reasons = []
    for stock in engine.facts:
        stock.pegy_ratio = stock.pe / ((stock.earnings_growth + stock.dividend_yield) + EPSILON)
        reasons = []

        # Check individual criteria
        if 0 < stock.pegy_ratio < LOW_PEGY_RATIO_THRESHOLD:
            reasons.append(f"the PEGY Ratio is lower than {LOW_PEGY_RATIO_THRESHOLD} ({stock.pegy_ratio:.2f})")
        if 0 < stock.pe < VALUE_PE_THRESHOLD:
            reasons.append(f"the P/E ratio is lower than {VALUE_PE_THRESHOLD} ({stock.pe})")
        if stock.dividend_yield > VALUE_DIV_YIELD_THRESHOLD:
            reasons.append(
                f"the dividend yield is higher than {VALUE_DIV_YIELD_THRESHOLD:0.2%} ({stock.dividend_yield:0.2%})"
            )
        if 0 < stock.debt_equity_ratio < DEBT_EQUITY_THRESHOLD:
            reasons.append(f"the debt/equity ratio is lower than {DEBT_EQUITY_THRESHOLD} ({stock.debt_equity_ratio})")

        # Check combinations of criteria
        if 0 < stock.pe < VALUE_PE_THRESHOLD and stock.dividend_yield > VALUE_DIV_YIELD_THRESHOLD:
            reasons.append(
                f"both the P/E ratio ({stock.pe}) and dividend yield ({stock.dividend_yield:0.2%}) "
                "suggest this is a value stock"
            )
        if stock.earnings_growth > EARNINGS_GROWTH_THRESHOLD and stock.pe > VALUE_PE_THRESHOLD:
            reasons.append(
                f"the earnings growth is higher than {EARNINGS_GROWTH_THRESHOLD:0.2%} ({stock.earnings_growth:0.2%}) "
                "and the P/E ratio is higher than {VALUE_PE_THRESHOLD} ({stock.pe}) suggest this is a growth stock"
            )

        if reasons:
            stocks_with_reasons.append((stock, reasons))

    # sort stocks by the number of reasons
    stocks_with_reasons.sort(key=lambda x: len(x[1]), reverse=True)

    # print the stocks with the most reasons first
    for stock, reasons in stocks_with_reasons:
        print(f"Stock {stock.name} ({stock.ticker}) is recommended as it meets {len(reasons)} criteria:")
        for reason in reasons:
            print(f"\t* {reason}")
        print("\n")
