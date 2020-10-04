from db.run_sql import run_sql 
from models.country import Country 


def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values) 
    id = results[0]['id']
    country.id = id

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for result in results:
        country = Country(result ["name"], result["id"])
        countries.append((country))
    return countries 

def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = Country(result ["name"], result["id"])
    return country 

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET name = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)


