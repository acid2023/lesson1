_dict = {"city" : "Moscow", "temperature" : "20"}
print(_dict["city"])
_dict["temperature"]=str(int(_dict["temperature"])-5)
print(_dict)
print(_dict.get("country", "Россия"))
print(len(_dict))
_dict["дата"]="27.05.2019"
print(len(_dict))