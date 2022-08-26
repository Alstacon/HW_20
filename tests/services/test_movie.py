import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1, title='title1', description='desc1', trailer='tr1', year=1900, rating='rat1', genre_id=1,
                   genre='gen1', director_id=1, director='dir1')
    movie2 = Movie(id=2, title='title2', description='desc2', trailer='tr2', year=2000, rating='rat2', genre_id=2,
                   genre='gen2', director_id=2, director='dir2')

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.create = MagicMock(return_value=movie1)
    movie_dao.partially_update = MagicMock()
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None
        assert movie.title == "title1"

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie = {
            "title": "title1",
            "description": "desc1",
            "trailer": "tr1",
            "year": "1900",
            "rating": "rat1",
            "genre_id": 1,
            "genre": "gen1",
            "director_id": 1,
            "director": "dir1"
        }

        assert self.movie_service.create(movie).title == movie.get("title")
