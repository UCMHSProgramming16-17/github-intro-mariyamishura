import csv
import requests
import pandas as pd
from bokeh.charts import Bar, output_file, save

#Create the file and set parameters
file = open("level.csv","w")
csv = csv.writer(file,delimiter = ",")
csv.writerow(["id","lvl"])

#write a forloop for the separate groups of pokemon, must be in range from 1-7
for x in range (1,7):
    endpoint = "http://pokeapi.co/api/v2/"
    num = "evolution-chain/"+str(x)+"/"
    url = endpoint+num
    payload = {}
    r = requests.get(url, params=payload)
    print(r)
    d = r.json()
    lvl = d["chain"]["evolves_to"][0]["evolution_details"][0]["min_level"]
    csv.writerow([x, lvl])
file.close()


data = pd.read_csv("level.csv")
#set up the data points for the graph
bar = Bar(data, values="level", label="name", title="Evolution Levels among Pokemon")
output_file("bar.html")
#save the bar graph
save(bar)

    