# standard libraries
from functools import wraps
from typing import Any, Callable

EXPERT_SYSTEM = "ExpertSystem"


class Rule:
    """
    A Rule is a decorator that wraps a function and adds it to the Expert System.
    """

    def __init__(self, condition: Callable[[EXPERT_SYSTEM], bool]):  # noqa: D107
        self.condition = condition

    def __call__(self, f: Callable) -> Callable:  # noqa: D102
        @wraps(f)
        def wrapped_rule(engine: EXPERT_SYSTEM, *args: Any, **kwargs: Any) -> Any:
            if self.condition(engine):
                return f(engine, *args, **kwargs)

        return wrapped_rule
