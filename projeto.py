# algoritmo 6.2
def eliminacao_gauss_pivotamento_parcial(A,b):
    '''recebe uma matriz A nxn e uma matriz b nx1, monta uma matriz aumentada nx(n+1),
    que representa um sistema linear, e devolve as solucoes x1,x2,...,xn,
    ou imprime "nao ha solucao unica", caso ou nao haja solucao, ou sejam infinitas
    '''
    mensagem = "o sistema linear tem solucao nao unica"
    # funcao auxiliar
    def copia_matriz(velha):
        nova = []
        for i in range(len(velha)):
            nova_linha = []
            for elemento in velha[i]:
                nova_linha.append(elemento)
            nova.append(nova_linha)
        return nova
    
    # funcao auxiliar
    def imprime_matriz(matriz): 
        for linha in matriz:
            print(linha)
        print('\n')
    
    # funcao auxiliar
    def monta_matriz_aumentada(A,b):
        matriz_aumentada = copia_matriz(A)
        for i in range(len(A)):
            matriz_aumentada[i].append(b[0][i])
    
        return matriz_aumentada
    
    # aqui comeca de fato o algoritmo 
    matriz_aumentada = monta_matriz_aumentada(A,b)
    
    print('Matrizes lidas:\n')
    imprime_matriz(A)
    imprime_matriz(b)
    
    print('Montamos a matriz aumentada a partir de A e b:\n')
    imprime_matriz(matriz_aumentada)
    
    # linhas, colunas = n+1 
    n = len(matriz_aumentada)
    
    # vamos pular o step 1, pois cursores sao desnecessarios
    
    # step 2
    for i in range(n-1): 
        # step 3
        # valor impossivel
        p = -1
        # para pegar o maior de uma sequencia de valores,
        # vamos iniciar considerando que o primeiro e o maior
        # e conforme percorremos a sequencia, atualizamos esse valor
        maior = matriz_aumentada[i][i]
        # colocamos i+1 por pela conforma como estamos capturando o maior valor
        for p_aux in range (i+1,n):
            # esta condicao nao garante que pegaremos o maior, o que sera explicado
            if abs(matriz_aumentada[p_aux][i]) > abs(maior):
                maior = matriz_aumentada[p_aux][i]
                p = p_aux
            
        # step 4
        # p == -1 significa que nenhum elemento da coluna era maior em modulo que o anterior
        # em outras palavras, ou todos sao nulos, ou o o elemento da diagonal principal era o maior
        if p == -1:
            # vamos verificar o segundo caso
            # caso ele nao seja nulo, ele sera o maior da coluna
            if maior != 0:
                p = i
            else:
                imprime_matriz(matriz_aumentada)
                #return "saiu step 4"
                return mensagem
        # step 5
        if p != i: 
            linha_aux = matriz_aumentada[i]
            matriz_aumentada[i] = matriz_aumentada[p]
            matriz_aumentada[p] = linha_aux
            
            print('Troca de linha:\n')
            imprime_matriz(matriz_aumentada)
            
        # step 6
        for j in range(i+1,n):
            # step 7
            escalar = matriz_aumentada[j][i]/matriz_aumentada[i][i] 
            # step 8
            matriz_aumentada[j] = [matriz_aumentada[j][k] - escalar*matriz_aumentada[i][k] 
                                   for k in range(n+1)]
            
            print('Atualizando:\n')
            imprime_matriz(matriz_aumentada)
    # step 9
    if matriz_aumentada[n-1][n-1] == 0:
        imprime_matriz(matriz_aumentada)
        #return "saiu step 7"
        return mensagem
    
    print('Matriz escalonada:\n')
    imprime_matriz(matriz_aumentada)
    
    # iniciando conjunto solucao
    X = [0]*n 
    
    # step 10
    ultima_solucao = matriz_aumentada[n-1][n]/matriz_aumentada[n-1][n-1] # step 8
    # adicionando a solucao na posicao correta
    X[n-1] = ultima_solucao
    # step 11
    for i in range(n-2,-1,-1):
        # apenas certificando que trabalharemos com float
        somatoria = 0.0
        for j in range(i+1,n):
            somatoria = somatoria + matriz_aumentada[i][j]*X[j]
        X[i] = (matriz_aumentada[i][n] - somatoria)/matriz_aumentada[i][i]
        
    solucoes = []
    solucoes.append(X)
    
    print('Solucao:\n')
    imprime_matriz(transpoe(solucoes))
    print('-------------------------------------------')
    
    # step 12
    return solucoes

def eliminacao_gauss_pivotamento_parcial_sem_passos(A,b):
    '''funcionamento igual a funcao eliminacao_gauss_pivotamento_parcial,
    porem nao exibe os passos intermediarios para nao poluir a visualizacao
    no terminal 
    '''
    mensagem = "o sistema linear tem solucao nao unica"
  
    matriz_aumentada = monta_matriz_aumentada(A,b)
    
    print("Passos intermediarios nao serao exibidos\n")
    print('Matrizes geradas:\n')
    imprime_matriz(A)
    imprime_matriz(b)
    
    # linhas, colunas = n+1 
    n = len(matriz_aumentada)
    
    # vamos pular o step 1, pois cursores sao desnecessarios
    
    # step 2
    for i in range(n-1): 
        # step 3
        # valor impossivel
        p = -1
        # para pegar o maior de uma sequencia de valores,
        # vamos iniciar considerando que o primeiro e o maior
        # e conforme percorremos a sequencia, atualizamos esse valor
        maior = matriz_aumentada[i][i]
        # colocamos i+1 por pela conforma como estamos capturando o maior valor
        for p_aux in range (i+1,n):
            # esta condicao nao garante que pegaremos o maior, o que sera explicado
            if abs(matriz_aumentada[p_aux][i]) > abs(maior):
                maior = matriz_aumentada[p_aux][i]
                p = p_aux
            
        # step 4
        # p == -1 significa que nenhum elemento da coluna era maior em modulo que o anterior
        # em outras palavras, ou todos sao nulos, ou o o elemento da diagonal principal era o maior
        if p == -1:
            # vamos verificar o segundo caso
            # caso ele nao seja nulo, ele sera o maior da coluna
            if maior != 0:
                p = i
            else:
                imprime_matriz(matriz_aumentada)
                #return "saiu step 4"
                return mensagem
        # step 5
        if p != i: 
            linha_aux = matriz_aumentada[i]
            matriz_aumentada[i] = matriz_aumentada[p]
            matriz_aumentada[p] = linha_aux
            
        # step 6
        for j in range(i+1,n):
            # step 7
            escalar = matriz_aumentada[j][i]/matriz_aumentada[i][i] 
            # step 8
            # substituimos a linha j por uma nova linha, a principio vazia
            # vamos preencher essa nova linha com os elemento fazendo
            # uma operacao elementar termo a termo, ate a ultima coluna da matriz aumentada
            # por isso vamos até n+1, ou seja, ate a coluna n, onde ficam os valores da matriz coluna b
            matriz_aumentada[j] = [matriz_aumentada[j][k] - escalar*matriz_aumentada[i][k] 
                                   for k in range(n+1)]
    # step 9
    if matriz_aumentada[n-1][n-1] == 0:
        imprime_matriz(matriz_aumentada)
        #return "saiu step 7"
        return mensagem
    
    # iniciando conjunto solucao
    X = [0]*n 
    
    # step 10
    ultima_solucao = matriz_aumentada[n-1][n]/matriz_aumentada[n-1][n-1] # step 8
    # adicionando a solucao na posicao correta
    X[n-1] = ultima_solucao
    # step 11
    for i in range(n-2,-1,-1):
        # apenas certificando que trabalharemos com float
        somatoria = 0.0
        for j in range(i+1,n):
            somatoria = somatoria + matriz_aumentada[i][j]*X[j]
        X[i] = (matriz_aumentada[i][n] - somatoria)/matriz_aumentada[i][i]
        
    solucoes = []
    solucoes.append(X)
    
    print('Solucao:\n')
    imprime_matriz(transpoe(solucoes))
    print('-------------------------------------------')
    
    # step 12
    return solucoes

# funcoes auxiliares

# f1
def copia_matriz(velha):
        nova = []
        for i in range(len(velha)):
            nova_linha = []
            for elemento in velha[i]:
                nova_linha.append(elemento)
            nova.append(nova_linha)
        return nova
# f2
def transpoe(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    transposta = [[0]*linhas for _ in range(colunas)]

    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = matriz[i][j]
    return transposta
# f3
def imprime_matriz(matriz): 
    for linha in matriz:
        print(linha)
    print('\n')
# f4
def monta_matriz_aumentada(A,b):
    matriz_aumentada = copia_matriz(A)
    for i in range(len(A)):
        matriz_aumentada[i].append(b[0][i])

    return matriz_aumentada
# f5
def gerar_linha_pseudo_aleatoria(n, min_1, max_1, min_2, max_2, semente):
    import random
    random.seed(semente)
    linha = [0.0]*n
    for i in range(n):
        fator_aleatoriedade_valor = random.uniform(0,1)
        fator_aleatoriedade_sinal = random.uniform(0,1)
        if fator_aleatoriedade_valor < 0.5:
                elemento = random.uniform(min_1, max_1)
        else:
            elemento = random.uniform(min_2, max_2)
        if fator_aleatoriedade_sinal < 0.5:
             linha[i] = (-1)*elemento
        else:
             linha[i] = elemento
    return linha
# f6
def cria_sistema_pseudo_aleatorio(n, min_1, max_1, min_2, max_2, semente):
    A = [[]]*n
    for i in range(n):
         # "semente + i" porque queremos que as linhas sejam distintas
         # apenas: "semente" cria uma matriz com linhas iguais
         A[i] = gerar_linha_pseudo_aleatoria(n, min_1, max_1, min_2, max_2, semente+i)
    b = [[]]
    b[0] = gerar_linha_pseudo_aleatoria(n, min_1, max_1, min_2, max_2, semente)

    return A,b
# f7
def ler_matrizes(nome_arquivo):
    from csv import reader
    with open(nome_arquivo, 'r') as arquivo:
        linhas_arquivo = list(reader(arquivo))
        A = [list(map(float, linha)) for linha in linhas_arquivo[:-1]]
        b = [list(map(float, linhas_arquivo[-1]))]
    return A,b

# ----------------------------------------------------------

def problema_1():
    # leitura
    A_pef, b_pef = ler_matrizes("pecaPlanaS.csv")

    # algoritmo implementado
    sol_pef = eliminacao_gauss_pivotamento_parcial(A_pef,b_pef)

    # algoritmo scipy
    import numpy as np
    from scipy.linalg import solve 

    A_pef_scipy = np.array(A_pef)
    b_pef_scipy = np.array(b_pef)

    sol_pef_scipy= solve(A_pef_scipy, b_pef_scipy.T)

    # solucao  
    print("Problema 1 - Solucao algoritmo:")
    imprime_matriz(transpoe(sol_pef))
    # verificacao
    print(f"Solucao scipy:\n{sol_pef_scipy}\n")

def problema_2():
    # leitura
    A_pef, b_pef = ler_matrizes("trelicaPlanaIsos.csv")

    # algoritmo implementado
    sol_pef = eliminacao_gauss_pivotamento_parcial(A_pef,b_pef)

    # algoritmo scipy
    import numpy as np
    from scipy.linalg import solve 

    A_pef_scipy = np.array(A_pef)
    b_pef_scipy = np.array(b_pef)

    sol_pef_scipy= solve(A_pef_scipy, b_pef_scipy.T)

    # solucao  
    print("Problema 1 - Solucao algoritmo:")
    imprime_matriz(transpoe(sol_pef))
    # verificacao
    print(f"Solucao scipy:\n{sol_pef_scipy}\n")

problema_1()
problema_2()




