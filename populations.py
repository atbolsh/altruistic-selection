"""This is the python code. When run, it will prompt for some values, and then print the result after
several generations"""

import random

#The make series is just the method of creating the next generation.

def make_values():
	"""User prompt"""
	global freqA 
	global size
	global cheater_prob
	global altruist_prob
	global lower_group
	global upper_group
	global number
	global gen
	freqA = float(raw_input("starting dominant allele (non-cheater) frequency?"))
	size = int(raw_input("size of competing groups?"))
	lower_group = float(raw_input("probability of a cheater group surviving?"))
	upper_group = float(raw_input("probaility of an altruist group surviving?"))
	cheater_prob = float(raw_input("what is the probability that a cheater survives in a surviving group?"))
	altruist_prob = float(raw_input("what is the probability that an altruist survives in a surviving group?"))
	number = int(raw_input("how many groups?"))
	gen = int(raw_input("how many generations?"))

def make_allele():
	"""To guarantee random mating,
	the alleles are drawn at random
	from the general pool."""
	if random.random() < freqA :
		return "A"
	else:
		return "a"

def make_individual():
	"""An individual is two alleles"""
	return make_allele() + make_allele()

def make_all():
	"""Sets the jungle for the new generation;
	to simplify things, each generation is the
	same size. Also: not object oriented for
	optimization."""
	global life
	life = []
	for i in range(number):
		group = []
		for j in range(size):
			group.append(make_individual())
		life.append(group)
	
def test(group):
	"""Who in the group survives? Also: the ambiguity of
	the second line allows us to model Altruism as the
	recessive allele by means of clever responses (opposite)"""
	cheater_num = sum([1 for x in group if x == 'aa'])
	surv_prob = lower_group + (upper_group - lower_group)*(1 - (1.0/size)*cheater_num) #Each cheater hurts the same.
	if random.random() > surv_prob:
		return (0, 0)
	A = 0
	a = 0
	for ind in group:
		if ind == 'aa':
			if random.random() < cheater_prob:
				a += 2
		if (ind == 'Aa') or (ind == 'aA'):
			if random.random() < altruist_prob:
				A += 1
				a += 1
		if ind == 'AA':
			if random.random() < altruist_prob:
				A += 2
	return (A, a)

def run():
	"""Test each group; see the frequency change with time."""
	global gen
	if gen < 0:
		print "A: %f" % freqA
		return None
	make_all()
	A = 0
	a = 0
	for g in life:
		t = test(g)
		A += t[0]
		a += t[1]
	if A + a == 0:
		print "error: all died"
		return None
	global freqA
	freqA = float(A)/(A + a)
	gen -= 1
	return True

def main():
	make_values()
	while(run()):
		pass

main()


