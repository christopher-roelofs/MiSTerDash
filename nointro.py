import xmltodict
import json
doc = None
with open('nes.dat') as fd:
    doc = xmltodict.parse(fd.read())

print(json.dumps(doc["datafile"]["game"][0]))