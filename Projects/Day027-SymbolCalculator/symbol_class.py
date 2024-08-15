import pandas
from math import ceil


class ArcaneSymbol:
    def __init__(self, symbol_type="Vanishing Journey", curr_level=1,
                 curr_symbols=0):
        self.symbol_type = symbol_type
        self.curr_level = curr_level
        self.curr_symbols = curr_symbols
        self.max_level = 20
        self.symbols_per_day = self.daily_symbols()

    def symbol_info(self):
        symbol_costs_df = pandas.read_csv("symbol_costs.csv")
        symbol_costs_df = symbol_costs_df.set_index("Symbol")

        multiplicative_cost = symbol_costs_df.loc[self.symbol_type,
        "Multiplicative_Cost"]
        additive_cost = symbol_costs_df.loc[self.symbol_type, "Additive_Cost"]

        return multiplicative_cost, additive_cost

    def daily_symbols(self):
        symbol_costs_df = pandas.read_csv("symbol_costs.csv")
        symbol_costs_df = symbol_costs_df.set_index("Symbol")

        symbols_per_day = symbol_costs_df.loc[self.symbol_type, "Quest_Reward"] + \
                          symbol_costs_df.loc[self.symbol_type, "Minigame_Reward"]

        return symbols_per_day

    def symbol_needs(self):
        multiplicative_meso_cost, additive_meso_cost = self.symbol_info()

        symbols_remaining = sigma_sum(self.curr_level, self.max_level,
                                      lambda i: (i ** 2 + 11))

        mesos_needed = ((self.curr_level + self.max_level - 1) *
                        (self.max_level - self.curr_level) / 2 *
                        multiplicative_meso_cost) + \
                       ((self.max_level - self.curr_level) *
                        additive_meso_cost)

        time_needed = ceil(symbols_remaining / self.symbols_per_day)

        return symbols_remaining, mesos_needed, time_needed


def sigma_sum(start, end, expression):
    return sum(expression(i) for i in range(start, end))
