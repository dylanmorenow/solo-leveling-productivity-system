import json
import copy
import builtins
import pytest

import project as sl


@pytest.fixture
def empty_save(monkeypatch):
    monkeypatch.setattr(sl, "save_data", lambda *_, **__: None)


@pytest.fixture
def new_player_dict():
    return {"id": {}}


@pytest.fixture
def existing_player_dict():
    return {
        "id": {
            "Jin-Woo": {
                "level": 7,
                "exp": 50,
                "rank": "D",
                "active_quests": {},
                "completed_quests": 3,
            }
        }
    }


class _FakeInput:
    def __init__(self, answers):
        self._iter = iter(answers)

    def __call__(self, _prompt=""):
        try:
            return next(self._iter)
        except StopIteration:
            raise AssertionError("input() called too many times")


def test_load_data(tmp_path):
    file = tmp_path / "pemain.json"
    file.write_text(json.dumps({"id": {"A": {}}}))

    data = sl.load_data(file)
    assert data == {"id": {"A": {}}}


def test_check_player_existing(existing_player_dict, empty_save):
    player = sl.check_player(existing_player_dict, "Jin-Woo")
    assert player["level"] == 7
    assert len(existing_player_dict["id"]) == 1


def test_check_player_new(new_player_dict, empty_save):
    player = sl.check_player(new_player_dict, "Igris")
    assert player == {
        "level": 1,
        "exp": 0,
        "rank": "E",
        "active_quests": {},
        "completed_quests": 0,
    }
    assert "Igris" in new_player_dict["id"]


def test_check_stats():
    player = {
        "level": 4,
        "exp": 80,
        "rank": "D",
        "active_quests": {"Run 5 km": 30},
        "completed_quests": 7,
    }
    stats = sl.check_stats(player, "Beru")
    assert (
        stats
        == "Player: Beru | Rank: D | Level: 4 | EXP: 80/400\nActive Quests: 1 Completed Quests: 7"
    )


def test_add_quest(monkeypatch, empty_save):
    player = {
        "level": 1,
        "exp": 0,
        "rank": "E",
        "active_quests": {},
        "completed_quests": 0,
    }
    data = {"id": {"Solo": copy.deepcopy(player)}}

    fake_input = _FakeInput(["Belajar pytest", "40"])
    monkeypatch.setattr(builtins, "input", fake_input)

    sl.add_quest(player, data, "Solo")

    assert "Belajar pytest" in player["active_quests"]
    assert player["active_quests"]["Belajar pytest"] == 40
    assert data["id"]["Solo"]["active_quests"] == player["active_quests"]


def test_complete_quest(monkeypatch, empty_save):
    player = {
        "level": 1,
        "exp": 0,
        "rank": "E",
        "active_quests": {"Push-up 20×": 120},
        "completed_quests": 0,
    }
    data = {"id": {"Solo": copy.deepcopy(player)}}

    fake_input = _FakeInput(["1"])
    monkeypatch.setattr(builtins, "input", fake_input)

    monkeypatch.setattr(sl, "check_level_up", lambda *_, **__: None)

    sl.complete_quest(player, data, "Solo")

    assert player["active_quests"] == {}
    assert player["exp"] == 120
    assert player["completed_quests"] == 1
    assert data["id"]["Solo"]["exp"] == 120


