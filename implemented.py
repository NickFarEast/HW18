from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.service.genre import GenreService
from setup_db import db
from app.service.director import DirectorService


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)


genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)