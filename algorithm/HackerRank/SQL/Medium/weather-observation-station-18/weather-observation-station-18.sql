select round(abs(st_c.c-st_a.a) + abs(st_d.d-st_b.b), 4)
from
((select min(lat_n) as a from station) as st_a,
(select max(lat_n) as c from station) as st_c,
(select min(long_w) as b from station) as st_b,
(select max(long_w) as d from station) as st_d)
