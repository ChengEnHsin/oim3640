"""Mini project: financial simulation for Cypher startup.

This draft implements a basic monthly simulation of user growth,
revenue, expenses and break-even analysis. It intentionally stays
"pure Python" (no third-party libraries) so it can be extended later.
"""

from typing import Dict, List, Optional


def simulate_months(
    months: int,
    starting_free: int = 1000,
    starting_premium: int = 50,
    monthly_new_free: float = 0.1,
    conversion_rate: float = 0.02,
    churn_free: float = 0.01,
    churn_premium: float = 0.005,
    premium_price: float = 10.0,
    job_post_price: float = 50.0,
    featured_listing_price: float = 20.0,
    jobs_per_user: float = 0.002,
    featured_per_user: float = 0.005,
    fixed_cost: float = 2000.0,
    variable_cost_per_user: float = 0.5,
) -> List[Dict[str, float]]:
    """Run a simple simulation over a number of months.

    Returns a list of dictionaries where each element contains
    the metrics for that month (users, revenue, costs, profit).
    """
    data: List[Dict[str, float]] = []
    free = starting_free
    premium = starting_premium

    for m in range(1, months + 1):
        # churn out users
        churned_free = free * churn_free
        churned_premium = premium * churn_premium
        free -= churned_free
        premium -= churned_premium

        # new free signups
        new_free = free * monthly_new_free
        free += new_free

        # conversions to premium
        converted = free * conversion_rate
        if converted > free:
            converted = free
        free -= converted
        premium += converted

        # revenue streams
        sub_revenue = premium * premium_price
        jobs = (free + premium) * jobs_per_user
        job_revenue = jobs * job_post_price
        featured = (free + premium) * featured_per_user
        featured_revenue = featured * featured_listing_price
        total_revenue = sub_revenue + job_revenue + featured_revenue

        # costs
        variable_cost = (free + premium) * variable_cost_per_user
        total_cost = fixed_cost + variable_cost
        profit = total_revenue - total_cost

        data.append(
            {
                "month": m,
                "free_users": free,
                "premium_users": premium,
                "new_free": new_free,
                "converted": converted,
                "churned_free": churned_free,
                "churned_premium": churned_premium,
                "revenue": total_revenue,
                "cost": total_cost,
                "profit": profit,
            }
        )
    return data


def print_summary(data: List[Dict[str, float]]) -> None:
    """Print a simple table of the results."""
    if not data:
        print("No data to display.")
        return
    header = (
        "Month | Free | Premium | Rev | Cost | Profit"
    )
    print(header)
    print("-" * len(header))
    for row in data:
        print(
            f"{row['month']:5d} | {int(row['free_users']):5d} | {int(row['premium_users']):7d} | "
            f"{row['revenue']:6.0f} | {row['cost']:5.0f} | {row['profit']:6.0f}"
        )


def find_break_even(data: List[Dict[str, float]]) -> Optional[int]:
    """Return the month number where cumulative profit becomes non-negative."""
    cumulative = 0.0
    for row in data:
        cumulative += row["profit"]
        if cumulative >= 0:
            return row["month"]
    return None


def run_scenario(**params) -> None:
    """Helper to run simulation with provided parameters and show results."""
    months = params.pop("months", 24)
    print("Running scenario with parameters:")
    for k, v in sorted(params.items()):
        print(f"  {k} = {v}")
    data = simulate_months(months=months, **params)
    print_summary(data)
    be = find_break_even(data)
    if be is not None:
        print(f"Break-even reached in month {be}")
    else:
        print("Break-even not reached in simulation period")


if __name__ == "__main__":
    # default run
    run_scenario()
