nota1 = int(input("digite a primeira nota "))
nota2 = int(input("digite a segunda nota "))
nota3 = int(input("digite a terceira nota "))
nota4 = int(input("digite a quarta nota "))
media = (nota1*1 + nota2*1 + nota3*2 )/4
print(media)
if media > 6 :
 print ("aprovado")
elif media < 5:
 print ("recuperação")
else:
    print ("reprovado")