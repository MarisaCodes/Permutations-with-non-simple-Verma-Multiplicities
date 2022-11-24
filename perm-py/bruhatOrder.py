import pprint
import numpy as np
from pkg.permutations import get_sym_n
from pkg.smlnbr import small_neighbors
from sympy.combinatorics import Permutation


def zero_pad_sym_n(lol):
    for lis in lol:
        lis.insert(0, 0)
    return lol


def get_bruhat_order(sym_n):
    sorted_sym_n_by_inv = {}
    for lis in sym_n:
        perm = Permutation(lis)
        inv = perm.inversions()
        lis.append(len(small_neighbors(lis)))
        if str(inv) in sorted_sym_n_by_inv:
            sorted_sym_n_by_inv = {**sorted_sym_n_by_inv,
                                   str(inv): [*sorted_sym_n_by_inv[str(inv)], lis]}
        else:
            sorted_sym_n_by_inv[str(inv)] = [lis]

    return sorted_sym_n_by_inv


def get_false_permutations(sorted_sym_n, max_small_neighbors):
    false_perms_dict = []
    for i in sorted_sym_n:
        for j, lis in enumerate(sorted_sym_n[i]):
            if lis[-1] >= max_small_neighbors:
                temp = lis[:]
                temp.pop()
                perm = Permutation(temp)
                false_perms_dict.append([lis, perm.cyclic_form])
    return false_perms_dict


# sym_n = zero_pad_sym_n(get_sym_n([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# b_order = get_bruhat_order(sym_n)

# pprint.pprint(get_false_permutations(b_order, 8))
# get_bruhat_order(zero_pad_sym_n(get_sym_n([1, 2, 3, 4, 5, 6])))

sym_5 = zero_pad_sym_n(get_sym_n([1, 2, 3, 4, 5]))
b_order = get_bruhat_order(sym_5)

# pprint.pprint(len(get_false_permutations(b_order, 5)))
