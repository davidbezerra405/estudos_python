frase = 'Curso em Video Python'
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.split())

dividido = frase.split()
print(dividido[0])

data = '21/6/2021'
datadiv = data.split('/')
print(data)
print(datadiv)
data2 = '-'.join(datadiv)
print(data2)
data3 = datadiv[2]+'-'+datadiv[1]+'-'+datadiv[0]
print(data3)

