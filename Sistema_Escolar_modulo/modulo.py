import statistics

#moda
def mode_(dados):
    mode = statistics.mode(dados)
    return mode

#media
def mean_(dados):
    media = statistics.mean(dados)
    return media

#desvio padão 
def desvio_(dados):
    desv = statistics.stdev(dados)
    return desv

#menor nota
def menor_n(dados):
    me = min(dados)
    return me

#maior nota
def maior_n(dados):
    ma = max(dados)
    return ma










