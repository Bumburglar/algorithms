import random
import string

numTries=0
best=0
bestattempt=''
def generate():
	gen=""
	poss=string.ascii_lowercase+' '
	for x in range(0,27):
		gen += random.choice(poss)
	return gen

def score(genstring):
	score=0
	compstring='methinks it is like a weasel'
	for i in range(0,len(genstring)):
		if compstring[i] == genstring[i]:
			score += 1
	return score
	
def monkey():
	global numTries
	global best
	global bestattempt
	found = False
	while found == False:
		genstring=generate()
		tot=score(genstring)
		if tot > best:
			best = tot
			bestattempt=genstring
		if numTries % 1000 == 0:
			print(genstring + "\n" , best)
		if best== 26:
			print(genstring)
			found = True	
