import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP


def _data_path() -> Path:
    configured_path = os.environ.get("ACTIVITIES_DATA")
    if configured_path:
        return Path(configured_path).expanduser()

    return Path.cwd() / "app" / "backend" / "data" / "activities.json"


def _load_activities() -> dict:
    path = _data_path()
    if not path.exists():
        raise FileNotFoundError(
            f"Activities data file not found at {path}. "
            "Open a workspace that contains app/backend/data/activities.json "
            "or set ACTIVITIES_DATA for the school-activities MCP server."
        )

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


mcp = FastMCP("school-activities")


@mcp.tool()
def list_activities() -> list[str]:
    """Return the names of all available school activities."""
    activities = _load_activities()
    return list(activities.keys())


@mcp.tool()
def get_signups_count(activity: str) -> int:
    """Return how many students have signed up for the given activity.

    Raises ValueError if the activity name is not recognised.
    """
    activities = _load_activities()
    if activity not in activities:
        raise ValueError(f"Unknown activity: {activity!r}")
    return len(activities[activity]["participants"])


if __name__ == "__main__":
    mcp.run()