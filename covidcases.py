import pandas as pd
import plotly.express as px

line1 = pd.read_csv("covidcases.csv")

graph = px.scatter(line1,x="date", y="cases", color="country")
print("Getting the Cases...")
graph.show()
