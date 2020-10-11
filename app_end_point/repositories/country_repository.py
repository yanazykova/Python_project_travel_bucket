from db.run_sql import run_sql 
from models.country import Country 


def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values) 
    id = results[0]['id']
    country.id = id

# Creating a function which will allow to select 
# all the countries saved in the database and pass them to the index template:
def select_all():
    # Let's give a variable "countries" a value of an empty list:
    countries = []
    # Let's assign a variable "sql" to the sql command
    # which will select all countries from the countries table:
    sql = "SELECT * FROM countries"
    # Variable "results" is assigned to the result of calling the 
    # function "def run_sql" which was defined in the run_sql.py file, 
    # in the brackets we're passing in the argument "sql" which is the 
    # variable from the preseding assignment:
    results = run_sql(sql)
    # now we're iterating over the dictionary which was returned 
    # as the result of the invoking the above "run_sql" function:
    for result in results:
    # the resulted dictionary would contain a key "country" for which we're 
    # going to create an instance of a Country class with attributes "name" and "id":
        country = Country(result ["name"], result["id"])
    # each returned country is now going to be appended to the forementioned 
    # "countries" list:
        countries.append((country))
    # and all the countries are going to be returned as a now completed list:
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


