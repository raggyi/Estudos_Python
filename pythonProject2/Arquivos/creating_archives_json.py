import  json
d1={
    "Person1":{
        "name":"Roger",
        "age":25
    },
    "Person2":{
        "name":"Jose",
        "age":12
    }
    }

d1_json = json.dumps(d1,ident=True)
with open('abc.json','w+') as file:
    file.write(d1_json)


