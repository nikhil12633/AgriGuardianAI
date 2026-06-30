from .market_tool import get_best_crop
from .soil_tool import analyze_soil


def generate_farm_advice(
    season,
    soil_type,
    water_requirement,
    ph,
    nitrogen,
    phosphorus,
    potassium
):

    soil = analyze_soil(
        ph,
        nitrogen,
        phosphorus,
        potassium,
        soil_type,
        season
    )

    market = get_best_crop(
        season=season,
        soil_type=soil_type,
        water_requirement=water_requirement,
        candidate_crops=soil["suitable_crops"]
    )

    if "error" in market:

        return {
            "error":
                market["error"],

            "soil_recommendations":
                soil["recommendations"],

            "soil_suitable_crops":
                soil["suitable_crops"]
        }

    return {
        "recommended_crop":
            market["recommended_crop"],

        "market_price":
            market["market_price"],

        "profit_score":
            market["profit_score"],

        "soil_recommendations":
            soil["recommendations"],

        "soil_suitable_crops":
            soil["suitable_crops"],

        "reasoning": [
            f"Season: {season}",
            f"Soil: {soil_type}",
            f"Water: {water_requirement}",
            "Selected using soil suitability and market profitability"
        ]
    }