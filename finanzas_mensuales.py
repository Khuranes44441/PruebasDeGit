
def finanzasPersonales(mes):
    patrimonio_total = []
    gastos_mensuales = []
    valor_setup_pc = 32707

    print(f"FINANZAS PERSONALES {mes}: ")

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
        # print(f"ingresos extra {mes}: {ingresos_extra_total}")
        patrimonio_total.append(ingresos_extra_total)

        print(f"SUELDO MENSUAL {mes}: {paga_moderacion_mensual + ingresos_extra_total}")


# MESES TRABAJADOS

    sueldo_mensual("mayo",cantidad_dias_3_horas_y_media=1, cantidad_dias_4_horas=6, cantidad_dias_4_horas_y_media=5, cantidad_dias_8_horas=0,progresar=12840, ife= 9000 )
    
    sueldo_mensual("junio",0, 10, 0, 0, 6400,9000)

    sueldo_mensual("julio",0,10,0,0,6400,0)

    sueldo_mensual("agosto",0,10,0,0,6400,0)

    sueldo_mensual("septiembre",0,10,0,0,6400,0)

    sueldo_mensual("octubre",0,10,0,0,6400,0)

    sueldo_mensual("noviembre",0,10,0,0,6400,0)

    sueldo_mensual("diciembre",0,10,0,0,6400,0)

# GASTOS EXTRA MENSUALES

    def gastos_extra_mensuales(mes):
        comida = 5000
        vicios = 3000
        gastos_totales_mensuales = comida + vicios
        gastos_mensuales.append(gastos_totales_mensuales)
        print(f"gastos extra acumulados al mes de {mes}: {sum(gastos_mensuales)} pesos")

    gastos_extra_mensuales("junio")
    gastos_extra_mensuales("julio")
    gastos_extra_mensuales("agosto")
    gastos_extra_mensuales("septiembre")
    gastos_extra_mensuales("octubre")
    gastos_extra_mensuales("noviembre")
    gastos_extra_mensuales("diciembre")
    
    


    def calculo_patrimonio_total ():
            
            # print(f"patrimonio neto total {mes}: {sum(patrimonio_total)}")
            print(f"patrimonio despues del gastos extra del mes de {mes}: {sum(patrimonio_total) - sum(gastos_mensuales)}")

    calculo_patrimonio_total()

    def gasto_unico_setup_pc():
        recursos_para_setup = sum(patrimonio_total) - sum (gastos_mensuales)
        print(f"el patrimonio que me queda en el mes {mes} despues de comprar el setup de la pc es de {recursos_para_setup - valor_setup_pc} pesos ")
    
    gasto_unico_setup_pc()


    def validador_finanzas():
        total = sum(patrimonio_total) - sum(gastos_mensuales) - valor_setup_pc
        print(f"*************************************")
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
        else:
            print("tenes mas de 100000, ya esta rey")
    validador_finanzas()

    

    

finanzasPersonales("diciembre")


