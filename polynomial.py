class Polynomial:
	def __init__(self, coefficient):
	# coefficient is a list [a0, a1, a2, ...]
		self.coeff = coefficient
	
	def P(self, X):
	# X is a variable
	# I evaluate a polynomial ith a Horner method
		result = 0
		for c in reversed(self.coeff):
			result += result*X + c
		return result
		
	def __add__(self, other):
	# Permits to calculate polynomial with operator '+'
		size = max(len(self.coeff), len(other.coeff))
		new_coeff = [0] * size
		for i in range(size):
			c1 = self.coeff[i] if i < len(self.coeff) else 0
			c2 = other.coeff[i] if i < len(other.coeff) else 0
			new_coeff[i] = c1 + c2
		return Polynomial(new_coeff)
	
	# Display polynomial
	def __str__(self):
		termes = []
		for i,c in enumerate(self.coeff):
			if i == 0:
				termes.append(str(c)) # Just numbers for X^0
			elif i == 1:
				termes.append(f"{c}X") # Just X for X^1
			else:
				termes.append(f"{c}X^{i}") # X^n for rest
		return " + ".join(termes)