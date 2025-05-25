import random
import time
import matplotlib.pyplot as plt

# Randomized QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Deterministic QuickSort (pivot = middle element)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Measure average execution time
def measure_time(sort_func, arr, repeats=5):
    total = 0
    for _ in range(repeats):
        copied = arr.copy()
        start = time.perf_counter()
        sort_func(copied)
        total += time.perf_counter() - start
    return total / repeats

# Main benchmark runner
def run_benchmarks():
    sizes = [10_000, 50_000, 100_000, 500_000]
    rand_times = []
    det_times = []

    for size in sizes:
        arr = [random.randint(0, 1_000_000) for _ in range(size)]
        print(f"\nArray size: {size}")

        rand_time = measure_time(randomized_quick_sort, arr)
        det_time = measure_time(deterministic_quick_sort, arr)

        print(f"  Randomized QuickSort: {rand_time:.4f} seconds")
        print(f"  Deterministic QuickSort: {det_time:.4f} seconds")

        rand_times.append(rand_time)
        det_times.append(det_time)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, marker='o', label="Randomized QuickSort")
    plt.plot(sizes, det_times, marker='s', label="Deterministic QuickSort")
    plt.xlabel("Array Size")
    plt.ylabel("Average Execution Time (seconds)")
    plt.title("Performance Comparison: Randomized vs Deterministic QuickSort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run benchmarks
if __name__ == "__main__":
    run_benchmarks()
