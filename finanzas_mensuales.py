

def finanzasPersonales(mes):
    patrimonio_total = []
    gastos_mensuales = []

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

    # sueldo_mensual("julio",0,10,0,0,6400,0)

    # sueldo_mensual("agosto",0,10,0,0,6400,0)

    # sueldo_mensual("septiembre",0,10,0,0,6400,0)

    # sueldo_mensual("octubre",0,10,0,0,6400,0)

    # sueldo_mensual("noviembre",0,10,0,0,6400,0)

    # sueldo_mensual("diciembre",0,10,0,0,6400,0)


    def gastos(mes):
        comida = 5000
        vicios = 3000
        gastos_totales_mensuales = comida + vicios
        gastos_mensuales.append(gastos_totales_mensuales)
        print(f"gastos extra acumulados al mes de {mes}: {sum(gastos_mensuales)} pesos")

    gastos("junio")
    # gastos("julio")
    # gastos("agosto")


    def calculo_patrimonio_total ():
            
            print(f"patrimonio neto total {mes}: {sum(patrimonio_total)}")
            print(f"patrimonio despues del gastos extra del mes de {mes}: {sum(patrimonio_total) - sum(gastos_mensuales)}")

    calculo_patrimonio_total()


finanzasPersonales("junio")


