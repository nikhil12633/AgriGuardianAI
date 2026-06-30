from app.agri_guardian.tools.advisory_tool import generate_farm_advice


def test_kharif_black_medium():
    result = generate_farm_advice(
        season="Kharif",
        soil_type="Black",
        water_requirement="Medium",
        ph=6.8,
        nitrogen="low",
        phosphorus="medium",
        potassium="high"
    )

    assert result["recommended_crop"] == "Tur"
    assert result["profit_score"] == 9
    assert "soil_recommendations" in result
    assert "reasoning" in result


def test_rabi_sandy_low():
    result = generate_farm_advice(
        season="Rabi",
        soil_type="Sandy",
        water_requirement="Low",
        ph=7.0,
        nitrogen="medium",
        phosphorus="medium",
        potassium="medium"
    )

    assert result["recommended_crop"] == "Cumin"
    assert result["profit_score"] == 10


def test_kharif_red_high():
    result = generate_farm_advice(
        season="Kharif",
        soil_type="Red",
        water_requirement="High",
        ph=6.5,
        nitrogen="medium",
        phosphorus="medium",
        potassium="high"
    )

    assert result["recommended_crop"] == "Turmeric"
    assert result["profit_score"] == 10


def test_invalid_combination():
    result = generate_farm_advice(
        season="Summer",
        soil_type="Rocky",
        water_requirement="Extreme",
        ph=7.0,
        nitrogen="medium",
        phosphorus="medium",
        potassium="medium"
    )

    assert "error" in result