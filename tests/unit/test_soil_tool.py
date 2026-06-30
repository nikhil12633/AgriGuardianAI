from app.agri_guardian.tools.soil_tool import analyze_soil


def test_acidic_soil():
    result = analyze_soil(
        ph=5.3,
        nitrogen="low",
        phosphorus="medium",
        potassium="medium"
    )

    assert result["ph"] == 5.3
    assert "Groundnut" in result["suitable_crops"]
    assert any(
        "acidic" in r.lower()
        for r in result["recommendations"]
    )


def test_neutral_soil():
    result = analyze_soil(
        ph=6.8,
        nitrogen="medium",
        phosphorus="medium",
        potassium="medium"
    )

    assert "Maize" in result["suitable_crops"]
    assert "Wheat" in result["suitable_crops"]


def test_alkaline_soil():
    result = analyze_soil(
        ph=8.5,
        nitrogen="high",
        phosphorus="low",
        potassium="medium"
    )

    assert "Cotton" in result["suitable_crops"]

    assert any(
        "alkaline" in r.lower()
        for r in result["recommendations"]
    )


def test_nitrogen_deficiency():
    result = analyze_soil(
        ph=6.5,
        nitrogen="low",
        phosphorus="medium",
        potassium="medium"
    )

    assert any(
        "nitrogen" in r.lower()
        for r in result["recommendations"]
    )