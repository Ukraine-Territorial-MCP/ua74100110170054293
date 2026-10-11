import json
from pathlib import Path
from mcp.server.mcpserver import MCPServer

BASE = Path(__file__).resolve().parent
data = json.loads((BASE / "data.json").read_text(encoding="utf-8"))
village = data["village"]
geo = data["geography"]

server = MCPServer(
    name="village-" + village["katottg"].lower(),
    title="Село " + village["name"],
    description="MCP села " + village["name"],
    version="0.1.0",
)

@server.tool()
def get_identity() -> dict:
    """Назва, КАТОТТГ та адміністративна належність."""
    return village

@server.tool()
def get_basic_profile() -> dict:
    """Базовий профіль із географічними даними."""
    return {**village, "geography": geo}

@server.tool()
def get_sources() -> dict:
    """Джерела адміністративних і географічних даних."""
    return data["sources"]

if __name__ == "__main__":
    server.run(transport="stdio")
