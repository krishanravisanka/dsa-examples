# Python Data Structures & Algorithms Examples

This repository contains a collection of Python scripts that provide clear, practical implementations of common data structures and algorithms. Each script is a standalone solution to a classic computer science problem, designed for learning and reference.

---

## Algorithms Included

### 1. Two Sum
- **File:** `two_sum.py`
- **Problem:** Given an array of integers `nums` and a `target`, return the indices of the two numbers that add up to `target`.
- **Algorithm:** Uses a **single-pass hash map (dictionary)** for O(n) time complexity. It stores seen numbers and their indices, checking for the required "complement" at each step.

### 2. Contains Duplicate
- **File:** `contains_duplicate.py`
- **Problem:** Given an array of integers, determine if any value appears at least twice.
- **Algorithm:** Employs a **hash set** for efficient O(n) checking. It iterates through the list, adding each number to the set and returning `true` if a number is already present.

### 3. Valid Anagram
- **File:** `valid_anagram.py`
- **Problem:** Given two strings, determine if the second string is an anagram of the first.
- **Algorithm:** Uses a **frequency counter (hash map)** to count character occurrences in both strings. It returns `true` if the character counts are identical for both.

### 4. Top K Frequent Elements
- **File:** `top_k_frequent_elements.py`
- **Problem:** Given an integer array and an integer `k`, return the `k` most frequent elements.
- **Algorithm:** First, it builds a **frequency map** of all elements. Then, it sorts the elements by frequency in descending order and returns the top `k` items.

### 5. Product of Array Except Self
- **File:** `product_of_array_except_self.py`
- **Problem:** Given an integer array, return an answer array such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
- **Algorithm:** An efficient O(n) solution that uses two passes. The first pass calculates the **prefix products**, and the second pass calculates the **postfix products** to find the final result without using division.

### 6. Three Sum
- **File:** `three_sum.py`
- **Problem:** Find all unique triplets in an array that sum to zero.
- **Algorithm:** The solution first **sorts the array**. Then, it iterates through the array and uses a **two-pointer approach** for each element to find pairs that sum to the required value, efficiently avoiding duplicate triplets.

### 7. Maximum Subarray (Kadane's Algorithm)
- **File:** `kadanes_algorithm.py`
- **Problem:** Find the contiguous subarray within a one-dimensional array of numbers that has the largest sum.
- **Algorithm:** A classic implementation of **Kadane's Algorithm**. It iterates through the array once, tracking the maximum sum of a subarray ending at the current position and the overall maximum sum found so far.

### 8. Minimum Window Substring
- **File:** `minimum_window_substring.py`
- **Problem:** Given two strings `s` and `t`, find the minimum window (substring) in `s` which contains all the characters in `t`.
- **Algorithm:** This script demonstrates a **brute-force approach**. It generates every possible substring of `s` and checks if it contains the required characters from `t` using a frequency counter.

---

## How to Run

Each script is self-contained and can be run individually from your terminal:

```bash
python two_sum.py
python contains_duplicate.py
python valid_anagram.py
python top_k_frequent_elements.py
python product_of_array_except_self.py
python three_sum.py
python kadanes_algorithm.py
python minimum_window_substring.py
```

## Requirements

All scripts use standard Python 3 libraries and do not require any external dependencies.
