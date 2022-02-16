import math

LatitudeEstacaoAgraus = int(input('Insira a latitude da estação A (º) - '))
LatitudeEstacaoAminutos = int(input('Insira a latitude da estação A (min) - '))
LatitudeEstacaoAsegundos = float(input('Insira a latitude da estação A (seg) - '))

print()

LongitudeEstacaoAgraus = int(input('Insira a longitude da estação A (º) - '))
LongitudeEstacaoAminutos = int(input('Insira a longitude da estação A (min) - '))
LongitudeEstacaoAsegundos = float(input('Insira a longitude da estação A (seg) - '))

#Conversão de Latitudes
latA = (LatitudeEstacaoAgraus + (LatitudeEstacaoAminutos/60) + (LatitudeEstacaoAsegundos/3600))*(-1)

#Conversão de Longitudes
longA = (LongitudeEstacaoAgraus + (LongitudeEstacaoAminutos/60) + (LongitudeEstacaoAsegundos/3600))

print()

LatitudeEstacaoBgraus = int(input('Insira a latitude da estação B (º) - '))
LatitudeEstacaoBminutos = int(input('Insira a latitude da estação B (min) - '))
LatitudeEstacaoBsegundos = float(input('Insira a latitude da estação B (seg) - '))

#Conversão de Latitudes
latB = (LatitudeEstacaoBgraus + (LatitudeEstacaoBminutos/60) + (LatitudeEstacaoBsegundos/3600))*(-1)
print()

LongitudeEstacaoBgraus = int(input('Insira a longitude da estação B (º) - '))
LongitudeEstacaoBminutos = int(input('Insira a longitude da estação B (min) - '))
LongitudeEstacaoBsegundos = float(input('Insira a longitude da estação B (seg) - '))

#Conversão de Longitudes
longB = (LongitudeEstacaoBgraus + (LongitudeEstacaoBminutos/60) + (LongitudeEstacaoBsegundos/3600))

print()
print('==========================================================')
print('PARÂMETROS ESTAÇÃO A')
print('Latitude = ', latA)
print('Longitude = ', longA)

print()
print('PARÂMETROS ESTAÇÃO B')
print('Latitude = ', latB)
print('Longitude = ', longB)