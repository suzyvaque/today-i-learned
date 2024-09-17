select continent, floor(avg(population))

from (select country.continent as continent, city.population as population from country, city where country.code = city.countrycode) as aggregated

group by continent;
