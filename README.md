# 🎯️ Polynomials

A polynomial is of the form $P(X) = \sum_{i}^{n} a_{i}X^{i}$.
This repository allows you to calculate polynomials rapidly.

## Features
- Polynomial evaluation using Horner's method
- Addition, subtraction, and multiplication of polynomials
- Scalar operations (add/multiply by numbers)
- Equality comparison
- Degree calculation
- Derivative computation
- String representation

## 📁️ Project structure
```text
Polynomial/
├── docs
│   ├── polynomial.tex
├── polynomial.py               # main code
├── README.md
└── test_polynomial.py          # Tests 
```
## 💻️ Install and use
1. Clone repository
```text
git clone https://github.com/TifaniohMF/Polynomial.git
cd Polynomial
```
2. Run tests
```bash
python3 test_polynomial.py
```

Example usage:
```python
from polynomial import Polynomial

p1 = Polynomial([1, 2, 3])  # 1 + 2X + 3X^2
p2 = Polynomial([1, 1])     # 1 + X
print(p1 + p2)  # 2 + 3X + 3X^2
print(p1 * p2)  # 1 + 3X + 5X^2 + 3X^3
print(p1.derivative())  # 2 + 6X
```

## 🛠️ Prerequisites
Make sure you have installed:
- Python 3.x
- Git

## 🤝 Contribution
Contributions are welcome! If you want to add a method or improve the existing code:
1. Fork the project
2. Create your feature branch
```bash
git checkout -b feature/newfeature
```
3. Commit your changes
```bash
git commit -m "feat: add feature"
```
4. Push to branch
```bash
git push origin feature/newfeature
```
5. Open Pull request

### Contact
**TifaniohMF** - [GitHub Profile](https://github.com/TifaniohMF)
