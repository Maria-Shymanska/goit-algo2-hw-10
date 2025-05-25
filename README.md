# 📌 Task 1: QuickSort Comparison

🔍 Description
This script compares the randomized and deterministic QuickSort algorithms.
It benchmarks them on arrays of size: 10_000, 50_000, 100_000, and 500_000.

✅ Features
Implements:

randomized_quick_sort(arr)

deterministic_quick_sort(arr)

Measures execution time for 5 runs

Calculates average time per algorithm per array size

Visualizes results using matplotlib (graph + table)

📦 Requirements
pip install matplotlib numpy

▶️ Run

python quicksort_comparison.py

## 📌 Task 2: Greedy Class Scheduling

🔍 Description
This script solves the set-covering problem using a greedy algorithm to assign teachers to cover all required subjects while minimizing the number of teachers used.

✅ Features
Uses a Teacher class with:

name, age, email, subjects

Function create_schedule(subjects, teachers):

Selects teachers who can cover the most remaining subjects

Resolves ties by choosing the youngest teacher

Graceful failure message if covering all subjects is impossible

▶️ Run
python schedule_greedy.py
