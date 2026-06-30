from unittest.mock import patch, Mock
from app.agri_guardian.tools.weather_tool import get_weather


@patch("app.agri_guardian.tools.weather_tool.os.getenv")
@patch("app.agri_guardian.tools.weather_tool.requests.get")
def test_valid_city(mock_get, mock_getenv):
    """
    Test successful weather retrieval.
    """

    mock_getenv.return_value = "fake_api_key"

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Bidar",
        "main": {
            "temp": 30,
            "humidity": 65
        },
        "weather": [
            {
                "description": "clear sky"
            }
        ]
    }

    mock_get.return_value = mock_response

    result = get_weather("Bidar")

    assert result["city"] == "Bidar"
    assert result["temperature"] == 30
    assert result["humidity"] == 65
    assert result["weather"] == "clear sky"


@patch("app.agri_guardian.tools.weather_tool.os.getenv")
def test_missing_api_key(mock_getenv):
    """
    Test missing API key.
    """

    mock_getenv.return_value = None

    result = get_weather("Bidar")

    assert "error" in result
    assert result["error"] == "OPENWEATHER_API_KEY not found"


@patch("app.agri_guardian.tools.weather_tool.os.getenv")
@patch("app.agri_guardian.tools.weather_tool.requests.get")
def test_invalid_city(mock_get, mock_getenv):
    """
    Test invalid city.
    """

    mock_getenv.return_value = "fake_api_key"

    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.text = "city not found"

    mock_get.return_value = mock_response

    result = get_weather("UnknownCity")

    assert "error" in result


@patch("app.agri_guardian.tools.weather_tool.os.getenv")
@patch("app.agri_guardian.tools.weather_tool.requests.get")
def test_api_failure(mock_get, mock_getenv):
    """
    Test API server failure.
    """

    mock_getenv.return_value = "fake_api_key"

    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "internal server error"

    mock_get.return_value = mock_response

    result = get_weather("Bidar")

    assert "error" in result