'''
'   '   Proposição
'   '   Chama-se proposição
'   '   Chama-se proposição toda oração declarativa
'   '   Chama-se proposição toda oração declarativa que pode ser declarada
'   '   Chama-se proposição toda oração declarativa que pode ser declarada Verdadeira
'   '   Chama-se proposição toda oração declarativa que pode ser declarada ou Falsa
'   '
'   '   se oração ->
'   '   se oração ->    tem sujeito e predicado
'   '   se oração ->    tem sujeito e predicado e è declarativa ->
'   '   se oração ->    tem sujeito e predicado e è declarativa ->      não é (exclamativa ou interrogativa)
'   '   se oração ->    tem sujeito e predicado e è declarativa ->      não é (exclamativa ou interrogativa)    ->  oe é Verdadeira (V) ou é Falsa (F)
'''

V = True
F = False

Proposition_v = V 
Proposition_f = F

'''
    by H.Meneses
        dado a área total de uma circunferência, se tomarmos duas circunferências de raio igual à metade do raio da cincunferência que os circunscreve, qual a probabilidade de tomarmos ao acaso
        um ponto qualquer da circunferência e este ponto está localizado fora da circunferências internas?
        obs* considere 
        Raio Estático.

        C/d = pi
        C   = 2*pi*R
        d   = 2r

        Solution:
            se A a área total da circunferência maior de raio R
            :. A = pi * R^2

            Am = pi * R^2/4

            probabilidade = 2Am/A
            probabliidade = 1/2 ou 0.5  

        mas perceba que incrivel, a probabilidade de está em um deles é 1/3      
'''