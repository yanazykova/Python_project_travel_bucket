from flask import Blueprint, Flask, redirect, render_template, request 

from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint 
("countries", __name__) 

# INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)


