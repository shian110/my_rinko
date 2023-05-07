#const n=4.

%Define
color(1..n).

%Generate

%every vertex has just one color
{coloring(X,C):color(C)}=1 :- node(X).

%adjacent vertices have different color
:- coloring(X,C), coloring(Y,C), edge(X,Y), color(C).

#show coloring/2.
