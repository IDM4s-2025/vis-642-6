import plotly.express as px
import pandas as pd

df = pd.read_csv("Iris.csv")

fig = px.scatter(df, x="SepalWidthCm", y="SepalLengthCm", color="Species")
fig.show()
