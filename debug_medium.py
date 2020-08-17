"""
tree-isomorphism-test - An algorithm for fast tree isomorphism test
Copyright (C) 2019,2020  Lluís Alemany Puig

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

