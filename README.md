
This is an an agent-based (thread-based) implementation of a solution to the winner determination problem (WDP) in combinatorial auctions. It is based on the methode proposed in [2]. 
It was tested with [StacklessPython](http://www.stackless.com/) wich gave better results then the conventional CPython.

###Definition:
As explained in [1] :
**"The combinatorial auction is a type of auctions in which agents (bidders) can place bids on combinations of items (goods), called packages, rather than just individual items.
The combinatorial auctions have been used in solving resource and task allocation problems in multi-agents system [7, 23]. They play an important role in various domains such as economics, game theory and the sale of spectrum licenses in America’s Federal Communications Commissions (FCC) auctions."**

###Execution:
The code is executed as follows:
```bash
python sls.py benchmarkfile
```
One can find some examples of benchmark files in the **benchmarks** folder.

###Ref: 
- [1] X.-S. Yang (Ed.): Artif. Intell., Evol. Comput. and Metaheuristics, SCI 427, pp. 775–791.
c Springer-Verlag Berlin Heidelberg 2013
springerlink.com

- [2] Dalila Boughaci, Belaid Benhamou et Habiba Drias : Une recherche locale stochastique pour le problème de la détermination du gagnant dans les enchères combinatoires. Gilles Trombettoni. JFPC 2008- Quatrièmes Journées Francophones de Programmation par Contraintes, Jun 2008, Nantes, France. pp.59-68. https://hal.inria.fr/inria-00290789/document

