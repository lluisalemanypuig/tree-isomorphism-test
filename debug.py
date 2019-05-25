import time
from random import sample, random
from sys import argv
import networkx as nx
from tree_isomorphism_test import are_trees_isomorphic

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

########################################################################

if len(argv) < 2:
	print("I need the number of vertices")
	print("    python test.py 5")
	exit(1)

n = int(argv[1])
if n < 5:
	print("Error: number of vertices must be >= 5")
	exit(1)

g = nx.nonisomorphic_trees(n)
list_dif_trees = []

if n <= 20:
	print("Use all trees o %d vertices" % n)
	list_dif_trees = list(g)
	n_trees = len(list_dif_trees)
else:
	# sample SOME of the trees
	print("Sample some of the trees of %d vertices" % n)
	p = 0.3141592
	n_trees = 0
	for t in g:
		r = random()
		if r <= p:
			list_dif_trees.append(t)
			n_trees += 1
		if n_trees >= 10000:
			break

print("Using %d non-isomorphic trees" % n_trees)

list_some_trees = []
for i in range(0,50):
	list_some_trees += sample(list_dif_trees, int(n_trees/5))

n_trees = len(list_some_trees)
n_pairs = (n_trees*(n_trees - 1))/2

true_tests = 0
false_tests = 0
nx_time = 0
my_time = 0

proc_pairs=0
for i in range(0, n_trees):
	for j in range(i+1, n_trees):
		proc_pairs += 1
		
		begin = time.time()
		if nx.faster_could_be_isomorphic(list_some_trees[i], list_some_trees[j]):
			nx_iso = nx.is_isomorphic(list_some_trees[i], list_some_trees[j])
		else:
			nx_iso = False
		end = time.time()
		nx_time += end - begin
		
		begin = time.time()
		my_iso = are_trees_isomorphic(list_some_trees[i], list_some_trees[j])
		end = time.time()
		my_time += end - begin
		
		assert(my_iso == nx_iso)
		
		if my_iso: true_tests += 1
		else: false_tests += 1
		
		if j%500 == 0:
			print("Processed:", (proc_pairs/n_pairs*100))
			print("    Time spent so far:")
			print("        Networkx:", nx_time, "seconds")
			print("        My test:", my_time, "seconds")

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

print("Note! Most likely my test for trees")
print("is slower than Nx's test for graphs.")
print("HOWEVER! sit back and watch...")
print("")

###############################################
# TEST 1
print("Test 1:")
t1 = nx.Graph()
t2 = nx.Graph()
t1.add_edges_from([(1, 2), (2, 8), (2, 3), (4, 5), (5, 8), (5, 6), (5, 7), (8, 10), (8, 9), (8, 11), (11, 16), (11, 17), (11, 18), (11, 19), (11, 12), (11, 13), (11, 14), (11, 15)])
t2.add_edges_from([(1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 13), (10, 13), (11, 13), (12, 13), (13, 16), (14, 16), (15, 16), (16, 19), (17, 19), (18, 19)])
small_tests(t1, t2)

"""
# This test is not impressive...
print("Test 2:")
t1 = nx.Graph()
t2 = nx.Graph()
t1.add_edges_from([(1, 2), (1, 3), (3, 4), (3, 5), (5, 8), (5, 6), (5, 7), (8, 9), (8, 10), (8, 11)])
t2.add_edges_from([(1, 10), (2, 10), (2, 3), (4, 5), (5, 8), (5, 6), (5, 7), (8, 9), (8, 10), (10, 11)])
small_tests(t1, t2)
"""

print("Test 3:")
t1 = nx.Graph()
t2 = nx.Graph()
t1.add_edges_from([(1, 18), (2, 4), (3, 4), (4, 18), (5, 6), (6, 8), (6, 18), (6, 7), (9, 18), (9, 10), (11, 18), (12, 18), (13, 18), (14, 18), (15, 18), (16, 18), (17, 18)])
t2.add_edges_from([(1, 3), (2, 3), (3, 12), (3, 4), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 13), (12, 14), (12, 15), (15, 16), (15, 17), (17, 18)])
small_tests(t1, t2)

"""
# This test is not impressive...
print("Test 4:")
t1 = nx.Graph()
t2 = nx.Graph()
t1.add_edges_from([(1, 10), (2, 3), (3, 4), (3, 10), (5, 6), (5, 7), (7, 8), (7, 9), (7, 10), (10, 11)])
t2.add_edges_from([(1, 3), (2, 3), (3, 4), (3, 5), (5, 10), (5, 6), (5, 7), (8, 9), (8, 10), (10, 11)])
small_tests(t1, t2)
"""
