from sympy.combinatorics import Permutation

p_1 = Permutation([0, 5, 3, 4, 2, 1])
print(p_1.cyclic_form)
print(p_1.inversions())
