"""
tree-isomorphism-test - An algorithm for fast tree isomorphism test
Copyright (C) 2019  Lluís Alemany Puig

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: Lluís Alemany Puig (lluis.alemany.puig@gmail.com)
"""

import time
from random import sample, random
from tree_isomorphism_test import are_trees_isomorphic
import networkx as nx
from debug_aux import check_all_pairs

def run_large_tests(n):
	print("-----------------")
	print("-- Large tests --")
	print("-----------------")
	
	if n <= 16:
		print("Error: number of vertices must be larger than 16")
		return False
	
	print("Building list of non-isomorphic trees...")
	
	g = nx.nonisomorphic_trees(n)
	list_dif_trees = []
	
	print("    Sample some of the trees of %d vertices" % n)
	p = 0.3141592
	n_trees = 0
	for t in g:
		r = random()
		if r <= p:
			list_dif_trees.append(t)
			n_trees += 1
		if n_trees >= 15000:
			break
	
	print("Using %d non-isomorphic trees" % n_trees)
	
	list_some_trees = []
	for i in range(0,50):
		list_some_trees += sample(list_dif_trees, int(n_trees/5))
	
	n_trees = len(list_some_trees)
	n_pairs = (n_trees*(n_trees - 1))/2
	
	print("Checking all pairs...")
	check_all_pairs(list_some_trees)
	return True
