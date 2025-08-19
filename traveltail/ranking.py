
from typing import List, Tuple
from .models import Recommendation

def _minmax(values: List[float]) -> Tuple[float, float]:
    mn, mx = min(values), max(values)
    if mn == mx:
        return mn, mn + 1.0
    return mn, mx

def rank_recommendations(recos: List[Recommendation], weights=None) -> List[Recommendation]:
    if not recos:
        return []
    weights = weights or {"cost": 0.5, "time": 0.3, "loyalty": 0.2}
    costs = [r.total_cost_usd for r in recos]
    times = [r.total_time_minutes for r in recos]
    loyals = [r.loyalty_score for r in recos]
    cmin, cmax = _minmax(costs)
    tmin, tmax = _minmax(times)
    lmin, lmax = _minmax(loyals)
    for r in recos:
        c_norm = (r.total_cost_usd - cmin) / (cmax - cmin)
        t_norm = (r.total_time_minutes - tmin) / (tmax - tmin)
        l_norm = (r.loyalty_score - lmin) / (lmax - lmin)
        r.score = (weights["cost"] * (1 - c_norm)
                   + weights["time"] * (1 - t_norm)
                   + weights["loyalty"] * (l_norm))
    return sorted(recos, key=lambda x: x.score, reverse=True)
