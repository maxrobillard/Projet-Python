import pandas as pd

def recuperationDataAlcool(type):
    csv = pd.read_csv("data/youth_cont.csv")
    if type == "data":
        return csv
    elif type == "total":
        column = '15-19 years old, current drinkers both sexes (%)'
        RenameFrench = "consommation d'alcool<br> pour les 15-19 ans"
        return column,RenameFrench
    elif type == "man":
        column = '15-19 years old, current males drinkers (%)'
        RenameFrench = "consommation d'alcool<br> pour les hommes 15-19 ans"
        return column,RenameFrench
    elif type == "female":
        column = '15-19 years old, current females drinkers (%)'
        RenameFrench = "consommation d'alcool<br> pour les femmes 15-19 ans"
        return column,RenameFrench
    elif type == "moyenne":
        moyenne = csv.groupby('Continent').mean()
        return moyenne
    elif type == "continent":
        continent = csv.Continent.unique()
        return continent
    else :
        return "veuillez selectionner un type défini"


def recuperationDataAccident(type):
    csv = pd.read_csv("data/jeunes_morts_cont.csv")
    def clear(len,data):
        jm = data
        for i in range(len):
            print("i vaut :",i)
            start1 = 17+(17*i)
            stop1=391+(17*i)
            if i != 11 :
                if i!=15:
                    if i!=27:
                        jm=jm.drop(jm.index[start1:stop1])
                        print(jm[0+(17*i):17+(17*i)])
                        print(0+(17*i),17+(17*i))
                    else :
                        stop1+=-22
                        jm=jm.drop(jm.index[start1:stop1])
                        print(jm[459:476])
                else :
                    stop1+=-189
                    jm=jm.drop(jm.index[start1:stop1])
                    print(jm[255:275])
            else :
                stop1+=-20
                jm=jm.drop(jm.index[start1:stop1])
                print(jm[180:221])

        return jm

    if type == "data":
        return csv
    elif type == "dataClear":
        jm = csv.drop(["Unnamed: 0","Unnamed: 0_x","Unnamed: 0_y","Data type"],axis=1)
        jm2 = jm[jm.Year!=2018]
        jm2 = jm2[jm2.Year!=2017]
        jm2 = jm2[jm2.Country!="Hungary"]
        jm2 = jm2[jm2.Country!="Israel"]
        jm2 = jm2[jm2.Country!="Luxembourg"]
        jm2 = jm2[jm2.Country!="Argentina"]
        jm2 = jm2[jm2.Country!="Colombia"]
        pays = jm2.Country.unique()
        data = clear(len(pays),jm2)
        return data
    elif type == "MapAccident":
        csv = recuperationDataAccident("dataClear")
        column = "Value"
    elif type == "PaysSelect":
        pays = csv.Country.unique()
        return pays
    else :
        return "veuillez selectionner un type défini"

def recuperationDataTolerance(type):
    csv = pd.read_csv("data/tolerance_compl.csv")
    if type == "data":
        return csv
    elif type == "MapTolerance":
        dataSelect = "Legal blood alcohol concentration (BAC) limits for young/novice drivers"
        dataFrench = "Limites légales de concentration <br>d’alcool dans le sang (BAC) pour<br>les jeunes conducteurs/novices"
        return dataSelect, dataFrench
    else :
        return "veuillez selectionner un type défini"
