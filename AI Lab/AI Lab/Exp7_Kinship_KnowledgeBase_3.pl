can_cook(priya).
can_cook(jaya).
can_cook(tiyasha).
likes(priya, X) :- can_cook(X).
