# Tree isomorphism test

An isomorphism test in Python3 for trees using NetworkX. This is an implementation of the algorithm described in [these](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf) slides (last accessed May 25th, 2019). The algorithm is based on Aho, Hopcroft and Ullman's algorithm published in their book _The Design and Analysis of Computer Algorithms_ 1974. The complete bibliographic reference is the following:

	@book{Aho1974a,
		author = {Aho, A. V. and Hopcroft, J. E. and Ullman, J. D.},
		title = {The Design and Analysis of Computer Algorithms},
		series = {Addison-Wesley series in computer science and information processing},
		year = {1974},
		isbn = {9780201000290},
		edition = {1st},
		publisher = {Addison-Wesley Publishing Company},
		address = {Michigan University},
	}

## Implementation

In [this](https://github.com/lluisalemanypuig/tree-isomorphism-test/blob/master/tree_isomorphism_test.py?ts=4) file.
In order to use it, the file can be imported with

        from tree_isomorphism_test import are_trees_isomorphic

The function _are_trees_isomorphic_ returns True (False) when the two trees passed as parameters are Isomorphic (Non-isomorphic).

## Running

In [this](https://github.com/lluisalemanypuig/tree-isomorphism-test/blob/master/debug.py?ts=4) file you will find a small piece of code used to debug the isomorphism test. It also measures the execution time and compares it to Networkx's.

There are three types of tests. The first, the small tests, shows that NetworkX needs 9 seconds and 20 seconds to determine that two trees are not isomorphic, whereas my function takes about 0.0005 seconds (measured on May 2019). The other tests, medium and large, are designed to stress the correctness of my implementation.

The last two tests show that my implementation for tree isomorphism is slower than NetworkX's function for graph isomorphism when run on the same pairs of trees.

In order to run the tests issue 

	python3 debug.py --small-tests
	python3 debug.py --medium-tests
	python3 debug.py --large-tests 20
