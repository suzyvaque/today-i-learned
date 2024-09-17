select n,
(case
when p is null then "Root"
when n not in (select p from bst where p is not null) then "Leaf"
else "Inner" end)
as n_type

from bst order by n;
