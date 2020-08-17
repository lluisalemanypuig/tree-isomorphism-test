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

import networkx as nx
import queue

"""
A free tree fT (by defintion undirected) can be
made directed by taking as root a node r in V(fT)
and by orienting its edges {u,v} into edges (u,v)
where
	level(v) = level(u) + 1,
and every edge {u,r} in E(fT) becomes (r,u) in
the new tree.

A free tree is denoted as fT.
A directed tree is denoted as dT.

The transformation consisting on directing the
edges of a free tree fT taking as root a node
r in V(fT) is denoted as:
	dT = direct(fT, r)
"""

"""
Returns
	dT = direct(fT, r)
"""
def __orient_tree(fT, r):
	n = fT.number_of_nodes()
	nvis = 0
	vis = {}
	for u in fT.nodes(): vis[u] = False
	
	dT = nx.DiGraph()
	
	Q = queue.Queue()
	vis[r] = True
	Q.put(r)
	while Q.qsize() > 0:
		current = Q.get()
		
		for u in fT.neighbors(current):
			if not vis [u]:
				vis[u] = True
				dT.add_edge(current, u)
				Q.put(u)
	return dT

"""
Retrieve the nodes of the tree dT level 'level'.
The nodes are stored in 'dlevel', a dictionary
that stores a list of nodes for each integer
representing the level:
    d[0] = [root of dT]
    d[1] = [nodes at level 1]
    d[2] = [nodes at level 2]
    ....
The function returns the amount of levels (minus 1).
"""
def __levelise(dT,u, dlevel,level):
	if level not in dlevel:
		dlevel[level] = [u]
	else:
		dlevel[level].append(u)
	
	# this is a leaf
	if dT.degree(u) == 1:
		return level
	
	max_lev = 0
	# this is an internal node
	for v in dT.neighbors(u):
		l = __levelise(dT,v, dlevel,level + 1)
		max_lev = max(l, max_lev)
	return max_lev

"""
Give names to the nodes in level 'level'
in dT. Names are stored in 'names'. The
nodes in level 'level' are given in
'nodes_level'.
"""
def __nominalise(dT,level,nodes_level,names):
	for u in nodes_level:
		if dT.out_degree(u) == 0:
			names[u] = '0'
		else:
			for child in dT.neighbors(u):
				if u not in names:
					names[u] = names[child]
				else:
					names[u] += names[child]
			
			# '11211' must be the same as '21111', '12111', ..
			names[u] = ''.join(sorted(names[u]))
	# ....
	# end of function

"""
dT1 and dT2 are directed trees rooted at
r1 and r2 respectively.
"""
def __trees_isomorphic(dT1,r1, dT2,r2):
	# classify vertices into levels
	dlevel1 = {}
	dlevel2 = {}
	
	ml1 = __levelise(dT1,r1, dlevel1,0)
	ml2 = __levelise(dT2,r2, dlevel2,0)
	
	# if number of levels is different, the trees
	# are not isomorphic
	if ml1 != ml2:
		return False
	
	# if there is a level with different number of
	# vertices then the trees are not isomorphic
	for l in range(0, ml1+1):
		if len(dlevel1[l]) != len(dlevel2[l]):
			return False
	
	names1 = {}
	names2 = {}
	
	# check that every level is equal by comparing canonical names
	for l in range(ml1,-1, -1):
		#print("-----------------")
		
		level_nodes1 = dlevel1[l]
		level_nodes2 = dlevel2[l]
		
		# obtain names of for every node in this level
		__nominalise(dT1, l, level_nodes1, names1)
		__nominalise(dT2, l, level_nodes2, names2)
		
		# canonicalise the names
		all_names_set = set([names1[u] for u in level_nodes1])
		all_names_set = all_names_set.union(set([names2[u] for u in level_nodes2]))
		unique_names = sorted(list(all_names_set))
		
		for u in level_nodes1:
			names1[u] = str(unique_names.index(names1[u]) + 1)
		for u in level_nodes2:
			names2[u] = str(unique_names.index(names2[u]) + 1)
		
		# check that names at this level are the same!
		names_at_level1 = sorted(list(set([names1[u] for u in level_nodes1])))
		names_at_level2 = sorted(list(set([names2[u] for u in level_nodes2])))
		if names_at_level1 != names_at_level2:
			return False
	
	return True

def are_trees_isomorphic(fT1, fT2):
	assert(nx.is_tree(fT1))
	assert(nx.is_tree(fT2))
	
	# retrieve amount of leaves. If they
	# do not agree the trees are not isomorphic
	nleaves1 = len(list(filter(lambda u: fT1.degree(u) == 1, fT1.nodes())))
	nleaves2 = len(list(filter(lambda u: fT2.degree(u) == 1, fT2.nodes())))
	if nleaves1 != nleaves2:
		return False
	
	# retrieve centers of trees
	c1 = nx.center(fT1)
	c2 = nx.center(fT2)
	
	# if there are different amount of centers in the trees
	# then they can't be isomorphic
	if len(c1) != len(c2):
		return False
	
	# check isomorphism using one of the centers...
	td1 = __orient_tree(fT1,c1[0])
	td2 = __orient_tree(fT2,c2[0])
	isomorph = __trees_isomorphic(td1,c1[0], td2,c2[0])
	
	# ... and if there is only one center
	if len(c1) == 1:
		return isomorph
	
	# ... or if there are two centers
	if not isomorph:
		del(td1) # free unused memory
		td1 = __orient_tree(fT1,c1[1])
		isomorph = __trees_isomorphic(td1,c1[1], td2,c2[0])
	return isomorph

