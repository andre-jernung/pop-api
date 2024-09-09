import csv
import json

with open('testdata.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    jsondicts = []

    for line in data:
        newdict = {}
        newdict["id"] = line[0]
        newdict["name"] = line[1]
        newdict["account"] = line[2]
        newdict["org"] = line[3]
        jsondicts.append(newdict)
    
    with open("testdata.json", "w") as outfile:
        json.dump(jsondicts, outfile, indent=2)
        