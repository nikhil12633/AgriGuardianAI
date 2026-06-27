from .market_tool import get_best_crop
from .soil_tool import analyze_soil


def generate_farm_advice(
    ph: float,
    nitrogen: str,
    phosphorus: str,
    potassium: str
):
    """
    Combines soil and market analysis.
    """

    soil = analyze_soil(
        ph,
        nitrogen,
        phosphorus,
        potassium
    )

    market = get_best_crop()

    return {
        "recommended_crop": market["best_crop"],
        "market_price": market["price_per_quintal"],
        "soil_recommendations": soil["recommendations"]
    }