data="from aziznitham@gmail.com Sat Jan 509:14:16 2020"
f=data.find("@")
print(f)
m=data.find(" ", f)
print(m)
host=data[f+1 : m]
print(host)
