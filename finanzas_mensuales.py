

def finanzasPersonales():
    patrimonio_total = []
    

    # DINERO MODERACION

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

        print(f"moderacion {mes}:  {paga_moderacion_mensual}")
        patrimonio_total.append(paga_moderacion_mensual)


    # print(f"{patrimonio_total}")

# INGRESOS EXTRA

        
        progresar = progresar
        ife = ife
        ingresos_extra_total = progresar + ife
        print(f"ingresos extra {mes}: {ingresos_extra_total}")
        patrimonio_total.append(ingresos_extra_total)

        print(f"SUELDO MENSUAL {mes}: {paga_moderacion_mensual + ingresos_extra_total}")

# EJECUCION DEL CODIGO

    

    sueldo_mensual("mayo",cantidad_dias_3_horas_y_media=1, cantidad_dias_4_horas=6, cantidad_dias_4_horas_y_media=5, cantidad_dias_8_horas=0,progresar=12840, ife= 9000 )
    

    sueldo_mensual("junio",0, 10, 0, 0, 6400,9000)

    sueldo_mensual("julio",0,10,0,0,6400,0)
    

        

    def calculo_patrimonio_total ():
        
        print(f"el patrimonio neto total para el mes de julio es de {sum(patrimonio_total)}")

    calculo_patrimonio_total()




finanzasPersonales()
