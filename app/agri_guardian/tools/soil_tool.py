def analyze_soil(
    ph,
    nitrogen,
    phosphorus,
    potassium,
    soil_type=None,
    season=None
):
    recommendations = []
    suitable_crops = []

    # Normalize
    season = str(season).lower() if season else ""
    soil = str(soil_type).lower() if soil_type else ""

    # Season recommendations
    if season == "kharif":
        suitable_crops.extend([
            "Cotton",
            "Soybean",
            "Tur",
            "Jowar",
            "Groundnut"
        ])

    elif season == "rabi":
        suitable_crops.extend([
            "Wheat"
        ])

    # Soil recommendations
    if "black" in soil:
        suitable_crops.extend([
            "Cotton",
            "Soybean",
            "Tur",
            "Groundnut",
            "Jowar"
        ])

    elif "red" in soil:
        suitable_crops.extend([
            "Tur",
            "Green Gram",
            "Black Gram",
            "Soybean",
            "Groundnut"
        ])

    elif "loamy" in soil:
        suitable_crops.extend([
            "Tomato",
            "Wheat"
        ])

    # pH analysis
    if ph < 6:
        recommendations.append(
            "Soil is acidic. Apply agricultural lime."
        )

        suitable_crops.extend([
            "Groundnut",
            "Soybean",
            "Green Gram"
        ])

    elif ph > 8:
        recommendations.append(
            "Soil is alkaline. Apply gypsum."
        )

        suitable_crops.extend([
            "Cotton"
        ])

    else:
        recommendations.append(
            "Soil pH is suitable."
        )

    # Nutrients
    if nitrogen.lower() == "low":
        recommendations.append(
            "Apply nitrogen fertilizers or compost."
        )

    if phosphorus.lower() == "low":
        recommendations.append(
            "Apply phosphate fertilizers."
        )

    if potassium.lower() == "low":
        recommendations.append(
            "Apply potash fertilizers."
        )

    # Remove duplicates
    priority = [
    "Cotton",
    "Tur",
    "Soybean",
    "Groundnut",
    "Jowar",
    "Green Gram",
    "Black Gram",
    "Wheat",
    "Tomato"
    ]

    suitable_crops = [
    	crop
    	for crop in priority
    	if crop in suitable_crops
    ]

    return {
        "ph": ph,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "recommendations": recommendations,
        "suitable_crops": suitable_crops
       }