# Tree isomorphism test

An isomorphism test in Python3 for trees using NetworkX.
This is an implementation of the algorithm described in
[these](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf) slides (last accessed May 25th, 2019).
The names Aho, Hopcroft and Ullman are mentioned, but I could not find a proper reference.

## Implementation

In [this](https://github.com/lluisalemanypuig/tree-isomorphism-test/edit/master/tree_isomorphism_test.py) file.
In order to use it, the file could be imported with

        from tree_isomorphism_test import are_trees_isomorphic

The function _are_trees_isomorphic_ returns True (False) when the two trees passed as parameters are Isomorphic
(Non-isomorphic).

## Debugging

In [this](https://github.com/lluisalemanypuig/tree-isomorphism-test/edit/master/debug.py) file one will find a
small piece of code used to debug the test. It also measures the execution time and compares it to Networkx's.

My test is slower for most cases, but at the end of this file there are two tests for which Networkx takes
9 seconds in one test and 20 seconds in the other. My function takes 0.0005 seconds in both (tests were executed
and execution times were measured in the same computer).
