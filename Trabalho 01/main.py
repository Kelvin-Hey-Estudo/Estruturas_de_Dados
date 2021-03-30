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
matriculas = [1,2,3,4,5,6,7,8,9,0,11,12]

#######################
### lendo o arquivo 
arquivo = open("teste1.txt", "r")
linhas = arquivo.readlines()

nLinha = 0

######################################
### indice do vetor das matriculas 
index = 0

######################################
### indice do vetor das matriculas 
for linha in linhas:

    #############################
    ### número da linha atual
    nLinha += 1
    
    ############################################
    ### removendo o caractere ANSI de escape
    x = linha.replace("\n", "")
    
    #########################
    ### separando a linha
    linhaQuebrada = x.split(" ")
    tamanho = len(linhaQuebrada)

    ########################################################
    ### executando ações de acordo com o número da linha
    if nLinha == 1:

        #######################################
        ### preenche a quantidade de provas 
        qtdProvas = linhaQuebrada
    
    elif nLinha == 2:
        
        ##############################
        ### preenchendo o gabarito
        i = 0
        while i < (tamanho):    ##############################
           x = linhaQuebrada[i] ### variável temporária 
           gabarito[i] = x      ### atribuindo ao gabarito
           i += 1

    elif nLinha > 2: ### itera 12 vezes aqui

        print(linhaQuebrada)

        ##################################
        ### salvando o n° da matrícula
        x = linhaQuebrada[0] ### variável temporária 
        matriculas[index] = x ### atribuindo as matrículas
        index += 1 ### incrementa o indice
        

print("")
print(qtdProvas)
print(gabarito)
print(matriculas)
print(nLinha)
