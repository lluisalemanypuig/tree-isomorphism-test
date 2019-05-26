# Tree isomorphism test

An isomorphism test in Python3 for trees using NetworkX. This is an implementation of the algorithm described in
[these](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf) slides (last accessed May 25th, 2019).
The names _Aho_, _Hopcroft_ and _Ullman_ are mentioned, but I could not find a proper reference to their
algorithm.

## Implementation

In [this](https://github.com/lluisalemanypuig/tree-isomorphism-test/blob/master/tree_isomorphism_test.py?ts=4) file.
In order to use it, the file can be imported with

        from tree_isomorphism_test import are_trees_isomorphic

The function _are_trees_isomorphic_ returns True (False) when the two trees passed as parameters are Isomorphic
(Non-isomorphic).

## Debugging

In [this](https://github.com/lluisalemanypuig/tree-isomorphism-test/blob/master/debug.py?ts=4) file one will find a
small piece of code used to debug the isomorphism test. It also measures the execution time and compares it to Networkx's.

There are three types of tests. The first, the small tests, shows that NetworkX needs 9 seconds and 20 seconds
to determine that two trees are not isomorphic, whereas my function takes about 0.0005 seconds. The other tests,
medium and large, are designed to strees the correctness of my isomorphism test.

The last two tests show that my function for tree isomorphism is slower than NetworkX's function for graph isomorphism
when run on the same pairs of trees. This _might_ be due to the fact that the trees used for testing are generated
by NetworkX, which might label the vertices and order the edges within the internal structure of NetworkX's graph data
structure in a way that the library itself can make use of to improve the efficiency of the algorithms it implements.

In order to run the tests
