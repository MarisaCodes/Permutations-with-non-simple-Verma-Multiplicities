def gen_perm_from_arr(lis):
    perm = {}

    for index, item in enumerate(lis):
        index += 1
        perm[index] = item
    return perm


def small_neighbors(lis: list[int]) -> list[dict[str, int]]:
    perm = gen_perm_from_arr(lis)
    lis_small_neighbors = []
    for i in perm:
        for j in perm:
            if int(j) <= int(i):
                continue
            else:
                tau = lis[int(i):int(j)-1]
                if not bool(len(tau)):
                    if perm[i] > perm[j]:
                        new_perm = {**perm}
                        new_perm[i] = perm[j]
                        new_perm[j] = perm[i]
                        lis_small_neighbors.append(new_perm)
                else:
                    condition_bool = False
                    for m in range(len(tau)):
                        if perm[i] < perm[j]:
                            break
                        else:
                            if tau[m] > perm[i] or tau[m] < perm[j]:
                                condition_bool = True
                            else:
                                condition_bool = False
                                break
                    if condition_bool:
                        new_perm = {**perm}
                        new_perm[i] = perm[j]
                        new_perm[j] = perm[i]
                        lis_small_neighbors.append(new_perm)
    return lis_small_neighbors
