#with open("C:\MeusProjetos_Python\Capitulo5_Manipula_Arquivos\teste.txt", "r") as arquivo:

with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")