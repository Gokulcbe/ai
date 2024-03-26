% Define relationships
parent(john, lisa).
parent(john, kate).
parent(mary, lisa).
parent(mary, kate).
parent(lisa, anna).
parent(lisa, jack).

% Define rules for other relationships
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
child(X, Y) :- parent(Y, X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Define genders
male(john).
male(jack).
female(mary).
female(lisa).
female(kate).
female(anna).

% Query examples
% Is John the father of Anna?
% ?- father(john, anna).
% This will return false, as John is not the father of Anna.

% Who are the children of Mary?
% ?- child(X, mary).
% This will return X = lisa; X = kate.

% Who are the siblings of Lisa?
% ?- sibling(X, lisa).
% This will return X = kate; X = jack.

% Who are the parents of Anna?
% ?- parent(X, anna).
% This will return X = lisa.
