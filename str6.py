str = "Это тестовая <start>строка для изучения<end> строковых операций"

start_index = str.find('<start>') + len('<start>')
end_index = str.find('<end>')

diapazon = str[start_index : end_index]

print(diapazon)