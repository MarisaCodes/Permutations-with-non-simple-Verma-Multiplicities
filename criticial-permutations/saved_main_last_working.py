from pprint import pprint
import pickle
from sympy.combinatorics import Permutation
import numpy as np


def get_sym_n(lis):
    sym_n = []

    def swap_in_place(lis_to_swap, index_a, index_b):
        temp = lis_to_swap[index_a]
        lis_to_swap[index_a] = lis_to_swap[index_b]
        lis_to_swap[index_b] = temp

    def generate(n, heap_list):
        if n == 1:
            sym_n.append(heap_list[:])
            return

        generate(n-1, heap_list)
        for i in range(n-1):
            if n % 2 == 0:
                swap_in_place(heap_list, i, n-1)
            else:
                swap_in_place(heap_list, 0, n-1)
            generate(n-1, heap_list)

    generate(len(lis), lis[:])
    return sym_n


def get_sml_nbrs(perm: Permutation):
    inv_vec = perm.inversion_vector()
    # list to store indices (tuples: (i,j)) of elements in perm that can make valid swaps
    smlnbrs = []
    list_type_perm = list(perm)
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
                    smlnbrs.append(Permutation(tmp_list_type_perm))

    return smlnbrs


def smlnbr_pattern(smlnbrs: list[list[Permutation]]):
    if len(smlnbrs) != 1:
        print("please pass exactly only 1 permutation in List(List(Permutation)) form")
        return
    # list of lists, each containing permutations that are
    # small neighbors of argument `perm` at a given level
    pattern = [1]
    smlnbrs_copy = smlnbrs[:]

    def rec_gen_pattern(last_idx: int = 0):
        if smlnbrs_copy[len(smlnbrs_copy) - 1][0] == Permutation(list(range(len(list(smlnbrs_copy[0][0]))))):
            return

        next_lvl_smlnbrs = []
        for perm in smlnbrs_copy[last_idx]:
            all_next_lvl_smlbrs = get_sml_nbrs(perm)
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


def is_critical(pattern: list[int]):
    i = 0
    j = len(pattern) - 1
    while i != j and i < j:
        if pattern[i] != pattern[j]:
            return (True, i)
        i += 1
        j -= 1
    return (False, None)


def to_perm_class_type(list_type_perm: list[int]):
    return Permutation(
        [int(i) for i in (np.array(list_type_perm)-1)])


def to_list_type_perm_plus_1(perm: Permutation):
    return [int(i) for i in (np.array(list(perm))+1)]


def to_list_type_perm(list_type_perm_plus_1: list[int]):
    return [int(i) for i in (np.array(list_type_perm_plus_1)-1)]


def get_critical_perms(symn: list[list[int]]):
    critical_perms: list[tuple[list[int], list[int], int]] = []
    for list_type_perm in symn:
        perm = Permutation(list_type_perm)
        pattern = smlnbr_pattern([[perm]])
        check = is_critical(pattern)
        if check[0]:
            critical_perms.append(
                (to_list_type_perm_plus_1(perm), pattern, check[1])
            )
    return critical_perms


def get_thrm_criticals(symn_minus1_criticals: list[tuple[list[int], list[int], int]], n: int):
    critical_perms = []
    for list_type_perm_plus_1, _, _ in symn_minus1_criticals:
        symn_list_type_perm = to_list_type_perm(list_type_perm_plus_1)
        symn_list_type_perm.insert(n, n-1)
        perm = Permutation(symn_list_type_perm)
        pattern = smlnbr_pattern([[perm]])
        check = is_critical(pattern)

        right_result = perm
        left_result = perm

        simples = [Permutation(i-1, i) for i in range(n-1, 0, -1)]

        longest_perm = Permutation(list(range(n-1, -1, -1)))

        copies = [(to_list_type_perm_plus_1(perm), pattern, check[1])]
        inverses = []
        longest = []
        longest_inverses = []
        for simple in simples:
            left_result = simple*left_result
            right_result = right_result * simple
            if len(list(filter(lambda x: x[0] == to_list_type_perm_plus_1(left_result), copies))) == 0:
                pattern = smlnbr_pattern([[left_result]])
                check = is_critical(pattern)
                copies.append(
                    (to_list_type_perm_plus_1(left_result), pattern, check[1])
                )
            if len(list(filter(lambda x: x[0] == to_list_type_perm_plus_1(right_result), copies))) == 0:
                pattern = smlnbr_pattern([[right_result]])
                check = is_critical(pattern)
                copies.append(
                    (to_list_type_perm_plus_1(right_result), pattern, check[1])
                )
        for copy in copies:
            mult_long = longest_perm * \
                Permutation(to_list_type_perm(copy[0])) * longest_perm
            if len(list(filter(lambda x: x[0] == to_list_type_perm_plus_1(mult_long), longest))) == 0:
                pattern = smlnbr_pattern([[mult_long]])
                check = is_critical(pattern)
                longest.append(
                    (to_list_type_perm_plus_1(mult_long), pattern, check[1])
                )

        for copy in copies:
            inverse = ~Permutation(to_list_type_perm(copy[0]))
            if len(list(filter(lambda x: x[0] == to_list_type_perm_plus_1(inverse), inverses))) == 0:
                pattern = smlnbr_pattern([[inverse]])
                check = is_critical(pattern)
                inverses.append(
                    (to_list_type_perm_plus_1(inverse), pattern, check[1])
                )

        for inverse in inverses:
            mult_long = longest_perm * \
                Permutation(to_list_type_perm(inverse[0]))*longest_perm
            if len(list(filter(lambda x: x[0] == to_list_type_perm_plus_1(mult_long), longest_inverses))) == 0:
                pattern = smlnbr_pattern([[mult_long]])
                check = is_critical(pattern)
                longest_inverses.append(
                    (to_list_type_perm_plus_1(mult_long), pattern, check[1])
                )

        copies.extend(longest)
        copies.extend(inverses)
        copies.extend(longest_inverses)
        for copy in copies:
            if len(list(filter(lambda x: x[0] == copy[0], critical_perms))) == 0:
                critical_perms.append(copy)
    return critical_perms


sym4_criticals = get_critical_perms(get_sym_n([0, 1, 2, 3]))
thrm_criticals = get_thrm_criticals(sym4_criticals, 5)
pprint(sym4_criticals)
pprint(thrm_criticals)
pprint(len(thrm_criticals))

# print("real...")
# critical_sym6 = get_critical_perms(get_sym_n([0, 1, 2, 3, 4, 5, 6]))
# print(len(critical_sym6))
# pprint(critical_sym6)
