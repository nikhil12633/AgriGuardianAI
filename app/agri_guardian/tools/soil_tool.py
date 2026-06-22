def analyze_soil(
    ph: float,
    nitrogen: str,
    phosphorus: str,
    potassium: str
):
    recommendations = []
    suitable_crops = []

    # pH Analysis
    if ph < 6:
        recommendations.append(
            "Soil is acidic. Consider adding agricultural lime."
        )
        suitable_crops.extend([
            "Groundnut",
            "Soybean",
            "Green Gram"
        ])

    elif ph > 8:
        recommendations.append(
            "Soil is alkaline. Consider gypsum treatment."
        )
        suitable_crops.extend([
            "Barley",
            "Cotton",
            "Mustard"
        ])

    else:
        recommendations.append(
            "Soil pH is suitable for most crops."
        )
        suitable_crops.extend([
            "Maize",
            "Wheat",
            "Sugarcane"
        ])

    # Nutrient Analysis

    if nitrogen.lower() == "low":
        recommendations.append(
            "Nitrogen deficiency detected. Apply compost or nitrogen fertilizers."
        )

    if phosphorus.lower() == "low":
        recommendations.append(
            "Phosphorus deficiency detected. Apply phosphate fertilizers."
        )

    if potassium.lower() == "low":
        recommendations.append(
            "Potassium deficiency detected. Apply potash fertilizers."
        )

    return {
        "ph": ph,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "recommendations": recommendations,
        "suitable_crops": suitable_crops
    }