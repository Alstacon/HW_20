import pytest
from unittest.mock import MagicMock

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dir1 = Director(id=1, name='name1')
    dir2 = Director(id=2, name='name2')
    dir3 = Director(id=3, name='name3')

    director_dao.get_one = MagicMock(return_value=dir1)
    director_dao.get_all = MagicMock(return_value=[dir1, dir2, dir3])
    director_dao.create = MagicMock(return_value=dir1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None
        assert director.name == "name1"

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director = {
            "name": "name1"
        }

        assert self.director_service.create(director).name == director.get("name")


