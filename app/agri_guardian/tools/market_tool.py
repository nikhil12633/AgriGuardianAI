import csv
from pathlib import Path


def get_best_crop():
    """
    Reads crop prices and returns the highest-value crop.
    """

    csv_file = Path("datasets/crop_prices.csv")

    crops = []

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            crops.append({
                "crop": row["crop"],
                "price": float(row["price_per_quintal"])
            })

    best_crop = max(crops, key=lambda x: x["price"])

    return {
        "best_crop": best_crop["crop"],
        "price_per_quintal": best_crop["price"],
        "all_crops": crops
    }