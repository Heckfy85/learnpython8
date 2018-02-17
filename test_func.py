def get_vat(price, vat_rate):
	if price==int and vat_rate==int:
	    vat = price / 100 * vat_rate
	    price_no_vat = price - vat
	print(price_no_vat)
	else :
		print('введите число')
	

price1 = 100
vat_rate1='5'
get_vat(price1,vat_rate1)
