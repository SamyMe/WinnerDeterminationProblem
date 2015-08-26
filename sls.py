from random import randint, random
import threading
import sys
import pickle
from time import time

nbB=0
nbI=0
bids=[]
wp=1
maxiter=500
bestProfit=0
bestSol=0
key=0

def randomSol():
	global bids
	global key
	global conflict
	global nbB

	sol=[]
	key=randomKey()
	dontstop=True

	while dontstop:
		maximum=max(key)
		if maximum==0:
			break

		best=key.index(maximum)
		for bid in conflict[best]:
			key[bid]=0

		for i in range(nbB):
			if key[i]==1:
				sol.append(i)

		key[best]=0
		sol.append(best)


	#print "Randomly Generated Sol"
	#print sol
	#print "-------------"
	return sol

def profit(a):
	global bids
	p=0
	for i in a:
		p+=bids[i]["price"]
	return p


def randomKey():
	global nbB
	a=[]
	for i in range(nbB):
		a.append(randint(0,100000))
	return a

def conflictGraph():
	global bids
	global nbB
	conflict={}
	for i in range(nbB):
		conflict[i]=[]
		for j in range(nbB):
			if (set(bids[i]["items"])-set(bids[j]["items"]) != set(bids[i]["items"])) and (i != j) and not (j in conflict[i]):
				conflict[i].append(j)
	return conflict

	
def sls(lock):
	global maxiter
	global bestSol
	global bestProfit
	global bids
	global wp
	global nbB
	closed=[]
	for iteration in range(maxiter):
		lock.acquire()
		sol=bestSol[:]
		lock.release()


		r = random()
		if r<wp:
			selected=sol[0]
			while selected in sol:
				selected=randint(0,nbB-1)


		if [selected, sol] in closed:
			continue
		else: 
			closed.append([selected, sol])

		if selected in sol:
			#print "BREAK"
			break


		key=[1]*nbB
		key[selected]=0

		for bid in conflict[selected]:
			if bid in sol:
				sol.remove(bid)

		sol.append(selected)


		for bid in sol:
			key[bid]=0
			for i in conflict[bid]:
				key[i]=0
		

		for i in range(nbB):
			if key[i]==1:
				sol.append(i)
				for j in conflict[i]:
					key[j]=0
	
		lock.acquire()
		if bestProfit<profit(sol):
			bestSol = sol[:]
			bestProfit=profit(sol)
		lock.release()




#------------------------------- MAIN SLS ---------------------------------
if __name__ == "__main__":
	
	try:
		nbB, nbI, conflict,bids = pickle.load(open(sys.argv[1]+".pkl554","r"))
	except Exception:
		with open(sys.argv[1]) as f:
	 		for line in enumerate(f):
				if line[0]==0:
					[nbI,nbB]=map(int,filter(None,line[1].strip('\n').split(" ")))
				else:		
					aline=line[1].strip('\n').split(" ")
					aline= filter(None,aline) # fastest
					c={}
					c["price"]=float(aline[0])
					c["items"]=map(int,aline[1:])
					bids.append(c)
	
		conflict=conflictGraph()

		pickle.dump((nbB,nbI,conflict,bids),open(sys.argv[1]+".pkl","w+"))

	bestResponse=0
	bestProfit=0
	n=50
	for i in range(5):
		start=time()
		bestSol=randomSol()
		bestProfit=profit(bestSol)

		lock = threading.Lock()
		#print "LOCK CREATED"


		agent=[0]*n

		for t in range(n):
			agent[t] = threading.Thread(target=sls, args=(lock,))

		for t in range(n):	
			agent[t].start()

		for t in range(n):	
			agent[t].join()

		end=time()-start

		#print "Best solution is:"
		print(bestSol)
		print profit(bestSol)

		if profit(bestSol)>bestProfit:
			bestResponse=bestSol
			bestProfit=profit(bestResponse)


		open("sls-solutions","a+").write(sys.argv[1]+" "+str(nbB)+" "+str(n)+" "+str(maxiter)+" "+str(bestProfit)+" "+str(end)+"\n")

#########################################################"
# CHECKING FOR CONFLICTS IN SOLUTION
#########################################################"
#	for i in bestSol:
#		for j in bestSol:
#			if j!=i and (j in conflict[i]):
#				#print "ERROR"
#				break
#	#print "Solution is fine"


