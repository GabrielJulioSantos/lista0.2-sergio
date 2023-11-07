n1=int(input("qual o preço do produto"))
n2=int(input("qual o preço do produto"))
n3=int(input("qual o preço do produto"))
if n1<n2 and n3:
    print("o valor que esta em conta é {}".format(n1))
elif n2<n1 and n2<n3:
    print("o valor que esta em conta é {}".format(n2))
else:
    print("o valor que esta em conta é {}".format(n3))
    
