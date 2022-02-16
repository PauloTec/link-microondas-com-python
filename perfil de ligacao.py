import math

print('|-------------------------------------------------------------|')
print('|              Kundiama, Tecnologia e Inovação                |')
print('|            Telecomunicações - Radiocomunicação              |')

print('|                                                             |')
print('|    Cálculo de Ligação Por Microondas entre Zona 1 e Zona 2  |')
print('|                                                             |')

print('| Elaborado por:                                              |')
print('|            Engº Diassilua paulo Simao (10093)               |')
print('|                                                             |')

print('| Em memória: Professor Dr. Engº Alberto Amaral Lopes         |')
print('|-------------------------------------------------------------|')

#----------------------------------------------------------------
# Constantes de Atenuação
#-----------------------------------------------------------------
A_atmosferica = 0.5 #Atenuação atmosferica
A_guia_ondas1 = 0.5 #Atenuação nos guias de ondas
A_guia_ondas2 = 0.5 #atenuacao nos guias de onda ou cabos estação 2 [db]

T_ceu = 120 #temperatura vindo do ceu T sky
LarguraDeBandaDoRuido = 60 #largura de banda do Ruído (60MHz)

L = 1.58 #Para calcular diponibilidade do sistema

#----------------------------------------------------------------
# Constantes Base do Sistema (variáveis padrões do sistema)
#-----------------------------------------------------------------
e = 2.7 #euller
Nq = 16 #nivel de quantização
Mc = 3 #Margem de crescimento da arvore no ponto critico 3m
Ms = 5 #Margem de segurança devido a exatidão das medidas 5m

#------------ Potencias no sistema por defeito
PotenciaTx = 29 #Potência de transmissão em dBm
PotenciaRx = 29 #em dBm

PotenciaRecepcaoSistema = -80 #em dBm

# ==================================================================
# INÍCIO DO PROGRAMA
#---------------------- 1º LOCALIZAÇÃO DAS ESTAÇÕES

nomeEstacaoA = input('Nome da localização da estaçao A - ')
nomeEstacaoB = input('Nome da localização da estaçao B - ')

#---------------------- 2º CÁLCULO DOS PONTOS GEOGRÁFICOS DAS ESTAÇÕES

LatitudeEstacaoAgraus = int(input('Insira a latitude da estação A (º) - '))
LatitudeEstacaoAminutos = int(input('Insira a latitude da estação A (min) - '))
LatitudeEstacaoAsegundos = float(input('Insira a latitude da estação A (seg) - '))
print()
LongitudeEstacaoAgraus = int(input('Insira a longitude da estação A (º) - '))
LongitudeEstacaoAminutos = int(input('Insira a longitude da estação A (min) - '))
LongitudeEstacaoAsegundos = float(input('Insira a longitude da estação A (seg) - '))
print()
LatitudeEstacaoBgraus = int(input('Insira a latitude da estação B (º) - '))
LatitudeEstacaoBminutos = int(input('Insira a latitude da estação B (min) - '))
LatitudeEstacaoBsegundos = float(input('Insira a latitude da estação B (seg) - '))
print()
LongitudeEstacaoBgraus = int(input('Insira a longitude da estação B (º) - '))
LongitudeEstacaoBminutos = int(input('Insira a longitude da estação B (min) - '))
LongitudeEstacaoBsegundos = float(input('Insira a longitude da estação B (seg) - '))

#---------- Dados do ponto crítico
print()
LatitudePontoCriticoGraus = int(input('Insira a latitude do Ponto Crítico (º) - '))
LatitudePontoCriticoMinutos = int(input('Insira a latitude do Ponto Crítico (min) - '))
LatitudePontoCriticoSegundos = float(input('Insira a latitude do Ponto Crítico (seg) - '))

print()
LongitudePontoCriticoGraus = int(input('Insira a longitude do Ponto Crítico (º) - '))
LongitudePontoCriticoMinutos = int(input('Insira a longitude do Ponto Crítico (min) - '))
LongitudePontoCriticoSegundos = float(input('Insira a longitude do Ponto Crítico (seg) - '))

#Conversão de Latitudes
latA = (LatitudeEstacaoAgraus + (LatitudeEstacaoAminutos/60) + (LatitudeEstacaoAsegundos/3600))*(-1)
latB = (LatitudeEstacaoBgraus + (LatitudeEstacaoBminutos/60) + (LatitudeEstacaoBsegundos/3600))*(-1)
latPontoCritico = (LatitudePontoCriticoGraus + (LatitudePontoCriticoMinutos/60) + (LatitudePontoCriticoSegundos/3600))*(-1)

#Conversão de Longitudes
longA = (LongitudeEstacaoAgraus + (LongitudeEstacaoAminutos/60) + (LongitudeEstacaoAsegundos/3600))
longB = (LongitudeEstacaoBgraus + (LongitudeEstacaoBminutos/60) + (LongitudeEstacaoBsegundos/3600))
longPontoCritico = (LongitudePontoCriticoGraus + (LongitudePontoCriticoMinutos/60) + (LongitudePontoCriticoSegundos/3600))

#---------------------- Altura das estações em relação ao nível do mar
print()
altitudeMarA = float(input('Digite a Altitude em relação ao nivel do mar da Estacao A (Zona 1):  '))
altitudeMarB = float(input('Digite a Altitude em relação ao nivel do mar da Estacao B (Zona 2):  '))
AltitudePontoCritico = float(input('Digite a Altitude do Ponto crítico em relação ao nivel do mar: '))

#---------------------- 3º CÁLCULO DA DISTÂNCIA GEOGRÁFICA ENTRE AS DUAS ESTAÇÕES
b=abs((360+latA)*(math.pi/180)-((360+latB)*(math.pi/180)))
A = math.cos((90-(latA))*(math.pi/180))
B = math.cos((90-(latB))*(math.pi/180))

C = math.sin((90-(longA))*(math.pi/180))
D = math.sin((90-(longB))*(math.pi/180))

distancia_total = (6373*(math.acos((math.cos(b))*((A*B)+(C*D)))))+0.154
dAB = float(input('Digite a distância entre estação A e B que foi retirado do mapa (km):  '))

#---------------------- 3.1º Cálculo do Azimute
Azimute_eixo_x = math.atan((longA - longB)/(latA - latB))

if ((longA - longB)< 0) or ((latA - latB) < 0):
    Azimute_eixo_y = 360 + Azimute_eixo_x
else:
     Azimute_eixo_y = 360 - Azimute_eixo_x

#---------------------- Frequência de Operação, Escolhido na tabela de acordo a distância total de ligação
frequencia_uplink = float(input('De acordo a distância total, insira a Frequência de Uplink (GHz): '))

#---------------------- 3.2º Distância entre antenas e pontos críticos

#-------------------- Para distâncias inseridas retirados do mapa
#distância de acordo dados retirados do mapa
DistanciaEstacao1PontoCriticoMapa = float(input('Digite a distancia entre estação A e ponto Critico (ponto de obstrução):  '))
DistanciaEstacao2PontoCriticoMapa = dAB - DistanciaEstacao1PontoCriticoMapa

#Para distâncias inseridas e calculadas pelo software
#reutilizar distancia da estação A e o ponto crítico inserido
DistanciaEstacao2PontoCritico = distancia_total - DistanciaEstacao1PontoCriticoMapa

#---------------------- 4º CÁLCULO DO RAIO DE FRESNEL E RAIO MÁXIMO
A = DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCriticoMapa
B = DistanciaEstacao1PontoCriticoMapa+DistanciaEstacao2PontoCriticoMapa

A1 = DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCritico
B1 = DistanciaEstacao1PontoCriticoMapa+DistanciaEstacao2PontoCritico

#----------- Cálculo do Raio de Fresnel no ponto crítico a 100% com distâncias do mapa
auxiliar = A/(B*frequencia_uplink)
RaioFresnel = 550*math.sqrt(auxiliar)

#----------- Cálculo do Raio de Fresnel no ponto crítico a 100% com distâncias calculadas
auxiliar1 = A1/(B1*frequencia_uplink)
RaioFresnel1 = 550*math.sqrt(auxiliar1)

#----------- Cálculo do Raio de Fresnel no ponto crítico a 60%
RaioFresnel60 = RaioFresnel*0.6
RaioFresnel60_1 = RaioFresnel1*0.6 #com dist calculadas

#----------- Cálculo do Raio de Fresnel em relação a Distância total e Frequência de Uplink
auxiliarRaioFresnel2 = A/(distancia_total*frequencia_uplink)
RaioFresnel_freq_uplink = 550*math.sqrt(auxiliarRaioFresnel2)

auxiliarRaioFresnel21 = A1/(distancia_total*frequencia_uplink)
RaioFresnel_freq_uplink1 = 550*math.sqrt(auxiliarRaioFresnel21)

#Cálculo Do Raio Da 1ª Zona De Fresnel
distancia1 = distancia_total - DistanciaEstacao1PontoCriticoMapa
distancia2 = distancia_total - DistanciaEstacao2PontoCritico

auxiliarRaio1Zona = (distancia1*distancia2)/(distancia_total*frequencia_uplink)
Raio1ZonaFresnel = 17.3*math.sqrt(auxiliarRaio1Zona)

#----------- Cálculo do Raio Máximo
auxiliarRaioMaximo= distancia_total/frequencia_uplink
RaioMaximo = 8.657*math.sqrt(auxiliarRaioMaximo)

RaioMaximo1 = 545*math.sqrt(auxiliarRaioMaximo)

#Outra forma de calcular raio máximo
auxiliarRMaximo= (distancia1*distancia2)/distancia_total
RaioMaximoVersao2 = 545*math.sqrt(auxiliarRaioMaximo)

#----------- Correção equivalente da curvatura da Terra para k=4/3 no ponto crítico.
k_min = 4/3
diametroTerra = 12740 #em km

#Correção equivalente da terra para K=4/3+100% do raio de Fresnel no ponto crítico. Soma dos parâmetros H_m e RF
Hm = (DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCriticoMapa)/(k_min*diametroTerra)
Hc = Hm+RaioFresnel #Correção propriamente dito, com fresnel (de distancias) retirados do mapa

Hm1 = (DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCritico)/(k_min*diametroTerra)
Hc1 = Hm+RaioFresnel1 #Correção propriamente dito, com fresnel (de distancias) calculados

#-------------- CALCULO DA ALTURA DAS ANTENAS
#Altura previsto da antena
AlturaAntena= k_min+RaioFresnel
AlturaAntena1= k_min+RaioFresnel1 #com distancias calculados

#Altura máxima previsto da antena
AlturaMaximaAntena =  ((DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCriticoMapa))/((AlturaAntena*12740)) #Mapa

AlturaMaximaAntena1 =  ((DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCritico))/((AlturaAntena1*12740)) #Calculaado

#Altura previsto da antena considerando raio de fresnel
AlturaAntenaConsiderado = AlturaMaximaAntena+RaioFresnel
AlturaAntenaConsiderado1 = AlturaMaximaAntena1 + RaioFresnel1

#CÁLCULO DA ALTURA DA ANTENA DE RECEPÇÃO
auxiliarAntenaRx = distancia_total * (AltitudePontoCritico + (Hc*1000) + Mc + Ms - altitudeMarB)
auxiliarAntenaRx2 = (DistanciaEstacao2PontoCritico * (altitudeMarA + AlturaAntenaConsiderado - altitudeMarB))

alturaAntenaB = (auxiliarAntenaRx) - (auxiliarAntenaRx2) / (DistanciaEstacao1PontoCriticoMapa)

#Cálculo da Altura da Mínima da Antena de Recepção (com 60% Raio de Fresnel e Kmin)
alturaAntenaMinima = (DistanciaEstacao1PontoCriticoMapa*DistanciaEstacao2PontoCritico)/(k_min*diametroTerra)

#Cálculo da Altura da Antena de Recepção considerado com 60% Raio de Fresnel e Kmin
alturaAntenaMinima60 = alturaAntenaMinima+RaioFresnel60

#h2 = distancia_total*(hpc+Hc+Mc+Ms-hB)

#-------------- CALCULO DAS ATENUAÇÕES
print()
frequencia_opracao = float(print('Insere a frequência de operação do sistema'))
frequencia_downlink = float(print('Insere a frequência de downlink'))
# 1º ATENUAÇÃO NO ESPAÇO LIVRE EM DB com a frequência de operação do sistema
AtenEspacoLivreMapa = 43.4 + 20 * math.log10(dAB * frequencia_uplink)
AtenEspacoLivre = 43.4 + 20 * math.log10(distancia_total * frequencia_uplink) #distância total calculado

#1.1º Atenuacao na transmissão, por comunicação ser bi direcional, Usar frequencia de uplink na fórmula por ser Tx
AtenEspacoLivreTx_mapa = 32.45 + 20 * math.log10(dAB * frequencia_downlink)
AtenEspacoLivreTx = 32.45 + 20 * math.log10(distancia_total * frequencia_uplink) #distância total calculado

#1.2º Atenuacao na recepcão, por comunicação ser bi direcional, Usar frequencia de downlink na fórmula por ser Rx
AtenEspacoLivreRx_mapa = 32.45 + 20 * math.log10(dAB) + 20 * math.log10(frequencia_downlink)
AtenEspacoLivreRx = 32.45 + 20 * math.log10(distancia_total) + 20 * math.log10(frequencia_downlink) #distância total calculado

# 2º ATENUAÇÃO LÍQUIDA
ganhoTx = int(input('Digite o ganho da antena de transmissão: '))
ganhoRx = int(input('Digite o ganho da antena de recepção: '))

AtenLiquidaMapa = AtenEspacoLivreMapa + A_atmosferica + A_guia_ondas1 + A_guia_ondas2 - (ganhoTx + ganhoRx)
AtenLiquida = AtenEspacoLivre + A_atmosferica + A_guia_ondas1 + A_guia_ondas2 - (ganhoTx + ganhoRx)

#--- ATENUAÇÃO LÍQUIDA Para Transmissao
AtenLiquidaTxMapa = AtenEspacoLivreTx_mapa + A_atmosferica + A_guia_ondas1 + A_guia_ondas2 - (ganhoTx + ganhoRx)
AtenLiquidaTx = AtenEspacoLivreTx + A_atmosferica + A_guia_ondas1 + A_guia_ondas2 - (ganhoTx + ganhoRx)

#--- ATENUAÇÃO LÍQUIDA Para Recepção
AtenLiquidaRxMapa = AtenEspacoLivreRx_mapa + A_atmosferica + A_guia_ondas1 + A_guia_ondas2 - (ganhoTx + ganhoRx)
AtenLiquidaRx = AtenEspacoLivreRx + A_atmosferica + A_guia_ondas1 + A_guia_ondas2 - (ganhoTx + ganhoRx)

#-------------------- IMPRIMINDO DADOS ---------------------------------------------------
#print(' --------------- Latitudes e Longitudes -------------------')
print()
print('=========================================================')
print('Latitude Estação A (',nomeEstacaoA,') = ', latA)
print('Longitude para Estação A (',nomeEstacaoA,') = ', longA)
print()
print('Latitude para Estação B (',nomeEstacaoB,') = ', latB)
print('Longitude para Estação B (',nomeEstacaoB,') = ', longB)
print()
print('Latitude do ponto crítico = ', latPontoCritico)
print('Longitude do ponto crítico = ', longPontoCritico)
print('=========================================================')
print()

print('=========================================================')
print('Altura das estações em relação ao nível do mar')
print('Altitude ',nomeEstacaoA,'  em relação ao nivel do mar da Estacao A', altitudeMarA)
print('Altitude ',nomeEstacaoB,' em relação ao nivel do mar da Estacao A', altitudeMarB)
print('Altitude do Ponto crítico em relação ao nivel do mar da Estacao A', AltitudePontoCritico)
print('=========================================================')

print()
print('=========================================================')
print('Distância calculado entre ',nomeEstacaoA,' e ',nomeEstacaoB,' = ', distancia_total,'km')
print('Distância no mapa entre ',nomeEstacaoA,' e ',nomeEstacaoB,' = ', dAB,'km')
print()
print('Azimute ',Azimute_eixo_x,'º')
print('Angulo de elevação ',Azimute_eixo_y,'º')
print()
print('=========================================================')

#----------- Cálculo do Raio de Fresnel no ponto crítico a 100% com distâncias do mapa
print('Raio de Fresnel de acordo distâncias retirados do mapa = ', RaioFresnel)
print('Raio de Fresnel de acordo distâncias calculadas = ', RaioFresnel1)

#----------- Cálculo do Raio de Fresnel no ponto crítico a 60%
print('Raio de fresnel a 60% (distâncias no mapa)',RaioFresnel60)
print('Raio de fresnel a 60% (distâncias calculadas)',RaioFresnel60_1)

print('Cálculo do Raio de Fresnel em relação a Distância total no mapa e Frequência de Uplink',RaioFresnel_freq_uplink)
print('Cálculo do Raio de Fresnel em relação a Distância total calculado e Frequência de Uplink',RaioFresnel_freq_uplink1)

print('Cálculo Do Raio Da 1ª Zona De Fresnel',Raio1ZonaFresnel)
print()

print('-------------------- Cálculo do Raio Máximo --------------------------')
print('Cálculo Do Raio Máximo para 8.657',RaioMaximo)
print('Cálculo Do Raio Máximo para 545',RaioMaximo1)

print('Outra forma de calcular raio máximo')
print('Cálculo Do Raio Máximo versão 2',RaioMaximoVersao2)
print()

print('--------Correção equivalente da terra para K=4/3+100% do raio de Fresnel no ponto crítico.----------')
print('Correção equivalente da curvatura da Terra para k=4/3 no ponto crítico (Mapa) = ',Hm)
print('Correção equivalente da curvatura da Terra para k=4/3 no ponto crítico (Calculados) = ',Hm1)

print('Correção propriamente dito, com fresnel (de distâncias) retirados do mapa = ',Hc)
print('Correção equivalente da curvatura da Terra para k=4/3 no ponto crítico (Calculados) = ',Hc1)
print()

print('===================================================================')
print(' ------------ ALTURA DAS ANTENAS DE TRANSMISSÃO E RECEPÇÃO -----------------------')
print('Altura previsto da antena (Distancias do mapa)',AlturaAntena,'m')
print('Altura previsto da antena (Distancias calculadas)',AlturaAntena1,'m')
print()

print('Altura máxima prevista da antena (Distancias do mapa)',AlturaMaximaAntena,'m')
print('Altura máxima prevista da antena (Distancias calculadas)',AlturaMaximaAntena1,'m')
print()

print('Altura previsto da antena considerando raio de fresnel (Distancias do mapa)',AlturaAntenaConsiderado,'m')
print('Altura previsto da antena considerando raio de fresnel (Distancias calculadas)',AlturaAntenaConsiderado1,'m')
print()

print('------------ ALTURA DA ANTENAS DE RECEPÇÃO -----------------------')
print('Altura da antena em',nomeEstacaoB,' = ',alturaAntenaB,'m')
print('Altura Mínima da Antena de Recepção (com 60% Raio de Fresnel e Kmin) no ',nomeEstacaoB,'=',alturaAntenaMinima,'m')
print('Altura da Antena de Recepção com 60% Raio de Fresnel e Kmin no ',nomeEstacaoB,' = ',alturaAntenaMinima60,'m')

print()
print('=========================================================')
print('CÁLCULO DAS ATENUAÇÕES')
print('=========================================================')
print('Atenuações no espaço livre em dB (dados do mapa)', AtenEspacoLivreMapa)
print('Atenuações no espaço livre em dB ', AtenEspacoLivre)

print('Atenuacão na transmissão em dB (dados do mapa)', AtenEspacoLivreTx_mapa)
print('Atenuacão na transmissão em dB ', AtenEspacoLivreTx)

print('Atenuacão na recepção em dB (dados do mapa)', AtenEspacoLivreRx_mapa)
print('Atenuacão na recepção em dB ', AtenEspacoLivreRx)
print()
print('--------------------------------------------------------------')
print('Atenuação Líquida (dados do mapa)', AtenLiquidaMapa)
print('Atenuação Líquida ', AtenLiquida)
print()
print('Atenuação Líquida Para Transmissão (dados do mapa)', AtenLiquidaTxMapa)
print('Atenuação Líquida Para Transmissão', AtenLiquidaTx)

print('Atenuação Líquida Para Recepção (dados do mapa)', AtenLiquidaRxMapa)
print('Atenuação Líquida Para Recepção', AtenLiquidaRx)
