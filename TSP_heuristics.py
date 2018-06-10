# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 17:10:01 2018

@author: Anselmo

Implement a greedy and a local search heuristics for solving
the traveling salesman problem (TSP).

"""

def mais_proximo(cidades, matriz_dist, cidade_inicial):
    
    cidade_atual = cidade_inicial
    rota = []
    rota.append(cidade_inicial)
    cidades_restantes = list(cidades)
    cidades_restantes.remove(cidade_inicial)
    
    
    while len(cidades_restantes) > 0:
        
        menor_distancia = matriz_dist.sum()
        for cidade in cidades_restantes:
            
            distancia = matriz_dist[cidade_atual, cidade]
            
            if distancia < menor_distancia:
                menor_distancia = distancia
                prox_cidade = cidade
                
        cidade_atual = prox_cidade
        rota.append(cidade_atual)
        cidades_restantes.remove(cidade_atual)
        
    rota.append(cidade_inicial)
    
    return rota
            
            
def comprimento(rota, matriz_dist):
    
    comp_total = 0
    for k in range(len(rota)-1):
        distancia = matriz_dist[rota[k], rota[k+1]]
        comp_total+=distancia
    
    return comp_total
    
    
def busca_local(solucao_inicial, matriz_dist):
    
    solucao_atual = list(solucao_inicial)
    melhor_solucao = solucao_atual
    best_comp = comprimento(solucao_atual, matriz_dist)
    
    flag = True
    while flag:
        flag = False
        for k in range(1, len(solucao_atual)-2):   ##Gera solucoes vizinhas
            
            nova_rota = list(solucao_atual)
            nova_rota[k], nova_rota[k+1] = nova_rota[k+1], nova_rota[k]
            comp_nova_rota = comprimento(nova_rota, matriz_dist)
            
            if comp_nova_rota < best_comp:
                
                melhor_solucao = nova_rota
                best_comp = comp_nova_rota
                flag = True
                
        solucao_atual = melhor_solucao
            
    return melhor_solucao, best_comp

    