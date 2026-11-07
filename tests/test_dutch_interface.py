"""Exercise the Dutch locale through settings, pages and stored templates."""

import re
from collections import Counter
from datetime import UTC, datetime

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(monkeypatch, tmp_path):
    import localplaud.db.session as db
    from localplaud.api.app import app
    from localplaud.config import get_settings

    monkeypatch.setenv("LOCALPLAUD_STORE__DATABASE_URL", f"sqlite:///{tmp_path / 'dutch.db'}")
    monkeypatch.setenv("LOCALPLAUD_POLLER__DOWNLOAD_DIR", str(tmp_path / "audio"))
    monkeypatch.setenv("LOCALPLAUD_PLAUD__OFFICIAL__TOKENS_PATH", str(tmp_path / "tokens.json"))
    monkeypatch.setattr(db, "_engine", None)
    monkeypatch.setattr(db, "_Session", None)
    get_settings(reload=True)
    with TestClient(app) as test_client:
        yield test_client
    if db._engine:
        db._engine.dispose()


def test_dutch_locale_persists_and_renders_pages(client):
    prefs = client.get("/api/preferences/workspace").json()
    assert prefs["locale"] == "en"
    response = client.put("/api/preferences/workspace", json=prefs | {"locale": "nl"})
    assert response.status_code == 200
    assert client.get("/api/preferences/workspace").json()["locale"] == "nl"

    for path, visible in (
        ("/home", "Nog geen opnames."),
        ("/settings", '<option value="nl" selected>Nederlands</option>'),
        ("/templates?tab=explore", "Uitgebreide vergadernotulen"),
        ("/status", "Systeemstatus"),
    ):
        page = client.get(path)
        assert page.status_code == 200
        assert '<html lang="nl"' in page.text
        assert visible in page.text

    response = client.put("/api/preferences/workspace", json=prefs | {"locale": "en"})
    assert response.status_code == 200
    assert '<html lang="en"' in client.get("/settings").text


def test_dutch_templates_preserve_previous_prompt_versions(client):
    previous = {
        row["id"]: row
        for row in client.get("/api/note-templates").json()["templates"]
        if row["is_builtin"]
    }
    prefs = client.get("/api/preferences/workspace").json()
    response = client.put("/api/preferences/workspace", json=prefs | {"locale": "nl"})
    assert response.status_code == 200
    rows = client.get("/api/note-templates?include_history=true").json()["templates"]
    active = [row for row in rows if row["is_builtin"] and row["is_active"]]
    assert len(active) == 10
    assert all(row["provenance"] == "plaud-web-translated-nl" for row in active)
    for row in rows:
        if row["id"] in previous and row["provenance"] != "plaud-web-translated-nl":
            assert not row["is_active"]
            assert row["instructions"] == previous[row["id"]]["instructions"]


def test_dutch_catalog_covers_interface_keys_and_preserves_placeholders():
    from localplaud.i18n import catalog, translator

    dutch = catalog("nl")
    assert catalog("zh-Hant-TW").keys() <= dutch.keys()
    assert translator("nl")("Saving…") != "Saving…"
    assert (
        translator("nl")("Uncatalogued provider diagnostic") == "Uncatalogued provider diagnostic"
    )
    for source, translation in dutch.items():
        assert translation.strip(), source
        assert Counter(re.findall(r"\{[^{}]+\}", source)) == Counter(
            re.findall(r"\{[^{}]+\}", translation)
        ), source


def test_relative_date_uses_dutch_words_and_workspace_timezone():
    from localplaud.api.ui import relative_datetime

    now = datetime(2026, 11, 7, 12, tzinfo=UTC)
    timestamp = int(datetime(2026, 11, 6, 23, 30, tzinfo=UTC).timestamp() * 1000)
    assert relative_datetime(timestamp, locale="nl", timezone="Europe/Amsterdam", now=now) == (
        "Vandaag om 00:30"
    )
