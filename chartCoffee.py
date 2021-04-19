import csv
import plotly.express as px
import plotly
print(plotly.__version__)
with open('coffee.csv') as f:
    df = csv.DictReader(f)
     fig = px.scatter(df, x="Coffee", y="sleep")
     fig.show()