from flask import Blueprint, Flask, redirect, render_template, request

from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities=cities)

# SHOW??

# NEW

