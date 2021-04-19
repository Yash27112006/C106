import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    iceCream_sales = []
    temperature = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            iceCream_sales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
    
    return {"x":temperature,"y":iceCream_sales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between temperature and ice-cream sales: ", correlation[0,1])

def setup():
    data_path = "iceCream.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()