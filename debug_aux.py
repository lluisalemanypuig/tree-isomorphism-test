import time
from tree_isomorphism_test import are_trees_isomorphic
import networkx as nx

def check_all_pairs(L):
	n_trees = len(L)
	n_pairs = (n_trees*(n_trees - 1))/2
	
	nx_time = 0
	my_time = 0
	
	true_tests = 0
	false_tests = 0
	
	proc_pairs=0
	for i in range(0, n_trees):
		for j in range(i+1, n_trees):
			proc_pairs += 1
			
			begin = time.time()
			if nx.faster_could_be_isomorphic(L[i], L[j]):
				nx_iso = nx.is_isomorphic(L[i], L[j])
			else:
				nx_iso = False
			end = time.time()
			nx_time += end - begin
			
			begin = time.time()
			my_iso = are_trees_isomorphic(L[i], L[j])
			end = time.time()
			my_time += end - begin
			
			assert(my_iso == nx_iso)
			
			if my_iso: true_tests += 1
			else: false_tests += 1
			
			if proc_pairs%1000 == 0:
				print("Processed: %.3f" % (proc_pairs/n_pairs*100), "%")
				print("    Time spent so far:")
				print("        NetworkX: %.3f seconds" % nx_time)
				print("        My test: %.3f seconds" % my_time)
				print("    Amount of tests where trees were")
				print("        Isomorphic:", true_tests)
				print("        Non-Isomorphic:", false_tests)
	
	print("")
	print("--------------------------")
	print("")

	print("All tests agreed")
	print("    Tests returning true:", true_tests)
	print("    Tests returning false:", false_tests)
	print("    Networkx takes:   ", nx_time, "s")
	print("    My function takes:", my_time, "s")

	print("")
	print("--------------------------")
	print("")
	return True
