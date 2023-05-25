# Lista ficticia de alunos
alunos = [
#   id      nome    idade
    [1, 'Joao Pedro', 20],
    [2, 'Eduardo', 25],
    [3, 'Pedro', 21],
    [4, 'Renan', 23]
    
]
# print(alunos)
def atualiza_aluno():
    # pega as informacoes do usuario e valida elas
    while True:
        try:
            # remove qualquer espaço em branco antes ou depois do input do usuario:
            id_busca = input('Qual o ID deseja atualizar? ').strip()
            id_busca = int(id_busca) # transforma o input do usuario pra um int
            if id_busca > 0:
                break # se deu tudo certo sai do loop e vai pro for in na lista de alunos
            else:
                print('O ID começa em 1')
        # trata algum eventual erro
        except:
            print('ID deve ser um número inteiro válido maior que 0. Tente novamente')
    
    # pra cada aluno na lista de alunos:
    for aluno in alunos:
        if aluno[0] == id_busca: # se o ID passado pelo usuário for encontrado na lista entra na validação e depois pra atualização
            while True:
                try:
                    # pega os dados do usuario                limpa qualquer espaço em branco
                    novo_nome = input('Qual o novo nome do aluno? ').strip() # input do usuario
                    nova_idade = input(('Qual a nova idade do aluno? ')).strip() # input do usuario
                    nova_idade = int(nova_idade) # converte pra int

                    # checa se os dados são válidos
                    if novo_nome and nova_idade > 0: # se o nome for passado e a idade for positiva:                   
                        break # quebra do loop e vai pra atualização dos dados
                    else:
                        print('Idade não pode ser menor que 0 e nome não pode ficar vazio') 
                        continue # volta pro começo do loop
                except:
                    print('Nome deve conter apenas caracteres válidos e idade deve ser um número inteiro maior que 0') # caso alguma coisa no try der errada, cai aqui e volta pro começo do loop

            # ---- Atualização dos dados do Aluno ----- #            
            aluno[0] = id_busca # atualiza o id do aluno escolhido
            aluno[1] = novo_nome # atualiza o nome do aluno
            aluno[2] = nova_idade # atualiza a idade do aluno
            print('Aluno atualizado com sucesso')
            break # quebra o loop e termina a função
        
        # --- Caso o aluno (ID) não for encontrado
        else:
            print('Aluno não encontrado')
            break


atualiza_aluno() # chama a função pra ser executada
print(alunos) # printa a nova lista de alunos atualizada