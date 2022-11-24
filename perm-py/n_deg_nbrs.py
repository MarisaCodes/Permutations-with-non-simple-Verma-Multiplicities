from pprint import pprint
import numpy as np
from sympy import false
from pkg.smlnbr import small_neighbors
from pkg.permutations import get_sym_n
from sympy.combinatorics import Permutation


def smlnbr_lod_to_aoa(smlnbr_lod: list[dict[str, int]], n: int) -> np.ndarray:
    new = []
    for dic in smlnbr_lod:
        new.append(list(dic.values()))
    aoa = np.array(new, dtype=np.int32)
    aoa = np.reshape(aoa, (-1, n))
    return aoa


def aoa_to_aoa(aoa: np.ndarray, n: int) -> np.ndarray:
    new_aoa = np.array([], dtype=np.int32)
    new_lol = []
    for arr in aoa:
        lis = list(arr)
        lod = small_neighbors(lis)
        sml_nbrs = smlnbr_lod_to_aoa(lod, n)
        for sml_nbr in sml_nbrs:
            new_lol.append(sml_nbr)
    new_aoa = np.array(new_lol, dtype=np.int32)
    new_aoa = np.reshape(new_aoa, (-1, n))
    new_aoa = np.unique(new_aoa, axis=0)
    return new_aoa


def nth_deg_nbrs(aoa: np.ndarray, inv: int, num_nbrs: list[int], n: int) -> list[int]:
    if inv <= 0:
        return num_nbrs
    else:
        temp_aoa = aoa_to_aoa(aoa, n)
        num_nbrs.append(len(temp_aoa))
        return nth_deg_nbrs(temp_aoa, inv-1, num_nbrs, n)


def sup_nth_deg_nbrs(lis: list[int], n: int) -> list[int]:
    num_nbrs = []
    aoa_1 = smlnbr_lod_to_aoa(small_neighbors(lis), n)
    lis.insert(0, 0)
    inv = Permutation(lis).inversions() - 1
    num_nbrs = [1, len(aoa_1)]
    return nth_deg_nbrs(aoa_1, inv, num_nbrs, n)


def get_all_false_perms(iden_of_sym_n: list[int]) -> list[list]:
    sym_n = get_sym_n(iden_of_sym_n)
    n = len(iden_of_sym_n)
    aoa_sym_n = []
    all_false_lol = []
    for lis in sym_n:
        aoa_sym_n.append([lis, sup_nth_deg_nbrs(lis, n)])

    for x in aoa_sym_n:
        lis = x[0]
        inv = Permutation(lis).inversions()
        smnbr_pattern = x[1]
        for i in range(inv+1):
            if inv - i < i:
                break
            else:
                if smnbr_pattern[i] != smnbr_pattern[inv-i]:
                    all_false_lol.append(x)
                    break
    return all_false_lol


false_sym = get_all_false_perms([1, 2, 3, 4, 5])
pprint(false_sym)
print(len(false_sym))
