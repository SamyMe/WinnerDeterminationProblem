###Presentation:
This is an agent-based (thread-based) implementation of a solution to the winner determination problem (WDP) in combinatorial auctions. It is based on the methode proposed in [2]. 
It was tested with [StacklessPython](http://www.stackless.com/) wich gave better results then the conventional CPython.

***

###Definition:
####Winner Determination Problem:
As explained in [1] :
*"The combinatorial auction is a type of auctions in which agents (bidders) can place bids on combinations of items (goods), called packages, rather than just individual items.
The combinatorial auctions have been used in solving resource and task allocation problems in multi-agents system [7, 23]. They play an important role in various domains such as economics, game theory and the sale of spectrum licenses in America’s Federal Communications Commissions (FCC) auctions."*

####Solution:
Let the "B" be the initial set of bids

A solution is defined as the largest set of bids {bi} not in conflict. In other words a bid "b" is in "S" <=>
(for any "bi" in "S"  "b" is not in conflict with "bi")  AND  (for any “bi” not in “S”, there is a “bj” in “S” in conflict with it)

####Neighbor:
A neibore "N" of a solution "S" is defined as follows:
1. N = S
2. Let "E" be a random element which is NOT in "S" (E is in conflict with a bid in "S")
3. Remove from "N" all bids which are in conflict with "E"
4. Append "E" to "N"
5. Add all bids wich are not in "N" and are in conflict with no element of "N"


#####Example:
*Bids* =

b1:   1 2 3

b2:   5 6

b3:  1 5 7

b4:   4 5

B5:   6 8

*Some solutions*: 

S1: b1 b2 

S2: b3 b4 b5

*Neighbors*:

(Let **S1'** be a neighbor of S1)

1. **S1'** *= S1 = (b1 b2)*
2. *E = b5*
3. b2 is in conflict with b5 so: *S1' = S1' - b2 = (b1)*
4. *S1' = S1' + E = (b1 b5)*
5. b4 Is in conflict with neither b1 nor b5 so:  *S1' = S1' + b4*

***

###Algorithme:
The algorithme proposed is as follows : 

**Input**: An instence of WDP;
**output**: a solution S;

1. Creating conflict graph;
2. iter=0
3. Generating a random solution
4. launch *N* agent

- Each agent starts with a random solution, writes it in a *Blackboard* if it's better then the solution already there (or if there is no solution written) otherwise, he takes that better solution found in the *Board*.
- Then, he goes to a random neighbor (if this later is not *Tabou*).

***

###Execution:
The code is executed as follows:
```bash
python sls.py benchmarkfile
```
One can find some examples of benchmark files in the **benchmarks** folder.

***

###Ref: 
- [1] X.-S. Yang (Ed.): Artif. Intell., Evol. Comput. and Metaheuristics, SCI 427, pp. 775–791.
c Springer-Verlag Berlin Heidelberg 2013 springerlink.com

- [2] Dalila Boughaci, Belaid Benhamou et Habiba Drias : Une recherche locale stochastique pour le problème de la détermination du gagnant dans les enchères combinatoires. Gilles Trombettoni. JFPC 2008- Quatrièmes Journées Francophones de Programmation par Contraintes, Jun 2008, Nantes, France. pp.59-68. https://hal.inria.fr/inria-00290789/document

***

###License:
This is published under GNU GPL Lisence.
For more informations about the terms: https://www.gnu.org/licenses/gpl.html

![Image Alt](https://www.gnu.org/graphics/gplv3-127x51.png)

