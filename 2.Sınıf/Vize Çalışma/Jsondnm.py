
import json

person='{"name":"elif","surname":"muradiye","age":"19"}'

convert=json.loads(person)
print(convert["name"])
print(convert["surname"])
print(convert["age"])

with open ("kayit.json") as gozde:
    convert=json.load(gozde)
    print("""
        Meslek={}
        Okul={}
        Diller={} 
    """.format(convert["meslek"],convert["okul"],convert["diller"]))