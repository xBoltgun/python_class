def duplicate_encode(word):
	word = word.lower()
	l = []
	for x in word:
		n = word.count(x)
		if n > 1:
			l.append(')')
		elif n == 0 or n == 1:
			l.append('(')
	return ''.join(l)