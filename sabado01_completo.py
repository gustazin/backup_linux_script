estoque = {}
opcao = int 
opcao = 0 

while opcao != 3:
    print ("MENU")
    print ("1 - adicionar produto : ")
    print ("2 - Consultar produto: ")
    print ("3 - sair :")
    opcao = int(input("digite uma opção: "))
    if opcao == 1:
        nome_produto = input("digite o nome do produto :")
        print (nome_produto)
        quantidade = int(input("Digite a quantidade :"))
        print (quantidade)
        if nome_produto in estoque:
            estoque[nome_produto] = estoque[nome_produto] + quantidade 
            print ("Quantidade atualizada ! ")
        else:
            estoque[nome_produto] = quantidade
            print("produto adicionado")
    elif opcao ==  2:
        nome_produto = input ("digite o nome do produto para consulta:")
        print (nome_produto)
        if nome_produto in estoque:
            print ("quantidade disponivel: " ,estoque[nome_produto])
        elif nome_produto not in estoque:
            print ("Esse produto não está no estoque, adicione com a opção 1 :")
    elif opcao == 3:
        print ("saindo do sistema...")
    else:
        print ("opcao invalida, tente novamente ! " ) 


    
    

    
     