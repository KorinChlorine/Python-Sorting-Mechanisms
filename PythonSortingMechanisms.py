def print_results(algorithm_name, sorted_weights, stats):
    print(f"{algorithm_name}:")
    print("Sorted Weights:", " ".join(map(str, sorted_weights)))
    for stat_name, stat_value in stats.items():
        print(f"Total {stat_name}:", stat_value)

def bubble_sort(weights):
    comparisons, swaps = 0, 0
    for i in range(len(weights) - 1):
        for j in range(len(weights) - i - 1):
            comparisons += 1
            if weights[j] > weights[j + 1]:
                weights[j], weights[j + 1] = weights[j + 1], weights[j]
                swaps += 1
    return weights, {"Comparisons": comparisons, "Swaps": swaps}

def selection_sort(weights):
    comparisons, swaps = 0, 0
    for i in range(len(weights) - 1):
        min_index = i
        for j in range(i + 1, len(weights)):
            comparisons += 1
            if weights[j] < weights[min_index]:
                min_index = j
        if min_index != i:
            weights[i], weights[min_index] = weights[min_index], weights[i]
            swaps += 1
    return weights, {"Comparisons": comparisons, "Selections": swaps}

def insertion_sort(weights):
    comparisons, movements = 0, 0
    for i in range(1, len(weights)):
        key = weights[i]
        j = i - 1
        while j >= 0 and weights[j] > key:
            weights[j + 1] = weights[j]
            j -= 1
            comparisons += 1
            movements += 1
        weights[j + 1] = key
    return weights, {"Comparisons": comparisons, "Insertions": len(weights) - 1}

def merge_sort(weights):
    splits, merges = 0, 0

    def merge(array, left, mid, right):
        nonlocal merges
        left_part, right_part = array[left:mid + 1], array[mid + 1:right + 1]
        i = j = 0
        for k in range(left, right + 1):
            if j >= len(right_part) or (i < len(left_part) and left_part[i] <= right_part[j]):
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
        merges += 1

    def sort(array, left, right):
        nonlocal splits
        if left < right:
            mid = (left + right) // 2
            splits += 1
            sort(array, left, mid)
            sort(array, mid + 1, right)
            merge(array, left, mid, right)

    sort(weights, 0, len(weights) - 1)
    return weights, {"Splits": splits, "Merges": merges}

def run_sorting_algorithms():
    weights = [55, 11, 68, 33, 28, 98, 55, 12]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
    }
    for name, sort_func in algorithms.items():
        sorted_weights, stats = sort_func(weights[:])  
        print_results(name, sorted_weights, stats)
        print("\n")

if __name__ == "__main__":
    run_sorting_algorithms()
