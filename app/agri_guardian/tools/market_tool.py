import csv
from pathlib import Path


def get_best_crop(
    season: str = None,
    soil_type: str = None,
    water_requirement: str = None
):
    """
    Returns the best crop based on
    season, soil type, water requirement,
    and profitability.
    """

    csv_file = Path("datasets/crop_prices.csv")

    crops = []

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            crops.append({
                "crop": row["crop"],
                "season": row["season"],
                "price": float(row["price_per_quintal"]),
                "soil_type": row["soil_type"],
                "water_requirement": row["water_requirement"],
                "profit_score": int(row["profit_score"])
            })

    # Filter by season
    if season:
        crops = [
            c for c in crops
            if c["season"].lower() == season.lower()
            or c["season"] == "All"
        ]

    # Filter by soil
    if soil_type:
        crops = [
            c for c in crops
            if c["soil_type"].lower() == soil_type.lower()
        ]

    # Filter by water requirement
    if water_requirement:
        crops = [
            c for c in crops
            if c["water_requirement"].lower()
            == water_requirement.lower()
        ]

    if not crops:
        return {
            "error": "No suitable crops found."
        }

    # Score = profitability + market price
    best_crop = max(
        crops,
        key=lambda x: (
            x["profit_score"],
            x["price"]
        )
    )

    return {
        "recommended_crop": best_crop["crop"],
        "season": best_crop["season"],
        "soil_type": best_crop["soil_type"],
        "water_requirement":
            best_crop["water_requirement"],
        "market_price":
            best_crop["price"],
        "profit_score":
            best_crop["profit_score"]
    }