
from traveltail.models import Recommendation, Flight, Hotel
from traveltail.ranking import rank_recommendations

def make_dummy(shift=0):
    f = Flight(id="F", origin="A", destination="B", depart_at="2025-01-01T00:00:00",
               arrive_at="2025-01-01T01:00:00", duration_minutes=60+shift, price_usd=100+shift, airline="X")
    h = Hotel(id="H", city="B", name="H", checkin="2025-01-01", checkout="2025-01-02", nights=1, price_usd=50, rating=3.0)
    return Recommendation(f,h, total_cost_usd=f.price_usd+h.price_usd, total_time_minutes=f.duration_minutes, loyalty_score=3.0, score=0.0)

def test_rank_order_by_cost():
    recos = [make_dummy(0), make_dummy(100)]
    ranked = rank_recommendations(recos, weights={"cost":0.9,"time":0.05,"loyalty":0.05})
    assert ranked[0].total_cost_usd < ranked[1].total_cost_usd
