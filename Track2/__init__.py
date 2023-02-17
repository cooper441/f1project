import json
import os

print(os.getcwd())

with open("Silvestone.geojson") as f:
    data = json.load(f)

# for i in range(len(data["features"])):
#     print("Name")

print(data["type"])