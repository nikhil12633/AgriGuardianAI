import pytest
from pydantic import ValidationError

from app.agri_guardian.models.farm_profile import FarmProfile


def test_valid_profile():
    profile = FarmProfile(
        state="Karnataka",
        district="Bidar",
        village="Humnabad",
        land_size_acres=5.0,
        irrigation_type="Drip",
        current_crop="Tur"
    )

    assert profile.state == "Karnataka"
    assert profile.district == "Bidar"
    assert profile.land_size_acres == 5.0
    assert profile.current_crop == "Tur"


def test_invalid_land_size():
    with pytest.raises(ValidationError):
        FarmProfile(
            state="Karnataka",
            district="Bidar",
            village="Humnabad",
            land_size_acres="invalid",
            irrigation_type="Drip",
            current_crop="Tur"
        )
