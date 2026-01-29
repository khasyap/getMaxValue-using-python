# Get Maximum Constructible Value Using Python

## 📌 Project Overview
This project implements a **greedy algorithm** to compute the **smallest positive integer value that cannot be constructed** from a given list of positive integers. It is a common **interview and competitive programming problem** that demonstrates sorting and subset sum logic.

---

## 🧠 Problem Statement
Given a list of positive integers, determine the **smallest positive integer that cannot be formed** by summing any subset of the list.

---

## ⚙️ Algorithm Explanation
The array is first sorted in ascending order. A variable called `current` is initialized to **1**, representing the smallest value that cannot yet be formed.

As we iterate through the array:
- If the current number is **less than or equal to `current`**, we expand the range of constructible sums.
- If a number is **greater than `current`**, the loop stops because that value cannot be formed.

---

## 🧩 Code Logic
1. Sort the array  
2. Set `current = 1`  
3. If `num <= current`, update `current += num`  
4. If `num > current`, stop and return `current`

---

## 📌 Sample Input

## 5 
## 1
## 2
## 2
## 5
## 10

---

## 📌 Sample Output

## 21

---

## ⏱️ Time and Space Complexity

- **Time Complexity:** `O(n log n)` due to sorting  
- **Space Complexity:** `O(1)` constant extra memory  

---

## 🎯 Use Cases
- Coding interviews  
- Competitive programming  
- Greedy algorithm practice  
- Data processing  

---

## 🚀 Future Enhancements
- Add automated test cases  
- Build a GUI version  
- Add file input support  
- Convert into a web-based tool  

---

## 👨‍💻 Author
**Konakalla Khasyap Surya Saketh**

