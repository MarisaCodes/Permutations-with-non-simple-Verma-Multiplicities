def get_sym_n(lis):
    lol = []

    def swap_in_place(lis_to_swap, index_a, index_b):
        temp = lis_to_swap[index_a]
        lis_to_swap[index_a] = lis_to_swap[index_b]
        lis_to_swap[index_b] = temp

    def generate(n, heap_list):
        if n == 1:
            lol.append(heap_list[:])
            return
        generate(n-1, heap_list)

        for i in range(n-1):
            if n % 2 == 0:
                swap_in_place(heap_list, i, n-1)
            else:
                swap_in_place(heap_list, 0, n-1)
            generate(n-1, heap_list)

    generate(len(lis), lis[:])
    return lol
