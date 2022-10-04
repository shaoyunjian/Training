import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:
  data=json.load(response)

areaList = data["result"]["results"]

with open("data.csv", mode="w", encoding="utf-8") as file:
  for area in areaList:
    if int(area["xpostDate"][0:4]) >= 2015:
      file.write(area["stitle"]+","
      +area["address"][5:8]+","
      +area["longitude"]+","
      +area["latitude"]+","
      +"https://"+ area["file"].split("https://")[1]+"\n")