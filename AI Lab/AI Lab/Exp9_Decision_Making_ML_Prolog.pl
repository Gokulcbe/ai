male(kasthuriraja).
male(dhanush).
male(selva).
male(yatra).
male(linga).
female(vijaya).
female(aishwarya).
female(geethanjali).
female(anjali).
parent(kasthuriraja,dhanush).
parent(vijaya,dhanush).
parent(kasthuriraja,selva).
parent(vijaya,selva).
parent(dhanush,linga).
parent(aishwarya,linga).
parent(dhanush,yatra).
parent(aishwarya,yatra).
parent(selva,anjali).
parent(geethanjali,anjali).
father(F,X):-male(F),parent(F,X).
mother(M,X):-female(M),parent(M,X).
sibling(X,Y):-father(Z,X),father(Z,Y),X\=Y.
child(C,P):-parent(P,C).
brother(B,X):-male(B),sibling(B,X).
sister(S,X):-female(S),sibling(S,X).
daughter(D,X):-female(D),parent(X,D).
son(S,X):-male(S),parent(X,S).
spouse(X,Y):-child(Z,X),child(Z,Y).
wife(W,X):-female(W),male(X),spouse(W,X).
husband(H,X):-male(H),female(X),spouse(H,X).
grandfather(GP,GC):-male(GP),parent(GP,X),parent(X,GC).
grandmother(GP,GC):-female(GP),parent(GP,X),parent(X,GC).
grandchild(GC,GP):-grandmother(GP,GC).
grandchild(GC,GP):-grandfather(GP,GC).
aunt(A,X):-female(A),father(Z,X),brother(Z,A).
aunt(A,X):-female(A),mother(Z,X),sister(Z,A).
uncle(U,X):-male(U),father(Z,X),brother(Z,U).
uncle(U,X):-male(U),mother(Z,X),sister(Z,U).
uncle(U,X):-male(U),father(Z,X),sister(S,Z),husband(U,S).
cousin(X,Y):-parent(Z,X),parent(P,Y),sibling(Z,P).