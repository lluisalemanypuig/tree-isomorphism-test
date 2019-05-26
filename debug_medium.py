from random import sample, shuffle
import networkx as nx
from debug_aux import check_all_pairs

def __build_tree_list():
	L = []
	for i in range(5,17):
		print("    length", i)
		Li = list(nx.nonisomorphic_trees(i))
		if i <= 8:
			for k in range(0,3): L += Li
		else:
			for k in range(0,3): L += sample(Li, 3*i)
	return L

def run_medium_tests():
	print("------------------")
	print("-- Medium tests --")
	print("------------------")
	
	print("Building tree list...")
	L = __build_tree_list()
	print("    List contains", len(L), "trees")
	
	print("Shuffling...")
	shuffle(L)
	
	print("Checking all pairs...")
	return check_all_pairs(L)

