from sympy.combinatorics import Permutation
from pprint import pprint
import numpy as np


def get_sml_nbrs(list_type_perm: list) -> list:
    perm = list_to_perm(list_type_perm)
    inv_vec = perm.inversion_vector()
    # list to store indices (tuples: (i,j)) of elements in perm that can make valid swaps
    smlnbrs = []
    for i, num_invs in enumerate(perm.inversion_vector()):
        count_to_stop = 0
        for j in range(i+1, len(list_type_perm)):
            if count_to_stop == num_invs:
                break
            if list_type_perm[j] < list_type_perm[i]:
                count_to_stop += 1
                check = list(filter(
                    lambda x: x < list_type_perm[i] and x > list_type_perm[j], list_type_perm[i+1:j]))
                if len(check) != 0:
                    continue
                else:
                    tmp_list_type_perm = list_type_perm[:]
                    tmp = tmp_list_type_perm[i]
                    tmp_list_type_perm[i] = tmp_list_type_perm[j]
                    tmp_list_type_perm[j] = tmp
                    smlnbrs.append(tmp_list_type_perm)

    return smlnbrs

# small neighbors structure: e.g. {"1432": [[1432], [1423, 1342], [1243, 1324], [1234]]}


def perm_to_list(perm: Permutation):
    return list(np.array(list(perm))+1)


def list_to_perm(list_type_perm: list):
    return Permutation(list(np.array(list_type_perm)-1))


def smlnbr_pattern(smlnbrs: list[list[list]]):
    if len(smlnbrs) != 1:
        print("please pass exactly only 1 permutation in List(List(Permutation)) form")
        return
    # list of lists, each containing permutations that are
    # small neighbors of argument `perm` at a given level
    pattern = [1]
    smlnbrs_copy = smlnbrs[:]
    d = {f'{smlnbrs[0][0]}': smlnbrs_copy}

    def rec_gen_pattern(last_idx: int = 0):
        if smlnbrs_copy[len(smlnbrs_copy) - 1][0] == list(range(1, 1+len(smlnbrs_copy[0][0]))):
            return

        next_lvl_smlnbrs = []
        for list_type_perm in smlnbrs_copy[last_idx]:
            all_next_lvl_smlbrs = get_sml_nbrs(list_type_perm)
            unique_next_lvl_smlnbrs = list(filter(
                lambda x: next_lvl_smlnbrs.count(x) == 0, all_next_lvl_smlbrs))
            if len(unique_next_lvl_smlnbrs) != 0:
                next_lvl_smlnbrs = [
                    *next_lvl_smlnbrs, *unique_next_lvl_smlnbrs]

        smlnbrs_copy.append(next_lvl_smlnbrs)
        pattern.append(len(next_lvl_smlnbrs))
        return rec_gen_pattern(last_idx+1)

    rec_gen_pattern()
    return pattern


pprint(smlnbr_pattern([[[4, 2, 3, 1]]]))
