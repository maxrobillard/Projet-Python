import pandas as pd
# Création d'une fonction qui traite et renvoi les données nécessaire en fonction des besoins, prend en parametre une string
def recuperationDataAlcool(type):
    csv = pd.read_csv("data/youth_cont.csv",encoding="utf-8")
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

# Création d'une fonction qui traite et renvoi les données nécessaire en fonction des besoins, prend en parametre une string
def recuperationDataAccident(type):
    csv = pd.read_csv("data/jeunes_morts_cont.csv",encoding="utf-8")
    def clear(len,data):
        data = data
        for i in range(len):
            start1 = 17+(17*i)
            stop1=391+(17*i)
            if i != 11 :
                if i!=15:
                    if i!=27:
                        data=data.drop(data.index[start1:stop1])
                        print(data[0+(17*i):17+(17*i)])
                        print(0+(17*i),17+(17*i))
                    else :
                        stop1+=-22
                        data=data.drop(data.index[start1:stop1])
                        print(data[459:476])
                else :
                    stop1+=-189
                    data=data.drop(data.index[start1:stop1])
                    print(data[255:275])
            else :
                stop1+=-20
                data=data.drop(data.index[start1:stop1])
                print(data[180:221])

        return data

    if type == "data":
        return csv
    elif type == "dataClear":
        data = csv.drop(["Unnamed: 0","Unnamed: 0_x","Unnamed: 0_y","Data type"],axis=1)
        data2 = data[data.Year!=2018]
        data2 = data2[data2.Year!=2017]
        data2 = data2[data2.Country!="Hungary"]
        data2 = data2[data2.Country!="Israel"]
        data2 = data2[data2.Country!="Luxembourg"]
        data2 = data2[data2.Country!="Argentina"]
        data2 = data2[data2.Country!="Colombia"]
        pays = data2.Country.unique()
        data = clear(len(pays),data2)
        return data
    elif type == "MapAccident":
        csv = recuperationDataAccident("dataClear")
        column = "Value"
    elif type == "PaysSelect":
        pays = csv.Country.unique()
        return pays
    else :
        return "veuillez selectionner un type défini"

# Création d'une fonction qui traite et renvoi les données nécessaire en fonction des besoins, prend en parametre une string
def recuperationDataTolerance(type):
    csv = pd.read_csv("data/tolerance_compl.csv",encoding="utf-8")
    if type == "data":
        return csv
    elif type == "MapTolerance":
        dataSelect = "Legal blood alcohol concentration (BAC) limits for young/novice drivers"
        dataFrench = "Limites légales de concentration <br>d’alcool dans le sang (BAC) pour<br>les jeunes conducteurs/novices"
        return dataSelect, dataFrench
    else :
        return "veuillez selectionner un type défini"
