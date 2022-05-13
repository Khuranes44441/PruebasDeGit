
def finanzasPersonales(mes,comida,vicios,gym):
    patrimonio_total = []
    gastos_mensuales = []
    valor_setup_pc = 32707
    sueldoMensual = 0
    sueldo_anual_total = []
    # gastos extras mensuales:
    comidA = comida
    vicioS = vicios
    gyM = gym
    gastos_extra_M = comidA + vicioS + gyM

    print(f"FINANZAS PERSONALES HASTA {mes}: ")
    print("*******************************************************************************************")

    print("CALCULO DE SUELDO MENSUAL")
    print(" ")

    def sueldo_mensual(mes, cantidad_dias_3_horas_y_media, cantidad_dias_4_horas, cantidad_dias_4_horas_y_media, cantidad_dias_8_horas, progresar, ife):

        dias_3_horas_y_media = cantidad_dias_3_horas_y_media
        paga_dias_3_horas_y_media = 1345
        paga0 = dias_3_horas_y_media*paga_dias_3_horas_y_media
        
        dias_4_horas = cantidad_dias_4_horas
        paga_dias_4_horas = 1540
        paga1 = dias_4_horas*paga_dias_4_horas

        dias_4_horas_y_media = cantidad_dias_4_horas_y_media
        paga_dias_4_horas_y_media = 1730
        paga2 = dias_4_horas_y_media*paga_dias_4_horas_y_media

        dias_8_horas = cantidad_dias_8_horas
        paga_dias_8_horas = 3270
        paga3 = dias_8_horas*paga_dias_8_horas

        paga_moderacion_mensual = paga0 + paga1 + paga2 + paga3

        patrimonio_total.append(paga_moderacion_mensual)

# INGRESOS EXTRA

        
        progresar = progresar
        ife = ife
        ingresos_extra_total = progresar + ife
        patrimonio_total.append(ingresos_extra_total)

        print(f"SUELDO MENSUAL {mes}: {paga_moderacion_mensual + ingresos_extra_total}")
        print(f"SUELDO MENSUAL {mes} despues de descontar los gastos extra mensuales: {paga_moderacion_mensual + ingresos_extra_total - gastos_extra_M}")

        sueldoMensual = paga_moderacion_mensual + ingresos_extra_total
        sueldo_anual_total.append(sueldoMensual)




# MESES TRABAJADOS

    sueldo_mensual("mayo",1, 6, 5, 0, 12840, 9000)
    
    sueldo_mensual("junio",0, 10, 0, 0, 6400,9000)

    sueldo_mensual("julio",0,10,0,0,6400,0)

    sueldo_mensual("agosto",0,10,0,0,6400,0)

    sueldo_mensual("septiembre",0,10,0,0,6400,0)

    sueldo_mensual("octubre",0,10,0,0,6400,0)

    sueldo_mensual("noviembre",0,10,0,0,6400,0)

    sueldo_mensual("diciembre",0,10,0,0,6400,0)


    print("*******************************************************************************************")
    print(f"PATRIMONIO TOTAL HASTA {mes}: {sum(sueldo_anual_total)}")
    print("*******************************************************************************************")

# GASTOS EXTRA MENSUALES

    print("CALCULO DE GASTOS EXTRA")
    print("*******************************************************************************************")

    def gastos_extra_mensuales(mes,comida,vicios,gym):
        comida = comida
        vicios = vicios
        gym = gym

        gastos_extra = comida + vicios + gym
        gastos_mensuales.append(gastos_extra)
        print(f"GASTOS EXTRA {mes}: \ncomida = {comidA} \nvicios = {vicioS} \ngym = {gyM}")
        print(" ")


    
    gastos_extra_mensuales("mayo",5000,3000,3200)
    # print(f"gastos extra: \n comida = {comidA} \n vicios = {vicioS} \n gym = {gyM}")
    gastos_extra_mensuales("junio",5000,3000,3200)
    gastos_extra_mensuales("julio",5000,3000,3200)
    gastos_extra_mensuales("agosto",5000,3000,3200)
    gastos_extra_mensuales("septiembre",5000,3000,3200)
    gastos_extra_mensuales("octubre",5000,3000,3200)
    gastos_extra_mensuales("noviembre",5000,3000,3200)
    gastos_extra_mensuales("diciembre",5000,3000,3200)

    print("*******************************************************************************************")
    print(f"gastos extra acumulados al mes de {mes}: {sum(gastos_mensuales)} pesos")
    print("*******************************************************************************************")
    
# PATRIMONIO TOTAL
    
    def calculo_patrimonio_total ():
            print("*******************************************************************************************")
            print(f"patrimonio en {mes} despues de descontar los gastos extras : {sum(patrimonio_total) - sum(gastos_mensuales)}")
            print("*******************************************************************************************")

    calculo_patrimonio_total()

    def gasto_unico_setup_pc():
        recursos_para_setup = sum(patrimonio_total) - sum (gastos_mensuales)
        print(f"patrimonio en {mes} despues de comprar el setup de la pc es de {recursos_para_setup - valor_setup_pc} pesos ")
        print("*******************************************************************************************")
        print(f"TOTAL: {recursos_para_setup - valor_setup_pc}")
    
    gasto_unico_setup_pc()

# VALIDADOR DE FINANZAS

    def validador_finanzas():
        total = sum(patrimonio_total) - sum(gastos_mensuales) - valor_setup_pc
        print("*******************************************************************************************")
        print(f"ESTADO DE MI PATRIMONIO {mes}: ")
        if total <= 0:
            print("te quedaste sin guita papa, TE FELICITO :) ")
        elif total <= 10000:
            print("menos de 10 mil")
        elif total <= 20000:
            print("10 mil 0 mas")
        elif total <= 30000:
            print("20 mil o mas")
        elif total <= 40000:
            print("30 mil o mas")
        elif total <= 50000:
            print("40 mil o mas")
        elif total <= 60000:
            print("50 mil o mas")
        elif total <=70000:
            print("60 mil o mas")
        elif total <= 80000:
            print("70 mil o mas")
        elif total <= 90000:
            print("80 mil o mas")
        elif total <= 100000:
            print("90 mil o mas")
        else:
            print("tenes mas de cien mil rey, vaya tranquilo :) ")

    validador_finanzas()

    

    

finanzasPersonales(mes="diciembre", comida=5000, vicios=3000, gym=3200)
# REALIZAR TODOS LOS CAMBIOS DESDE ACA, NO DESDE ADENTRO DE LA FUNCION!!!
# EJEMPLO: PARAMETRO 2: CANTIDAD DE MESES TRABAJADOS
#          PARAMETRO 3 : CANTIDAD DE MESES GASTO EXTRA


