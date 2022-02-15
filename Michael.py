for i in range(1, 101):
	if i % 3 | i % 5:
		print('Michael Marchese')
	elif i % 3:
		print('Michael')
	elif i % 5:
		print('Marchese')
	else:
		print(i)
