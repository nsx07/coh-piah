import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '' or sentencas[-1] == None:
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def frases_palavras(texto):
    '''Essa função recebe um texto e retorne o número de frases e palavras'''
    n_sentencas = separa_sentencas(texto)
    n_frases = []
    for sentenca in n_sentencas:
        n_frases += (separa_frases(sentenca)) * 1
    n_palavras = []
    for frase in n_frases:
        n_palavras += (separa_palavras(frase)) * 1 # multiplica a lista, não acrescente mais indices
    return n_frases,n_palavras

def tamanho_medio_palavra(texto):
    '''Essa função recebe um texto e retorna o tamanho médio da palavra do texto'''
    n_palavras = frases_palavras(texto)[1]
    cont = 0
    for palavra in n_palavras:
        cont += len(palavra)    
    media = cont / len(n_palavras)
    return media

def type_token(texto):
    '''Essa função recebe um texto e retorna a razão Type-Token do texto.'''
    n_palavras = frases_palavras(texto)[1]
    razao = n_palavras_diferentes(n_palavras) / len(n_palavras)
    return razao

def hapax_legomana(texto):
    '''Essa função recebe um texto e retorna a razão Hapax-Legomana do texto.'''
    n_palavras = frases_palavras(texto)[1]
    razao = n_palavras_unicas(n_palavras) / len(n_palavras)    
    return razao

def tamanho_medio_sentenca(texto):
    '''Essa função recebe um texto e retorna o tamanho médio da sentença.'''
    n_sentencas = separa_sentencas(texto)    
    cont = 0
    for sentenca in n_sentencas:
        cont += len(sentenca)
    media = cont / len(n_sentencas)
    return media

def complexidade_sentenca(texto):
    '''Essa função recebe um texto e retorna a complexidade da sentença.'''
    n_sentencas = len(separa_sentencas(texto))
    n_frases = len(frases_palavras(texto)[0])
    razao = (n_frases) / (n_sentencas)
    return razao

def tamanho_medio_frase(texto):
    '''Essa função recebe um texto e retorna o tamanho médio da frase'''
    n_frases = frases_palavras(texto)[0]
    cont = 0
    for palavra in n_frases:
        cont += len(palavra)    
    media = cont / len(n_frases)
    return media
    
def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e devolve a assinatura do texto.'''
    
    tam_medio_palavra = tamanho_medio_palavra(texto)
    type__token = type_token(texto)
    hapax__legomana = hapax_legomana(texto)
    tam_medio_sentenca = tamanho_medio_sentenca(texto)
    complexidade__sentenca = complexidade_sentenca(texto)
    tam_medio_frase = tamanho_medio_frase(texto)
    
    return [tam_medio_palavra,type__token,hapax__legomana,tam_medio_sentenca,complexidade__sentenca,tam_medio_frase]

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    cont = 0
    for i in range(6):
        cont += as_b[i] - as_a[i]
    cont = abs(cont)
    return cont / 6
    
def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        ass = calcula_assinatura(texto)
        assinaturas.append(compara_assinatura(ass,ass_cp))
    menor = assinaturas[0]
    texto_id = 0
    for assinatura in assinaturas:
        if assinatura < menor:
            menor = assinatura
            texto_id = assinaturas.index(assinatura)
    return texto_id+1