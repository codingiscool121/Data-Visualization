import pandas as pd
import plotly.express as px

data1 = pd.read_csv("crash_catalonia.csv")

graph = px.bar(data1, x="Week", y="Number of Crashes", title="Number of Crashes in Catalonia Per Day", color="Number of Crashes")
print("Crashes")
graph.show()
