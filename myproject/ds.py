# pre defined
data={"key": "value"}
#dynamic
data["k1"]=100
data[1]=1
data[1]={"key": 1675.25}
data[2]=[1,2,43,4]
data[3]=[{"k":1},{"k": 2}]

# data.clear()
#data.items() list of pair (key, items)
for key_val_pair in data.items():
    print(key_val_pair)
    
print(data.keys())
print(list(data.keys()))
print(data.values())
print(list(data.values()))

data.update({1: "1", 2: "1", 3: "1", "new_key": "vashblk"})
print(data.get(1))
print(data.get(1234)) #if key not exit then return None
print(data[1]) 
# print(data[1234]) #if key not exit then crash 
print(data.pop(1))
print(data.pop(2))
print(data.pop(3))
print('___________________________________') 
print(data.popitem()) # will crash if dictionary is empty
print(data) 


