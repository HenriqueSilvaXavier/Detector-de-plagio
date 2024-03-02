n1=input("Digite a primeira frase: ").lower().split()
n2=input("Digite a segunda frase: ").lower().split()
f=[]
lista=n2[:]
if len(n1)>=len(n2):
	n1, n2=n2[:], n1[:]
print(n1, n2)
for k in n1:
	if k in lista:
		f.append(k)
		lista.remove(k)
a=n1+n2
for n in f:
	a.remove(n)
b=n1
x=0
c=0
y=0
lista=[]
while x<=len(a)-1 or y<=len(b)-1:
	while x<=len(a)-1 and a[x]!=b[y] or y<=len(b)-1 and a[x]!=b[y]:
		if x<len(a)-1:
			x=x+1
		if x>=len(a)-1 and y<len(b)-1:
			y=y+1
	if x==len(a) and y==len(b):
		break
	if a[x]==b[y]:
		c=c+1
	if x<len(a)-1 and y<len(b)-1:
		x=x+1
		y=y+1
	elif y<len(b)-1:
		y=y+1
	elif x==len(a)-1 and y==len(b)-1:
		x=x+1
		y=y+1
porcentagem=c/len(a)
print("As frases tem {}% de plágio".format(porcentagem*100))