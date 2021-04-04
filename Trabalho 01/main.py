#################
### variáveis 
qtdProvas = 0
gabarito = ['a','b','a','a','a','a','a','a','a','a']
matriculas = []
alternativas = [1,2,3,4,5,6,7,8,9,0]

#######################
### lendo o arquivo 
arquivo = open("teste1.txt", "r")
linhas = arquivo.readlines()

######################################
### indice do vetor das matriculas 
nLinha = 0
index = 0

#############################
### iterando pelo arquivo
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
        qtdProvas = linhaQuebrada[0]
        
    elif nLinha == 2:
        
        ##############################
        ### preenchendo o gabarito
        i = 0
        while i < (tamanho):    ##############################
           x = linhaQuebrada[i] ### variável temporária 
           gabarito[i] = x      ### atribuindo ao gabarito
           i += 1

    elif nLinha > 2: ### itera pelo n° de linhas 

        ########################################
        ### itera pelas respostas dos alunos
        j = 1
        for i in range(0, 10):
            #######################################
            ### preenche as resposta dos alunos 
            
            ### mecanismo de segurança... avançado...
            ### pula a linha se estiver vazia(ignora)
            if linhaQuebrada[0] == "":
                break

            alternativas[i] = linhaQuebrada[j]
            j += 1

        ################################
        ### preechendo as matriculas
        matriculas = []
        for i in range(0, int(qtdProvas)):
            matriculas.append(None)

        ##################################
        ### salvando o n° da matrícula
        x = linhaQuebrada[0]  ### variável temporária 
        matriculas[index] = x ### atribuindo as matrículas

        ##########################
        ### calculando a média
        total = 0
        for i in range(0, 10):
            if gabarito[i] == alternativas[i]:
                total += 1
        
        ##############################
        ### exibindo os resultados 

        ### mecanismo de segurança... avançado...
        ### evita que mostre o valor anterior duas vezes
        if linhaQuebrada[0] != "":
            print(matriculas[index], total)

            index += 1 ### incrementa o indice
