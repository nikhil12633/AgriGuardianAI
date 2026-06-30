from app.agri_guardian.tools.market_tool import get_best_crop


def test_kharif_black_medium():
    result = get_best_crop(
        season="Kharif",
        soil_type="Black",
        water_requirement="Medium"
    )

    assert result["recommended_crop"] == "Tur"
    assert result["profit_score"] == 9


def test_kharif_sandy_low():
    result = get_best_crop(
        season="Kharif",
        soil_type="Sandy",
        water_requirement="Low"
    )

    assert result["recommended_crop"] == "Sesame"
    assert result["profit_score"] == 9


def test_rabi_sandy_low():
    result = get_best_crop(
        season="Rabi",
        soil_type="Sandy",
        water_requirement="Low"
    )

    assert result["recommended_crop"] == "Cumin"
    assert result["profit_score"] == 10


def test_rabi_loamy_medium():
    result = get_best_crop(
        season="Rabi",
        soil_type="Loamy",
        water_requirement="Medium"
    )

    assert result["recommended_crop"] == "Garlic"
    assert result["profit_score"] == 10


def test_invalid_crop_search():
    result = get_best_crop(
        season="Summer",
        soil_type="Rocky",
        water_requirement="Extreme"
    )

    assert "error" in result