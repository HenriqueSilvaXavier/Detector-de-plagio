from difflib import SequenceMatcher
frase1=input("Digite a primeira frase: ").strip().lower()
frase2=input("Digite a segunda frase: ").strip().lower()
similaridade=SequenceMatcher(None, frase1, frase2).ratio()
print("O grau de plágio é de {:.2f}%".format(similaridade*100)