from classs import Arvore

arvore = Arvore()

while True:
    print("\n|============================================|")
    option = int(input("   Escolha uma opção:\n "
                       "\n   (1) Inserir livro "
                       "\n   (2) Buscar livro por titulo "
                       "\n   (3) Buscar livros por ano "
                       "\n   (4) Remover livro "
                       "\n   (5) Listar livros em ordem alfabética "
                       "\n   (6) Altura da arvore "
                       "\n   (7) Sair do programa \n|============================================|\n"
                       "\nSua Escolha : "))
    if option==1:
        while True:
            try:
                #titulo,ano = map(str, input("Titulo e ano: ").split())
                #ano = int(ano)
                titulo = input("\nTitulo: ")
                ano = int(input("Ano: "))
                # Supor que cada titulo é unico
                if arvore.buscar_titulo(arvore._arvore,titulo.lower())!=None:
                    print("Esse livro já está catalogado")
                else:
                    print("Inserido.")
                    arvore.inserir(ano,titulo.lower())

                inserirNovamente = input("\nDeseja inserir outro livro [sim/não]? ")

                if (inserirNovamente.lower() != "sim"):
                    break
            except:
                print("Processo de inclussão finalizada............\n")
                break
    elif option==2:
        buscando_t = arvore.buscar_titulo(arvore._arvore,input("Nome do titulo que desejas fazer a procura: "))
        if buscando_t!=None:
            print(buscando_t)
        else:
            print("\n||............Esse livro não está catalogado............||")
    elif option==3:
        buscando_a = arvore.busca_ano(arvore._arvore,int(input("Ano que desejas fazer a procura: ")))
        print("\n||........................||\n    Procura finalizada!\n||........................||")
    elif option==4:
        removendo = arvore.remover(arvore._arvore,input("Titulo a ser removido: "),0)
        if removendo ==None:
            print("||............Remoção concluida............||")
    elif option==5:
        listar = (arvore.lista(arvore._arvore,[]))
        listar.sort(reverse=False)
        print("||...........Lista de livros em ordem alfabetica:",listar)
    elif option==6:
        print("||............Resultado:",arvore.altura(arvore._arvore,-1))
    elif option==7:
        break

print("\n(͡° ͜ʖ ͡°) Programa finalizado com sucesso (͡° ͜ʖ ͡°)")