import csv
import plotly.express as px
import numpy as np 

def getdatasource(datapath):
    icecream = []
    coldrink = []
    with open(datapath) as csvfile:
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            icecream.append(float(row["Marks"]))
            coldrink.append(float(row["Days Present"]))

    return{ "x":icecream, "y":coldrink }

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between marks and attendance is", correlation[0,1])

def setup():
    datapath = "./data.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

setup()