products = []
while True:
	name = input('Please enter the product name:')
	if name == 'q':
		break
	price = input('Please enter the product price:')
	if price == 'q':
		break
	products.append([name, price])

for p in products:
	print('Product name:', p[0], 'Product price', p[1])