#coding: utf-8
#Python 2.7

import csv

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

lista_total = [0]
bairros_total = {"" : 0}
bairros_meses = {}
bairros_perigosos = []
meses = []
legenda = {}


def meses_roubos(dicio):
    lista = []
    for i in dicio.keys():
        lista.append(i)
    return lista


def grafico(dicionario, info):
    fontP = FontProperties()
    fontP.set_size("small")
    marcadores = ["+",".","o","*","p","s","x","D","h"]
    eixo_y = []
    eixo_x = range(1, 9)
    nome_bairro = []
    legendas = []
    
    for i in dicionario.items():
        eixo_y.append(i[1])
        nome_bairro.append(i[0])
        
    for i in nome_bairro:
        legendas.append(info[i[6:]])

    for i in range(len(eixo_x)):
        plt.plot(eixo_x, eixo_y[i], label =legendas[i])
        
    plt.ylabel("numero de roubos")
    plt.xlabel("meses")
    art = []
    lgd = plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2, prop=fontP)
    art.append(lgd)
    plt.savefig("grafico_roubos2015.png", additional_artists=art,
    bbox_inches="tight")


with open("14SerieRouboVeiculo2015.csv", "rb") as arquivo:
    
    leitor = csv.reader(arquivo, delimiter=',')
    
    for i in leitor:
        if "a." in i[2]: 
            if "-" in i[15]:
                continue
            else:
                total = int(i[15])

                if len(lista_total) < 10:
                    lista_total.append(total)
            
                elif total > lista_total[0]:
                    lista_total.append(total)
                    
                    for k in bairros_total.items():
                        if k[1] == lista_total[0]:
                            del bairros_total[k[0]]
                    bairros_total[i[2]] = total
                    lista_total.pop(0)
                    lista_total.sort()
                
        else:
            continue

    perigosos = meses_roubos(bairros_total)
    arquivo.seek(0)
    for i in leitor:
        if i[2] in perigosos:
            for k in range(3, 11):
                if "-" in i[k]:
                    continue
                else:
                    meses.append(int(i[k]))
            bairros_meses[i[2]] = meses
            meses = []


for i in bairros_total.keys():
    legenda[i[6:]] = "{0}, Total de roubos {1}".format(i[6:], bairros_total[i])

grafico(bairros_meses, legenda)
