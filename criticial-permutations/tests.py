# from sympy.combinatorics import Permutation
# from pprint import pprint
# import numpy as np


# def get_sml_nbrs(list_type_perm: list[int]) -> list[list[int]]:
#     perm = list_to_perm(list_type_perm)
#     inv_vec = perm.inversion_vector()
#     # list to store indices (tuples: (i,j)) of elements in perm that can make valid swaps
#     smlnbrs = []
#     for i, num_invs in enumerate(perm.inversion_vector()):
#         count_to_stop = 0
#         for j in range(i+1, len(list_type_perm)):
#             if count_to_stop == num_invs:
#                 break
#             if list_type_perm[j] < list_type_perm[i]:
#                 count_to_stop += 1
#                 check = list(filter(
#                     lambda x: x < list_type_perm[i] and x > list_type_perm[j], list_type_perm[i+1:j]))
#                 if len(check) != 0:
#                     continue
#                 else:
#                     tmp_list_type_perm = list_type_perm[:]
#                     tmp = tmp_list_type_perm[i]
#                     tmp_list_type_perm[i] = tmp_list_type_perm[j]
#                     tmp_list_type_perm[j] = tmp
#                     smlnbrs.append(tmp_list_type_perm)

#     return smlnbrs

# # small neighbors structure: e.g. {"1432": [[1432], [1423, 1342], [1243, 1324], [1234]]}


# def perm_to_list(perm: Permutation) -> list[int]:
#     return list(np.array(list(perm))+1)


# def list_to_perm(list_type_perm: list) -> Permutation:
#     return Permutation(list(np.array(list_type_perm)-1))


# def smlnbr_pattern(list_type_perm: list[int]):
#     parent_perm_inversions = list_to_perm(list_type_perm).inversions()
#     identity = list(range(1, len(list_type_perm)+1))
#     # list form of a permutation (e.g. [1,3,4,2] in sym(4))
#     current_parent = list_type_perm
#     d = {}
#     # f'{"".join([str(i) for i in list_type_perm])}': [[list_type_perm]]
#     last_idx = 0

#     def rec_gen_pattern(current_parent: list[int] = list_type_perm, smlnbrs: list[list[int]] = [[list_type_perm]], last_idx: int = 0):
#         current_parent_inversions = list_to_perm(current_parent).inversions()
#         current_parent_key = f'{"".join([str(i) for i in current_parent])}'
#         if current_parent == identity:
#             pprint(smlnbrs)
#             return
#         next_lvl_nbrs = get_sml_nbrs(current_parent)
#         for nbr in next_lvl_nbrs:
#             rec_gen_pattern(nbr, [*smlnbrs, next_lvl_nbrs])

#     rec_gen_pattern(current_parent=list_type_perm)
#     return d

from concurrent.futures import ProcessPoolExecutor


def square(n):
    return n*n


with ProcessPoolExecutor() as executor:
    res = executor.map(square, [1, 2, 3, 4])

# print(list(res))
