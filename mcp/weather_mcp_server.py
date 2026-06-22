from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")


@mcp.tool()
def get_weather(city: str) -> dict:
    """
    Return weather information.
    """

    return {
        "city": city,
        "status": "success",
        "message": f"Weather lookup requested for {city}"
    }


if __name__ == "__main__":
    print("Starting Weather MCP Server...")
    mcp.run()