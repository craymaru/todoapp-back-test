from chalice import NotFoundError
import pytest

import app


class TestGetTodo:
    expected_dic = {
        "id": 201,
        "title": "ペットショップに行く",
        "memo": "ネコちゃんを見る",
        "priority": 1,
        "completed": False,
    }

    def test_get_todoでToDoが取得できる(self, monkeypatch):
        monkeypatch.setattr(
            "chalicelib.database.get_todo",
            lambda _: self.expected_dic
        )
        actual_dic = app.get_todo(201)
        assert actual_dic == self.expected_dic

    def test_get_todoでToDoが取得できない時にエラーを返す(self, monkeypatch):
        with pytest.raises(NotFoundError):
            monkeypatch.setattr(
                "chalicelib.database.get_todo",
                lambda _: False
            )
            app.get_todo(202)
