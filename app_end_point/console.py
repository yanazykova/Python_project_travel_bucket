import pdb 

from models.country import Country 
import repositories.country_repository as country_repository

# city_repository.delete_all()
# country_repository.delete_all()

country_1 = Country("Brazil")
country_repository.save(country_1)

country_2 = Country("Australia")
country_repository.save(country_2)

country_3 = Country("Japan")
country_repository.save(country_3) 


