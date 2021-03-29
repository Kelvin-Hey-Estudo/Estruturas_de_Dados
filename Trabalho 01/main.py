# 1 … receber a quantidade de provas a serem corrigidas
# 2 … receber as alternativas corretas (que podem ser ‘a’, ‘b’, ‘c’, ‘d’ ou ‘e’)
# 3 … receber as alternativas marcadas por cada um (em ordem)
# 4 … mostrar o código que identifica o aluno
# 5 … mostrar o conceito obtido por ele na referida prova

# ! … A prova possui sempre dez questões, sendo que cada uma vale 1 ponto

#################
### variáveis 
qtdProvas = 0
gabarito = ['a','b','a','a','a','a','a','a','a','a']

#######################
### lendo o arquivo 
arquivo = open("teste1.txt", "r")
linhas = arquivo.readlines()

#############################
### iterando pelo arquivo 
nLinha = 0

for linha in linhas:

    #############################
    ### número da linha atual
    nLinha += 1

    ############################################
    ### removendo o caractere ANSI de escape
    x = linha.replace("\n", "")
    linhaQuebrada = x.split(" ")
    
    ########################################################
    ### executando ações de acordo com o número da linha
    if nLinha == 1:

        #######################################
        ### preenche a quantidade de provas 
        qtdProvas = int(input("Digite a quantidade de provas: "))
    
    elif nLinha == 2:
        
        ##############################
        ### preenchendo o gabarito
        i = 0
        tamanho = len(linhaQuebrada)
        while i < (tamanho):    ##############################
           x = linhaQuebrada[i] ### variável temporária 
           gabarito[i] = x      ### atribuindo ao gabarito
           i += 1


