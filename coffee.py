import csv
import plotly.express as px
with open('data2.csv', newline = '') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Coffee", y = "sleep")
    fig.show()