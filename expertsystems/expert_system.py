class ExpertSystem:
    """
    An Expert System is a collection of rules and facts that can be used to make recommendations.
    """

    def __init__(self):  # noqa: D107
        self.rules = []
        self.facts = []
        self.enabled_rules = set()  # A set to keep track of enabled rule names

    def rule(self, condition, name=None):
        """
        A decorator that adds a rule to the expert system.
        """

        def decorator(func):
            self.rules.append((name, condition, func))
            return func

        return decorator

    def enable_rule(self, rule_name):
        """
        Enable a rule by name.
        """
        self.enabled_rules.add(rule_name)

    def disable_rule(self, rule_name):
        """
        Disable a rule by name.
        """
        self.enabled_rules.discard(rule_name)

    def run(self):
        """
        Run the expert system.
        """
        # Only run enabled rules
        for name, condition, action in self.rules:
            if name in self.enabled_rules and condition(self):
                action(self)
