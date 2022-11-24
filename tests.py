# from itertools import permutations
# from sympy.combinatorics import Permutation
import numpy as np
lis = np.array([1, 2, 3, 4])
# perm = {'1': 4, '2': 2, '3': 3, '4': 1}

# lol_1 = [[3, 2, 1, 4], [2, 3, 4, 1], [3, 1, 4, 2]]
# lol_2 = [[2, 3, 4, 1], [2, 4, 1, 3], [1, 4, 3, 2]]
# arr = np.array(lol_1+lol_2)
# print(np.unique(arr, axis=0))


def sup_fac(x):
    v = []
    return fac(x, v)


def fac(x: int, v: list[int]):
    if x == 0:
        return v
    else:
        v.append(x)
        return fac(x-1, v)


#print(sup_fac(5))
for i in range(3):
     print(i)

# lis = np.append(lis, np.array([55]))

# print(lis)


# def convert_smlnbr_to_list(perm):
#     perm_lis = []
#     for num in perm.values():
#         perm_lis.append(num)
#     perm_lis.insert(0, 0)
#     return perm_lis


# def convert_smlnbrlod_to_lol(lod):
#     smlnbr_lis = []
#     for perm in lod:
#         smlnbr_lis.append(np.array(convert_smlnbr_to_list(perm)))
#     return np.array(smlnbr_lis)


# def n_deg_lis_to_n_plus_1_lol(lis):
#     n_deg_lod = small_neighbors(lis)
#     n_deg_lol = convert_smlnbrlod_to_lol(n_deg_lod)
#     np1_deg_lod = []
#     for smlnbr in n_deg_lol:
#         np1_deg_lod.append(small_neighbors(smlnbr))
#     np1_deg_lod = np.array(np1_deg_lod)
#     np1_deg_lod = np1_deg_lod.reshape(np1_deg_lod.size)
#     np1_deg_lol = convert_smlnbrlod_to_lol(np1_deg_lod)
#     return np.unique(np1_deg_lol, axis=0)

# #########


# def n_deg_lol_to_n_plus_1_lol(lol):
#     np1_deg_lod = []
#     for smlnbr in lol:
#         np1_deg_lod.append(small_neighbors(smlnbr))
#     np1_deg_lod = np.array(np1_deg_lod)
#     np1_deg_lod = np1_deg_lod.reshape(np1_deg_lod.size)
#     np1_deg_lol = convert_smlnbrlod_to_lol(np1_deg_lod)
#     return np.unique(np1_deg_lol, axis=0)

# ####


# def sec_degree_neighbors(lis):
#     perm_lis = lis[:]
#     perm_lis.insert(0, 0)
#     perm_lis = Permutation(perm_lis)
#     inv = perm_lis.inversions()
#     if inv == 0:
#         return "This is the identity element"
#     else:
#         inv -= 1
#         return n_deg_lis_to_n_plus_1_lol(lis)


# def nth_deg_func(inv, first_deg_lol):
#     nth_deg_lol = []

#     # perm_lis = lis[:]
#     # perm_lis.insert(0, 0)
#     # perm_lis = Permutation(perm_lis)
#     # inv = perm_lis.inversions()

#     if inv == 0:
#         return nth_deg_lol
#     else:
#         temp = n_deg_lol_to_n_plus_1_lol(first_deg_lol)
#         nth_deg_lol.append(temp)
#         nth_deg_func(inv-1, temp)


# # test = sec_degree_neighbors([4, 2, 3, 1])
# # pprint.pprint(test)
# inv = Permutation([0, 4, 2, 3, 1]).inversions()
# val = convert_smlnbrlod_to_lol(small_neighbors([4, 2, 3, 1]))
# test = nth_deg_func(inv, val)
# print(test)


t = [[[1, 4, 2, 3], [2, 3, 4, 1], [2, 4, 1, 3]],
     [[2, 3, 4, 1], [3, 1, 4, 2], [3, 2, 1, 4]]]
c = [[[5, 4, 2, 3], [2, 3, 4, 1], [2, 4, 1, 3]],
     [[2, 3, 4, 1], [3, 1, 4, 2], [3, 2, 1, 4]]]
# n = np.array(t)
# f = np.array(c)
# t2 =[]
# n = np.reshape(n, (-1, 4))
# f = np.reshape(f, (-1, 4))
# t2.append(n)
# t2.append(f)
# t2 = np.array(t2,dtype=np.int32)
# t2 = np.reshape(t2, (-1, 4))
# print(t2)
