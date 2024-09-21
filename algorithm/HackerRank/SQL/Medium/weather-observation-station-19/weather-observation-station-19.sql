# Solution 1

select round(sqrt(power(st_b.b - st_a.a, 2) + power(st_d.d - st_c.c, 2)), 4)
from
(
(select min(lat_n) as a from station) as st_a,
(select max(lat_n) as b from station) as st_b,
(select min(long_w) as c from station) as st_c,
(select max(long_w) as d from station) as st_d
);



/*
# Solution 2

select round(sqrt(
power((select max(lat_n) as a from station) - (select min(lat_n) as a from station), 2) +
power((select max(long_w) as a from station) - (select min(long_w) as a from station), 2)
), 4);
*/
