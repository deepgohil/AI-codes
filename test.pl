female(nensi).
female(sushila).
male(deep).
male(suresh).
parent(suresh, deep).
parent(suresh, nensi).
parent(sushila, deep).
parent(sushila, nensi).
mother(X, Y):- parent(X, Y), female(X).
father(X, Y):- parent(X, Y), male(X).
haschild(X):- parent(X, _).
sister(X, Y):- parent(Z, X), parent(Z, Y), female(X), X\==Y.
brother(X, Y):- parent(Z, X), parent(Z, Y), male(X), X\==Y.
