def getMinimumPrice(price1,price2, bundlePrice, number1, number2):
    
    if number1==0 and number2 == 0:
        return 0
    if number1 == 0:
        return number2*price2
    if number2 == 0:
        return number1*price1
    return min(price1+getMinimumPrice(price1, price2, bundlePrice, number1-1, number2), price2+getMinimumPrice(price1, price2, bundlePrice, number1, number2-1), bundlePrice+getMinimumPrice(price1,price2, bundlePrice, number1-1,number2-1))
