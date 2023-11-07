n=float(input("qual é seu salario"))
if (n<=280):
    porcentual=20
elif(n<=700):
    porcentual= 15
elif (n<=1500):
    porcentual =10
elif (n>1500):
    porcentual=5
print("salario sem ajuste r${}".format(n))
print("porcentual{}".format(porcentual))
porcentual=porcentual/100
aumento=porcentual*n
novosalario= n + aumento
print("aumento {}".format(aumento))
print("novo salario{}".format(novosalario))


