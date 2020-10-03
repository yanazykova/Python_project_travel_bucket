from db.run_sql import run_sql 
from models.country import Country 

def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values) 
    id = results[0]['id']
    country.id = id

