s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"

a = s.split(', ')
first_name = a[0].split(':')[1]
last_name = a[1].split(':')[1]
age = a[2].split(':')[1]

print(f"-{first_name} \n-{last_name} \n-{age}")