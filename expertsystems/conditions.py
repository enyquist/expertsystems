# expert systems libraries
from expertsystems.expert_system import ExpertSystem
from expertsystems.sme_utils import (
    DEBT_EQUITY_THRESHOLD,
    EARNINGS_GROWTH_THRESHOLD,
    EPSILON,
    LARGE_CAP_THRESHOLD,
    LOW_PEGY_RATIO_THRESHOLD,
    LOW_PRICE_THRESHOLD,
    MEDIUM_CAP_THRESHOLD,
    ROE_THRESHOLD,
    SECTOR_GROWTH_THRESHOLD,
    THRESHOLD_VOLUME,
    VALUE_DIV_YIELD_THRESHOLD,
    VALUE_PE_THRESHOLD,
)


def cheap_stock_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts is cheap, False otherwise.
    """
    return any(stock.price < LOW_PRICE_THRESHOLD for stock in engine.facts)


def low_pegy_ratio_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a PEGY ratio less than LOW_PEGY_RATIO_THRESHOLD, False otherwise.
    """
    return any(
        0 < stock.pe / (stock.earnings_growth + stock.dividend_yield) + EPSILON < LOW_PEGY_RATIO_THRESHOLD
        for stock in engine.facts
    )


def low_pe_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a P/E ratio less than VALUE_PE_THRESHOLD, False otherwise.
    """
    return any(0 < stock.pe < VALUE_PE_THRESHOLD for stock in engine.facts)


def high_dividend_yield_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a dividend yield greater
    than VALUE_DIV_YIELD_THRESHOLD, False otherwise.
    """
    return any(stock.dividend_yield > VALUE_DIV_YIELD_THRESHOLD for stock in engine.facts)


def high_volume_trading_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a volume greater than THRESHOLD_VOLUME, False otherwise.
    """
    return any(stock.volume > THRESHOLD_VOLUME for stock in engine.facts)


def large_cap_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a market cap greater than LARGE_CAP_THRESHOLD, False otherwise.
    """
    return any(stock.market_cap > LARGE_CAP_THRESHOLD for stock in engine.facts)


def medium_cap_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a market cap between
    MEDIUM_CAP_THRESHOLD and LARGE_CAP_THRESHOLD, False otherwise.
    """
    return any(MEDIUM_CAP_THRESHOLD <= stock.market_cap <= LARGE_CAP_THRESHOLD for stock in engine.facts)


def small_cap_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a market cap less than MEDIUM_CAP_THRESHOLD, False otherwise.
    """
    return any(stock.market_cap < MEDIUM_CAP_THRESHOLD for stock in engine.facts)


def value_stock_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts is a value stock, False otherwise.
    """
    return any(
        stock.pe < VALUE_PE_THRESHOLD and stock.dividend_yield > VALUE_DIV_YIELD_THRESHOLD for stock in engine.facts
    )


def growth_stock_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts is a growth stock, False otherwise.
    """
    return any(
        stock.earnings_growth > EARNINGS_GROWTH_THRESHOLD and stock.pe > VALUE_PE_THRESHOLD for stock in engine.facts
    )


def sector_growth_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts is in a sector with growth greater
    than SECTOR_GROWTH_THRESHOLD, False otherwise.
    """
    return any((stock.sector_growth > SECTOR_GROWTH_THRESHOLD) for stock in engine.facts)


def earnings_growth_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has earnings growth greater
    than EARNINGS_GROWTH_THRESHOLD, False otherwise.
    """
    return any(stock.earnings_growth > EARNINGS_GROWTH_THRESHOLD for stock in engine.facts)


def low_debt_equity_ratio_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a debt/equity ratio less than
    DEBT_EQUITY_THRESHOLD, False otherwise.
    """
    return any(stock.debt_equity_ratio < DEBT_EQUITY_THRESHOLD for stock in engine.facts)


def high_roe_condition(engine: ExpertSystem) -> bool:
    """
    Returns True if any stock in the engine.facts has a return on equity greater than ROE_THRESHOLD, False otherwise.
    """
    return any(stock.roe > ROE_THRESHOLD for stock in engine.facts)
