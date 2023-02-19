from dz_18.dao.movie import MovieDAO
from dz_18.dao.genre import GenreDAO
from dz_18.dao.director import DirectorDAO
from dz_18.service.movie import MovieService
from dz_18.service.genre import GenreService
from dz_18.service.director import DirectorService
from dz_18.setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)
