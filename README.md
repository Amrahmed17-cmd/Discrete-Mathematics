# 🧮 Discrete Python

A robust Python application for performing essential discrete mathematics operations through an intuitive console interface.

## 📚 Overview

Discrete Python provides computational tools for fundamental discrete mathematics concepts that form the backbone of computer science and advanced mathematics. The application delivers precise calculations for:

- 🔢 **Combinations (nCr)** - Selection without regard to order
- 🔀 **Permutations (nPr)** - Arrangement where order matters
- ✖️ **Cartesian Products** - Set operations forming ordered pairs

Designed with educational clarity and mathematical precision, this application serves as both a practical tool and a learning resource.

## 🧩 Project Structure

```
discrete_python/
├── main.py               # Application entry point
├── app.py                # Core application and menu interface
└── discrete_math/        # Mathematical operations package
    ├── __init__.py       # Package initializer
    ├── factorial.py      # Factorial calculation implementation
    ├── combinations.py   # Combinations (nCr) implementation
    ├── permutations.py   # Permutations (nPr) implementation
    ├── cartesian.py      # Cartesian product implementation
    └── utils.py          # UI utility functions
```

## ⚙️ Mathematical Implementation

### Combinations (nCr)
Implements the mathematical formula for calculating the number of ways to choose `r` elements from a set of `n` elements without regard to order:

```
C(n,r) = n! / (r! * (n-r)!)
```

Practical applications include:
- Team selection problems
- Lottery number probabilities
- Statistical analysis

### Permutations (nPr)
Calculates arrangements where order matters using the formula:

```
P(n,r) = n! / (n-r)!
```

Practical applications include:
- Arrangement possibilities
- Password combinations
- Scheduling problems

### Cartesian Product
Computes all possible ordered pairs between two sets following the set theory definition:

```
A × B = {(a, b) | a ∈ A, b ∈ B}
```

Practical applications include:
- Coordinate systems
- Database query results
- Function domains and ranges

## 🚀 Usage

1. **Launch the application**:
   ```bash
   python main.py
   ```

2. **Navigate the interactive menu**:
   ```
   =============================================================
   ===================== Discrete Structure ====================
   =============================================================
   1. Combinations
   2. Permutations
   3. Cartesian Product
   4. Exit
   ```

3. **Input your values** based on the selected operation:
   - For combinations and permutations: Values for `n` and `r`
   - For Cartesian products: Elements for two sets

4. **View results** presented in mathematical notation

## ⚡ Performance

- Optimized factorial calculations
- Efficient memory management for set operations
- Cross-platform compatibility

## 📋 Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## 🔧 Installation & Running

### Running in any Python IDE

This project can be run in any Python IDE (PyCharm, VSCode, IDLE, Spyder, etc.) by following these steps:

1. **Open the project** in your preferred Python IDE
2. **Set the working directory** to the project root folder
3. **Run `main.py`** as the entry point
4. Alternatively, you can run the application directly from the terminal/command prompt

Many IDEs offer convenient ways to run Python applications:
- **PyCharm**: Right-click on `main.py` and select "Run 'main'"
- **VSCode**: Open `main.py` and click the "Run" button (▶️)
- **IDLE**: Open `main.py` and press F5
- **Jupyter**: Import the modules and call `main_display()` function

## 🎓 Educational Applications

This project is ideal for:
- 🏫 Computer Science education
- 📐 Discrete Mathematics courses
- 💻 Programming practice
- 🧪 Algorithm implementation

## 👨‍💻 Credits

Developed by: **Amr Ahmed**

## 📜 License

This project is released under the MIT License - see below for details:

```
MIT License

Copyright (c) Amr Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


*"Mathematics is the language in which God has written the universe." - Galileo Galilei* 🌟 