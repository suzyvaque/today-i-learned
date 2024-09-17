# Using CTE

with recursive numbers as(
    select 20 as n
    union all
    select n-1 from numbers where n>0
)
select repeat('* ', n) as stars
from numbers;
