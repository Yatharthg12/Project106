import csv
import plotly.express as px
with open('data.csv', newline = '') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Marks", y = "Days Present")
    fig.show()