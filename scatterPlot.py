import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width: Izhar Khan Khattak", y="sepal_length: We love learning")
fig.show()