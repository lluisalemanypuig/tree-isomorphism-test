from sys import argv
from debug_small import run_small_tests
from debug_medium import run_medium_tests
from debug_large import run_large_tests

def print_help():
	print("Debugger of tree isomorphism test")
	print("---------------------------------")
	print("This debugger offers three types of tests:")
	print("    --small-tests")
	print("        Runs a few small tests where NetworkX is a lot slower")
	print("        than my test. This test does not need extra arguments.")
	print("        Note that this is not enough to show that my implementation")
	print("        has no bugs.")
	print("")
	print("    --medium-tests")
	print("        Samples some non-isomorphic trees of several lengths,")
	print("        puts them all in the same list, shuffles it and checks")
	print("        for every pair whether the two trees are isomorphic or")
	print("        not. More precisely, let L_i be a list of  non-isomorphic")
	print("        trees of i vertices each. Sample without replacement")
	print("        3*i trees 10 times, and put each sample into a list L.")
	print("        Do this process for i=5..16. Then, check isomorphism")
	print("        for every unique pair of trees in L. This test does")
	print("        not need extra parameters.")
	print("")
	print("    --large-tests n")
	print("        Samples 15000 trees from the list of all non-isomorphic")
	print("        trees of 'n' vertices. Checks isomorphism for every pair")
	print("        of trees in the list.")
	print("        The number of vertices must be larget than 16: n >= 17")

if len(argv) < 2:
	print("Use")
	print("    python debug.py help")
	print("to see the usage")
	exit(1)

if len(argv) == 2:
	if argv[1] == "help":
		print_help()
		exit(0)
	
	if argv[1] == "--large-tests":
		print("Error: lacking amount of vertices.")
		print("Use")
		print("    python debug.py help")
		print("to see the usage")
		exit(1)
	
	# Either small or medium test
	if argv[1] not in {"--small-tests", "--medium-tests"}:
		print("Error: wrong parameter value '%s'" % argv[1])
		print("Use")
		print("    python debug.py help")
		print("to see the usage")
		exit(1)
	
	small = argv[1] == "--small-test"
	if small:
		run_small_tests()
	else:
		run_medium_tests()

elif len(argv) == 3:
	# large tests
	run_large_tests(int(argv[2]))
	
else:
	# wrong amount of parameters
	print("Error: wrong amount of parameters")
	print("Use")
	print("    python debug.py help")
	print("to see the usage")
	exit(1)



