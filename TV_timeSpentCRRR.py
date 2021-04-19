import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    Size_tv = []
    Time_spent = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            Size_tv.append(float(row["Size of TV"]))
            Time_spent.append(float(row[" Average time"]))
    
    return {"x":Size_tv,"y":Time_spent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Size of TV and Time spent: ", correlation[0,1])

def setup():
    data_path = "TV.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()