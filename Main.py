print('\n' * 100)

cadena=" Hola Ale "
'''reemplazamos lo que tiene la cadena'''
nueva= cadena.replace('Hola','HOLA')  
print(nueva)
'''eliminamos los espacios al principio y al final'''
otramas=cadena.strip()
print(otramas)
'''eliminamos los espacios al principio a la izquierda'''
otramasl=cadena.lstrip()
print(otramasl)
'''eliminamos los espacios al principio a la derecha'''
otramasr=cadena.rstrip()
print(otramasr)

'''cambiamos todo a may�sculas'''
ma=cadena.upper()
print(ma)
'''cambiamos todo a min�sculas'''
minu=cadena.lower()
print(minu)


''' Coratmos cada elemento por el signo ? '''
cadenaej2=" Hola Ale  ? Jos� ? Pedro Miguel ? Jorge Luis"
print(cadenaej2.split("?"))
