n1=int(input("digite um numero"))
n2=int(input("digite um numero"))
n3=int(input("digite um numero"))
if n1>n2 and n3:
    print("o maior numero é {}".format(n1))
elif  n2>n3 and n1:
    print("o maior numero  é{} ".format(n2))
else:
    print("o maior numero é {} ".format(n3))