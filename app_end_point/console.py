import pdb 

from models.city import City
import repositories.city_repository as city_repository

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

city_1 = City("Rio de Janeiro", country_1)
city_repository.save(city_1)

city_2 = City("Sidney", country_2)
city_repository.save(city_2)

city_3 = City("Tokyo", country_3)
city_repository.save(city_3)

pdb.set_trace()
