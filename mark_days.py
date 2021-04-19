import csv
import plotly.express as px
with open('marks_days.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Days Present", y="Marks")
    fig.show() 