import csv
from pathlib import Path


def normalize(text):
    if not text:
        return ""

    text = text.lower().strip()

    mapping = {
        "black soil": "black",
        "red soil": "red",
        "loamy soil": "loamy",
        "mansoon": "kharif",
        "monsoon": "kharif"
    }

    return mapping.get(text, text)


def get_best_crop(
    season=None,
    soil_type=None,
    water_requirement=None,
    candidate_crops=None
):

    season = normalize(season)
    soil_type = normalize(soil_type)
    water_requirement = normalize(water_requirement)

    csv_file = Path("datasets/crop_prices.csv")

    crops = []

    with open(csv_file, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            crops.append(
                {
                    "crop": row["crop"],
                    "season": row["season"].lower(),
                    "price": float(row["price_per_quintal"]),
                    "soil_type": row["soil_type"].lower(),
                    "water_requirement": row["water_requirement"].lower(),
                    "profit_score": int(row["profit_score"]),
                }
            )

    # candidate filtering
    if candidate_crops:

        candidate_crops = [
            x.lower()
            for x in candidate_crops
        ]

        crops = [
            c
            for c in crops
            if c["crop"].lower() in candidate_crops
        ]

    # season filter
    if season:

        crops = [
            c
            for c in crops
            if c["season"] == season
            or c["season"] == "all"
        ]

    # soil filter
    if soil_type:

        soil_filtered = [
            c
            for c in crops
            if c["soil_type"] == soil_type
        ]

        if soil_filtered:
            crops = soil_filtered

    # water filter
    if water_requirement:

        water_filtered = [
            c
            for c in crops
            if c["water_requirement"] == water_requirement
        ]

        if water_filtered:
            crops = water_filtered

    # fallback if nothing matched
    if not crops:

        with open(csv_file, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if (
                    candidate_crops
                    and row["crop"].lower()
                    in candidate_crops
                ):

                    return {
                        "recommended_crop": row["crop"],
                        "market_price": row["price_per_quintal"],
                        "profit_score": row["profit_score"],
                        "warning": "Partial market match",
                    }

        return {
            "error": "No suitable crops found"
        }

    best_crop = max(
        crops,
        key=lambda x: (
            x["profit_score"],
            x["price"],
        ),
    )

    return {
        "recommended_crop":
            best_crop["crop"],

        "season":
            best_crop["season"],

        "soil_type":
            best_crop["soil_type"],

        "water_requirement":
            best_crop["water_requirement"],

        "market_price":
            best_crop["price"],

        "profit_score":
            best_crop["profit_score"],
    }