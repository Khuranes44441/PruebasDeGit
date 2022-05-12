def presupuestoSetup(mes):
    listaPrecios = [7800,4350,3100,15800,1657]
    # 7400 = teclado mecanico
    # 4350 = mouse
    # 3100 = mouse pad xxl
    # 15800 = ram 
    # 1657 = funda para pc
    
    presupuesto = 0
    totalPresupuesto = 78275
    for i in listaPrecios:
        presupuesto = presupuesto + i

    print(f"PRESUPUESTO: ")
    print(f"el presupuesto para todo el setup sin contar la silla y el escritorio es de {presupuesto} pesos argentinos")
    print(f"el presupuesto que me queda en {mes} para la silla y el escritorio es de {totalPresupuesto - presupuesto} pesos argentinos")
    

presupuestoSetup("julio")