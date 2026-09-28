"""Time value of money (CFA Level I, Quantitative Methods).

Starter exercise: read each function, then try changing the inputs
at the bottom and run:  python exercises/tvm.py
"""


def future_value(pv, rate, n):
    """FV = PV * (1 + r)^n"""
    return pv * (1 + rate) ** n


def present_value(fv, rate, n):
    """PV = FV / (1 + r)^n"""
    return fv / (1 + rate) ** n


def npv(rate, cash_flows):
    """Net present value. cash_flows[0] happens today (t = 0)."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))


if __name__ == "__main__":
    print(f"FV of 1,000 at 5% for 10 years: {future_value(1000, 0.05, 10):,.2f}")
    print(f"PV of 1,000 in 10 years at 5%:  {present_value(1000, 0.05, 10):,.2f}")
    print(f"NPV of [-1000, 300, 400, 500] at 8%: {npv(0.08, [-1000, 300, 400, 500]):,.2f}")
