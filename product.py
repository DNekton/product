# product 記帳程式
products = [] #一維清單
while True:
	name = input ('輸入商品名稱: ')
	if name == 'q': #if迴圈, 當商品名稱輸入q即中斷迴圈
		break
	price = input ('輸入商品價格: ')
	products.append([name, price]) #直接在append([]), 創作二維清單, 放入商品及價格

print (products)
print ('第一個商品為', products[0][0]) #印出products[一維清單][二維清單]
print ('第一個商品價格為', products[0][1])

for p in products:
	print (p[0], '的價格是', p[1])
#藉由 for loop 依序印出讀取一維清單
