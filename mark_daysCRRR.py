import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    marks = []
    daysPresent = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks"]))
            daysPresent.append(float(row["Days Present"]))
    
    return {"x":daysPresent,"y":marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between marks and days present: ", correlation[0,1])

def setup():
    data_path = "marks_days.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()