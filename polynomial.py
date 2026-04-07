class Polynomial:
	def __init__(self, coefficients):
		# coefficients is a list [a0, a1, a2, ...] where a0 is the constant term
		# Remove leading zeros to normalize the polynomial
		while len(coefficients) > 1 and coefficients[-1] == 0:
			coefficients.pop()
		self.coeff = coefficients
	
	def P(self, X):
		# Evaluate the polynomial at X using Horner's method
		result = 0
		for c in reversed(self.coeff):
			result = result * X + c
		return result
		
	def __add__(self, other):
		if isinstance(other, (int, float)):
			new_coeff = self.coeff.copy()
			if new_coeff:
				new_coeff[0] += other
			else:
				new_coeff = [other]
			return Polynomial(new_coeff)
		elif isinstance(other, Polynomial):
			size = max(len(self.coeff), len(other.coeff))
			new_coeff = []
			for i in range(size):
				c1 = self.coeff[i] if i < len(self.coeff) else 0
				c2 = other.coeff[i] if i < len(other.coeff) else 0
				new_coeff.append(c1 + c2)
			return Polynomial(new_coeff)
		else:
			return NotImplemented
	
	def __str__(self):
		if not self.coeff:
			return "0"
		terms = []
		for i in range(len(self.coeff) - 1, -1, -1):
			c = self.coeff[i]
			if c == 0:
				continue
			if i == 0:
				terms.append(str(c))
			elif i == 1:
				if c == 1:
					terms.append("X")
				elif c == -1:
					terms.append("-X")
				else:
					terms.append(f"{c}X")
			else:
				if c == 1:
					terms.append(f"X^{i}")
				elif c == -1:
					terms.append(f"-X^{i}")
				else:
					terms.append(f"{c}X^{i}")
		if not terms:
			return "0"
		result = terms[0]
		for term in terms[1:]:
			if term.startswith("-"):
				result += " " + term
			else:
				result += " + " + term
		return result
	
	def __mul__(self, other):
		if isinstance(other, (int, float)):
			new_coeff = [c * other for c in self.coeff]
			return Polynomial(new_coeff)
		elif isinstance(other, Polynomial):
			n = len(self.coeff)
			m = len(other.coeff)
			new_coeff = [0] * (n + m - 1)
			for i in range(n):
				for j in range(m):
					new_coeff[i + j] += self.coeff[i] * other.coeff[j]
			return Polynomial(new_coeff)
		else:
			return NotImplemented
	
	def __sub__(self, other):
		if isinstance(other, (int, float)):
			return self + (-other)
		elif isinstance(other, Polynomial):
			return self + (-1 * other)
		else:
			return NotImplemented
	
	def __eq__(self, other):
		if isinstance(other, Polynomial):
			return self.coeff == other.coeff
		return False
	
	def degree(self):
		if not self.coeff or all(c == 0 for c in self.coeff):
			return -1  # Degree of zero polynomial
		return len(self.coeff) - 1
	
	def derivative(self):
		if self.degree() <= 0:
			return Polynomial([0])
		new_coeff = [i * self.coeff[i] for i in range(1, len(self.coeff))]
		return Polynomial(new_coeff)
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __radd__(self, other):
		return self.__add__(other)