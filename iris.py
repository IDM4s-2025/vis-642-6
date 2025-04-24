
import pandas as pd
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="petal_length", y="petal_width", color="species",
                 size='sepal_length', hover_data=['sepal_width'])
fig.show()
