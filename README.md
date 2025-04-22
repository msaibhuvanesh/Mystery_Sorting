

## 📌 Project Overview

This project focuses on implementing six classic sorting algorithms and analyzing their computational efficiency using real-world IMDb data. The algorithms include:

- Insertion Sort  
- Selection Sort  
- Quick Sort  
- Heap Sort  
- Shell Sort  
- Merge Sort  

i will implement external memory-constrained merge sort for large-scale datasets.

---

## 🗂️ Project Structure

### 🔧 Source Files

- `sorting_algos.py`  
  Implements all six sorting algorithms and handles test cases 1–12, including data filtering logic.

- `mystery_sorting.py`  
  Handles test cases 13–15 (external sorting with a 2000-record memory constraint).

- `testcases.py`  
  Provided test driver to check correctness and performance. **Do not modify this file.**

### 📁 Datasets

- `imdb_dataset.csv`  
  Full dataset with movie information.

- `test_cases_1_2.csv`  
  Smaller dataset for test cases 1.1–2.3.

---

## ✅ Test Case Coverage

### ➤ Basic Sorting (Test Cases 1–6)
Tests the correctness of individual sorting algorithms on different columns like `startYear`, `averageRating`, and `primaryTitle`.

### ➤ Multi-Column Sorting (Test Cases 7–10)
Applies sorting with filtered datasets using multiple columns and sorting methods.

### ➤ Large-Scale Sorting (Test Cases 11–12)
Tests merge and quick sort on the full dataset with multiple column sorting.

### ➤ External Merge Sort (Test Cases 13–15)
Implements memory-constrained external merge sort (2000-record limit) and produces sorted output across 93 chunk files.

---

## 🔍 Data Filtering Logic

- **Test Case 7:** Filter movies from years 1941 to 1955
- **Test Case 8:** Filter by genre (`Adventure`, `Drama`)
- **Test Case 9:** Filter by profession (`assistant_director`, `cinematographer`, etc.)
- **Test Case 10:** Filter names starting with vowels

---

## 📁 Output Files

### ➤ Chunked Sorting Output

- `./Individual/sorted_1.csv` to `./Individual/sorted_93.csv`

### ➤ Final Sorted Output

- `./Final/sorted_1.csv` to `./Final/sorted_93.csv`

---

## 🚀 How to Run

Use the testing script:

```bash
python testcases.py
