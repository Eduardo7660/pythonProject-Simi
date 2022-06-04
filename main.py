import pandas as pd
import PySimpleGUI as sg
import os

#calc Core 4, 6, 8, 10, 12, 14, 16, 18, 24, 32, 64
#calc threads 6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 64, 128
def calc(escolhaT, tabela, maxvalue):
   simiatt = 1-(abs(tabela-escolhaT)/maxvalue)
   return simiatt

def bubbleSort(finalList, coreList, threadsList, nameList, typelist):
  for passnum in range(len(finalList)-1,0,-1):
      for i in range(passnum):
          if finalList[i]<finalList[i+1]:
              #simi final
              temp = finalList[i]
              finalList[i] = finalList[i+1]
              finalList[i+1] = temp
              #core list
              temp = coreList[i]
              coreList[i] = coreList[i + 1]
              coreList[i + 1] = temp
              #threads list
              temp = threadsList[i]
              threadsList[i] = threadsList[i + 1]
              threadsList[i + 1] = temp
              #name List
              temp = nameList[i]
              nameList[i] = nameList[i + 1]
              nameList[i + 1] = temp
              #type List
              temp = typelist[i]
              typelist[i] = typelist[i + 1]
              typelist[i + 1] = temp


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#tela cores,
def cores():
  sg.theme('DarkAmber')  # Cor de fundo

  layout = [[sg.Text("Cores "), sg.Combo([4, 6, 8, 10, 12, 14, 16, 18, 24, 32, 64], default_value=4),
         sg.Text("Peso: "), sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=5)],
        [sg.Text("Digite outro valor para Cores: "), sg.Input(default_text='0'),
         sg.Text("Digite outro valor para Pesos: "), sg.Input(default_text='0')],
        [sg.Button('Ok'), sg.Button('Cancel')]]

# Cria a janela
  window = sg.Window('Núcleos', layout)
# Event Loop to process "events" and get the "values" of the inputs
  while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':  # if user closes window or clicks cancel
          break

  window.close()

  return values

#tela threads
def threads ():
  sg.theme('DarkAmber')

  layout = [[sg.Text("Threads "), sg.Combo([6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 64, 128], default_value=6),
          sg.Text("Peso: "), sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=5)],
          [sg.Text("Digite outro valor para Threads: "), sg.Input(default_text='0'),
          sg.Text("Digite outro valor para Pesos: "), sg.Input(default_text='0')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

  window = sg.Window('Threads', layout)
  while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':  # if user closes window or clicks cancel
          break

  window.close()

  return values

#tela modelo AMD/Intel/Apple
def model():
  sg.theme('DarkAmber')  # Cor de fundo

  layout = [[sg.Combo(["AMD", "Intel", "Apple"], default_value="AMD"),
           sg.Text("Peso: "), sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=3)],
          [sg.Text("Digite outro valor para Pesos: "), sg.Input(default_text='0')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Cria a janela
  window = sg.Window('Modelo', layout)
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':  # if user closes window or clicks cancel
        break

  window.close()

  return values

#tela tipo desktop/laptop
def Type():
 sg.theme('DarkAmber')  # Cor de fundo
 layout = [[sg.Combo(["Desktop", "Notebook"], default_value="Desktop"),
            sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=2)],
           [sg.Text("Digite outro valor para Pesos: "), sg.Input(default_text='0')],
           [sg.Button('Ok'), sg.Button('Cancel')]]
 # Cria a janela
 window = sg.Window('Modelo', layout)
 while True:
     event, values = window.read()
     if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Ok':  # if user closes window or clicks cancel
         break

 window.close()

 return values
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
csv = pd.read_csv("Processadores/CPU.csv")

#le os valores da tabela
threadsList = csv['threads'].values
coreList = csv['cores'].values
modelList = csv['manufacturer'].values
typelist = csv['type'].values
nameList = csv['cpuName'].values



#todo mundo vida lista aqui quero nem saber
coreList = list(coreList)
threadsList = list(threadsList)
modelList = list(modelList)
typelist = list(typelist)
nameList = list(nameList)
print(threadsList, "\n", coreList)

#entradas de valores
modeloL = model()
escolhaTL = threads()
escolhaCL = cores()
escolhaTyL = Type()

Ccola = [4, 6, 8, 10, 12, 14, 16, 18, 24, 32, 64]
Tcola = [6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 64, 128]
letsTry = []

print(escolhaCL, escolhaTL)

#Pega os valores da tela
#threads
if escolhaTL[0] != str:
 escolhaT = escolhaTL.get(0)
else:
 escolhaT = escolhaTL.get(2)

if escolhaTL[3] != str:
 pesoThread = escolhaTL.get(1)
else:
 pesoThread = escolhaTL.get(3)

#cores
if escolhaCL[0] != str:
 escolhaC = escolhaCL.get(0)
else:
 escolhaC = escolhaCL.get(2)

if escolhaCL[3] != str:
 pesoCore = escolhaCL.get(1)
else:
 pesoCore = escolhaCL.get(3)

#modelo
modelo = modeloL.get(0)
if modeloL[2] != str:
 pesoModelo = modeloL.get(2)
else:
 pesoModelo = modeloL.get(1)

#typo
escolhaType = escolhaTyL.get(0)
if escolhaTyL[2] != str:
 pesoType = escolhaTyL.get(2)
else:
 pesoType = escolhaTyL.get(1)

#todo mundo vira inteiro
escolhaT = int(escolhaT)
escolhaC = int(escolhaC)
pesoCore = float(pesoCore)
pesoThread = float(pesoThread)
pesoType = float(pesoType)
pesoModelo = float(pesoModelo)

simiCoreList = []
simiThreadsList = []
#lista de similaridade Core
for i in range(len(coreList)):
  ajudante = calc(coreList[i], escolhaC, 64)
  ajudante = ajudante * pesoCore
  simiCoreList.append(ajudante)

#lista de similaridade Threads
for j in range(len(threadsList)):
  ajudante = calc(threadsList[j], escolhaT, 128)
  ajudante = ajudante * pesoThread
  simiThreadsList.append(ajudante)

print(modelList, "\n", modelo)
simiModelList = []
for k in range(len(modelList)):
   if modelo == "AMD" and modelList[k] == "AMD" or modelo == "Intel" and modelList[k] == "Intel" or modelo == "Apple" and modelList[k] == "Apple":
       ajudante= calc(1, 1, 3)
       ajudante = ajudante * pesoModelo
       simiModelList.append(ajudante)
   elif modelo == "AMD" and modelList[k] != "AMD" or modelo == "Intel" and modelList[k] != "Intel" or modelo == "Apple" and modelList[k] != "Apple":
       ajudante = calc(1, 0.5, 3)
       ajudante = ajudante * pesoModelo
       simiModelList.append(ajudante)



pesoTotal = pesoModelo+pesoCore+pesoThread

#ultima similaridade
finalList = []
for o in range(len(simiThreadsList)):
  ajudante = (simiThreadsList[o] + simiThreadsList[o] + simiModelList[o])/pesoTotal
  finalList.append(ajudante)

print(finalList)

for j in range(len(finalList)):
  finalList[j] = finalList[j] * 100.00



#DataFrame(columns=["Similaridade", "Nome", "Core", "Threads", "Modelo", "Tipo"])
#finalList[i], nameList[i], coreList[i], nameList[i], modelList[i], typelist[i]

bubbleSort(finalList, coreList, threadsList, nameList, typelist)
dataFrame = pd.DataFrame({"Similaridade": finalList, "Nome": nameList, "Core": coreList, "Threads": threadsList, "Modelo": modelList, "Tipo":typelist})
for i in range(len(finalList)):
  if typelist[i] == escolhaType:
      print(finalList[i], coreList[i], threadsList[i], nameList[i], typelist[i], "\n")



print(dataFrame)


