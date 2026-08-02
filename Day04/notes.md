# Day 04: Python User Inputs & Core Logic Projects

Welcome to Day 04 of my Python learning journey! Today's focus was on capturing dynamic user data via `input()`, type casting, and applying basic math and conditional logic to build functional utility scripts.

---

## 📂 Programs Overview

### 1. Age Finder (`age_finder.py`)
* **Concept:** Takes the user's birth year or current age as input.
* **Logic:** Subtracts input from the current year (or calculates remaining lifespan milestones) using basic arithmetic and type conversion (`int()`).

### 2. Simple Interest Calculator (`interest_calculator.py`)
* **Concept:** Computes financial simple interest.
* **Logic:** Prompts user for Principal amount ($P$), Rate of interest ($R$), and Time ($T$).
* **Formula:** `SI = (P * R * T) / 100` using float/integer casting.

### 3. Number Checker (`number_checker.py`)
* **Concept:** Evaluates a user-inputted number.
* **Logic:** Uses conditional statements (`if/else`) and the modulo operator (`%`) to check if a number is even/odd, positive/negative, or zero.

### 4. BMI Calculator (`bmi_calculator.py`)
* **Concept:** Calculates Body Mass Index.
* **Logic:** Takes weight in kilograms and height in meters.
* **Formula:** `BMI = weight / (height ** 2)`, complete with formatted string (`f-string`) outputs.

---

## 🚀 Key Takeaways & Concepts Learned
* **User Input Handling:** Mastered the `input()` function, noting that it always returns data as a `str` type.
* **Type Casting:** Practiced converting strings to `int()` and `float()` to perform mathematical operations safely.
* **F-Strings:** Utilized formatted string literals for clean, readable output generation.
* **Basic Conditionals:** Reinforced program branching using `if`, `elif`, and `else` blocks.

---

## 🏃 How to Run the Scripts
1. Make sure you have Python installed (v3.x recommended).
2. Clone this repo and navigate to the `day04` folder:
   ```bash
   cd day04
   ```
3. Run any individual script:
   ```bash
   python bmi_calculator.py
   ```
