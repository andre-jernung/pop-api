import csv
import json

with open('testdata.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    jsondicts = {}
    index = -1

    for line in data:
        index = index + 1
        newdict = {}
        newdict["id"] = line[0]
        newdict["name"] = line[1]
        newdict["account"] = line[2]
        newdict["org"] = line[3]
        jsondicts.update({index: newdict})
    
    with open("testdata.json", "w") as outfile:
        json.dump(jsondicts, outfile, indent=2)
        