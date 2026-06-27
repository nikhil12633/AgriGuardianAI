from .market_tool import get_best_crop
from .soil_tool import analyze_soil


def generate_farm_advice(
    season: str,
    soil_type: str,
    water_requirement: str,
    ph: float,
    nitrogen: str,
    phosphorus: str,
    potassium: str
):
    """
    Generates final farming advice by combining
    soil analysis and market intelligence.
    """

    soil = analyze_soil(
        ph,
        nitrogen,
        phosphorus,
        potassium
    )

    market = get_best_crop(
        season=season,
        soil_type=soil_type,
        water_requirement=water_requirement
    )

    if "error" in market:
        return market

    return {
        "recommended_crop":
            market["recommended_crop"],

        "market_price":
            market["market_price"],

        "profit_score":
            market["profit_score"],

        "soil_recommendations":
            soil["recommendations"],

        "reasoning": [
            f"Suitable for {season} season",
            f"Suitable for {soil_type} soil",
            f"Requires {water_requirement} water",
            "Selected using profitability and market price"
        ]
    }