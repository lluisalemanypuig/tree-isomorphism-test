import time
from tree_isomorphism_test import are_trees_isomorphic
import networkx as nx

def are_iso(b):
	if b: return "Isomorphic"
	return "Non-isomorphic"

def small_tests(t1, t2):
	print("    Checking isomorphism with nx...")
	begin = time.time()
	nx_iso = nx.is_isomorphic(t1,t2)
	end = time.time()
	print("        in", end - begin, "seconds")
	print("        Result:", are_iso(nx_iso))
	
	print("    Checking with my function...")
	begin = time.time()
	my_iso = are_trees_isomorphic(t1,t2)
	end = time.time()
	print("        in", end - begin, "seconds")
	print("        Result:", are_iso(my_iso))
	print("")
	
	assert(my_iso == nx_iso)

def run_small_tests():
	print("-----------------")
	print("-- Small tests --")
	print("-----------------")
	
	###############################################
	# TEST 1
	print("Test 1:")
	t1 = nx.Graph()
	t2 = nx.Graph()
	t1.add_edges_from([(1, 2), (2, 8), (2, 3), (4, 5), (5, 8), (5, 6), (5, 7), (8, 10), (8, 9), (8, 11), (11, 16), (11, 17), (11, 18), (11, 19), (11, 12), (11, 13), (11, 14), (11, 15)])
	t2.add_edges_from([(1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 13), (10, 13), (11, 13), (12, 13), (13, 16), (14, 16), (15, 16), (16, 19), (17, 19), (18, 19)])
	small_tests(t1, t2)
	
	###############################################
	# TEST 2
	"""
	# This test is not impressive...
	print("Test 2:")
	t1 = nx.Graph()
	t2 = nx.Graph()
	t1.add_edges_from([(1, 2), (1, 3), (3, 4), (3, 5), (5, 8), (5, 6), (5, 7), (8, 9), (8, 10), (8, 11)])
	t2.add_edges_from([(1, 10), (2, 10), (2, 3), (4, 5), (5, 8), (5, 6), (5, 7), (8, 9), (8, 10), (10, 11)])
	small_tests(t1, t2)
	"""
	
	###############################################
	# TEST 3
	print("Test 3:")
	t1 = nx.Graph()
	t2 = nx.Graph()
	t1.add_edges_from([(1, 18), (2, 4), (3, 4), (4, 18), (5, 6), (6, 8), (6, 18), (6, 7), (9, 18), (9, 10), (11, 18), (12, 18), (13, 18), (14, 18), (15, 18), (16, 18), (17, 18)])
	t2.add_edges_from([(1, 3), (2, 3), (3, 12), (3, 4), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 13), (12, 14), (12, 15), (15, 16), (15, 17), (17, 18)])
	small_tests(t1, t2)
	
	###############################################
	# TEST 4
	"""
	# This test is not impressive...
	print("Test 4:")
	t1 = nx.Graph()
	t2 = nx.Graph()
	t1.add_edges_from([(1, 10), (2, 3), (3, 4), (3, 10), (5, 6), (5, 7), (7, 8), (7, 9), (7, 10), (10, 11)])
	t2.add_edges_from([(1, 3), (2, 3), (3, 4), (3, 5), (5, 10), (5, 6), (5, 7), (8, 9), (8, 10), (10, 11)])
	small_tests(t1, t2)
	"""
	
	return True
