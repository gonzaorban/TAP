p, r = map(int, input().split())

lista_gold = []
lista_opciones = []

for i in range(r): 
    gold_ronda = list(map(int, input().split()))
    opciones_ronda = list(map(int, input().split()))
    lista_gold.extend(gold_ronda)  
    lista_opciones.extend(opciones_ronda)  
# Inicializar
lista_final = [0] * (p + 1)

# cada ronda
for x in range(r):
    oro_para_compartir = lista_gold[2*x]   
    oro_robar = lista_gold[2*x + 1]         
    

    decisiones_ronda = lista_opciones[x*p:(x*p)+p]
    compartidores = decisiones_ronda.count(1)
    
    if compartidores > 0:
        oro_compartido = oro_para_compartir // compartidores
        oro_si_compartido = oro_para_compartir // (compartidores + 1)
    else:
        oro_compartido = 0  
        oro_si_compartido = oro_para_compartir  
    
    # Ines
    if oro_si_compartido >= oro_robar: 
        oro_ines = oro_para_compartir // (compartidores + 1)
        oro_compartir = oro_para_compartir // (compartidores + 1)
    else: 
        oro_ines = oro_robar
        if compartidores > 0:
            oro_compartir = oro_para_compartir // compartidores
        else:
            oro_compartir = 0  
    
    lista_final[p] += oro_ines
    for y in range(p): 
        if decisiones_ronda[y] == 1:  
            lista_final[y] += oro_compartir
        else: 
            lista_final[y] += oro_robar 

print(" ".join(map(str, lista_final)))
