from flask import Blueprint
#instanciate Blueprint class, 2 params are bluprint name and the package/module located
main = Blueprint('main', __name__)

from . import views, errors, DBConnectionConfig, Similarity, teamUtil, wikiUtil, TeamStanding