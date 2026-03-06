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


def run_sensitivity_analysis(
    base_params: Dict[str, float],
    scenarios: Dict[str, Dict[str, float]],
    months: int = 24
) -> Dict[str, List[Dict[str, float]]]:
    """Run multiple scenarios and return results for comparison.
    
    Args:
        base_params: Default parameters for the simulation
        scenarios: Dictionary of scenario names to parameter overrides
        months: Number of months to simulate
        
    Returns:
        Dictionary mapping scenario names to their simulation data
    """
    results = {}
    
    # Run base scenario
    results["base"] = simulate_months(months=months, **base_params)
    
    # Run each scenario
    for scenario_name, param_overrides in scenarios.items():
        scenario_params = base_params.copy()
        scenario_params.update(param_overrides)
        results[scenario_name] = simulate_months(months=months, **scenario_params)
    
    return results


def compare_scenarios(results: Dict[str, List[Dict[str, float]]]) -> None:
    """Print a comparison of key metrics across scenarios."""
    if not results:
        print("No results to compare.")
        return
    
    # Get final month data for each scenario
    final_data = {}
    break_even_months = {}
    
    for scenario, data in results.items():
        if data:
            final_data[scenario] = data[-1]  # Last month
            break_even_months[scenario] = find_break_even(data)
    
    # Print comparison table
    print("\nScenario Comparison (Final Month):")
    header = "Scenario | Free Users | Premium | Revenue | Cost | Profit | Break-even"
    print(header)
    print("-" * len(header))
    
    for scenario in sorted(results.keys()):
        if scenario in final_data:
            row = final_data[scenario]
            be = break_even_months[scenario]
            be_str = str(be) if be is not None else "N/A"
            print(
                f"{scenario:9s} | {int(row['free_users']):10d} | {int(row['premium_users']):8d} | "
                f"{row['revenue']:7.0f} | {row['cost']:4.0f} | {row['profit']:6.0f} | {be_str:10s}"
            )


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
    
    print("\n" + "="*60)
    print("SENSITIVITY ANALYSIS EXAMPLES")
    print("="*60)
    
    # Define base parameters
    base_params = {
        "starting_free": 1000,
        "starting_premium": 50,
        "monthly_new_free": 0.1,
        "conversion_rate": 0.02,
        "churn_free": 0.01,
        "churn_premium": 0.005,
        "premium_price": 10.0,
        "job_post_price": 50.0,
        "featured_listing_price": 20.0,
        "jobs_per_user": 0.002,
        "featured_per_user": 0.005,
        "fixed_cost": 2000.0,
        "variable_cost_per_user": 0.5,
    }
    
    # Define scenarios to test
    scenarios = {
        "higher_growth": {"monthly_new_free": 0.15, "conversion_rate": 0.03},
        "lower_growth": {"monthly_new_free": 0.05, "conversion_rate": 0.01},
        "higher_churn": {"churn_free": 0.02, "churn_premium": 0.01},
        "premium_pricing": {"premium_price": 15.0},
        "cost_reduction": {"fixed_cost": 1500.0, "variable_cost_per_user": 0.3},
    }
    
    # Run sensitivity analysis
    results = run_sensitivity_analysis(base_params, scenarios, months=24)
    
    # Compare scenarios
    compare_scenarios(results)
