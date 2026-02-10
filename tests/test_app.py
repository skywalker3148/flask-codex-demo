from datetime import datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_healthcheck_endpoint_returns_ok_with_utc_iso8601_timestamp():
    client = app.test_client()

    response = client.get("/healthcheck")

    assert response.status_code == 200
    body = response.get_json()
    assert body["ok"] is True
    assert isinstance(body["timestamp"], str)

    parsed_timestamp = datetime.fromisoformat(body["timestamp"].replace("Z", "+00:00"))
    assert parsed_timestamp.tzinfo is not None
    assert parsed_timestamp.utcoffset().total_seconds() == 0
