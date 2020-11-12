from chalice import NotFoundError
import pytest

import app


class TestGetAllTodos:

    expected_list = [
        {
            "completed": True,
            "id": "L5",
            "memo": "TONOSAKI",
            "priority": 3.0,
            "title": "夢の舞台へ駆け上がる"
        },
        {
            "completed": True,
            "id": "L6",
            "memo": "GENDA",
            "priority": 2.0,
            "title": "今ここで魅せる"
        },
        {
            "completed": False,
            "id": "L8",
            "memo": "KANEKO",
            "priority": 1.0,
            "title": "その瞬間を掴む"
        },
        {
            "completed": False,
            "id": "a5d8f7b0a8314c6190979832349cadcb",
            "memo": "123",
            "priority": "1",
            "title": "テスト"
        },
        {
            "completed": False,
            "id": "60558c27024e4c5ab8bae6d17f5a95b5",
            "memo": "FOOD",
            "priority": 3.0,
            "title": "ごはんを買う"
        },
        {
            "completed": False,
            "id": "bc33651f3c1843ebba770ec269e11c75",
            "memo": "CHANCE4",
            "priority": "3",
            "title": "熱い獅子の魂を魅せる"
        },
        {
            "completed": False,
            "id": "3a3aa5bf58384f599ed8253784559494",
            "memo": "CHANCE4",
            "priority": "3",
            "title": "熱い獅子の魂を魅せる2"
        }
    ]

    def test_get_all_todosでToDoを取得できる(self, monkeypatch):

        monkeypatch.setattr(
            "chalicelib.database.get_all_todos",
            lambda: self.expected_list
        )
        actual_dic = app.get_all_todos()
        assert actual_dic == self.expected_list
