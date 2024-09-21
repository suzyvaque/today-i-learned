(select city, char_length(city) from station
where char_length(city) in
(select min(char_length(city)) from station)
order by city asc limit 1)

union all

(select city, char_length(city) from station
where char_length(city) in
(select max(char_length(city)) from station)
order by city asc limit 1);
