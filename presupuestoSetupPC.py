def presupuestoSetup(mes):
    listaPrecios = [7800,4350,2450,15800,1657]
    
    presupuesto = 0
    totalPresupuesto = 67800
    for i in listaPrecios:
        presupuesto = presupuesto + i

    
    print(f"el presupuesto para todo el setup sin contar la silla y el escritorio es de {presupuesto} pesos argentinos")
    print(f"el presupuesto que me queda para la silla y el escritorio es de {totalPresupuesto - presupuesto} pesos argentinos")

presupuestoSetup("julio")