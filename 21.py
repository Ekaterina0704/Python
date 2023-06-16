"""
вывести все уникальные значения
"""
a= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}] 
result= set()
for item in a:
    result.add(list(item.values())[0])
print(*result)    

for item in data:
    for key in item:
        result.add(item[key])
print(result)