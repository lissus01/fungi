carilla=250000
implante=475000
ortodoncia=800000
op=0
op_cliente=0
total=0
des_auxiliar=0.15
des_administrativo=0.1
des_docente=0.05
total_pago=0
total_pago_final=0
total_cantidad=0
cantidad_c=0
cantidad_i=0
cantidad_o=0
total_carilla=0
total_implante=0
total_ortodoncia=0
while op!=2:
    print("1-Cotizacion")
    print("2-Renunciar / Salir o comenzar nueva cotizacion .")
    while True:
        try:
            op1=int(input("Ingrese su opcion a ingresar : "))
            if op1==1 or op1==2:
                break
            else:
                print("La opcion ingresada esta fuera de rango. ")
        except:
            print("Ingrese su opcion en numeros!")
    if op1==1:
        while True:
            print("-----SERVICIOS------")
            print("1- Carillas Porcelana $250.000")
            print("2-Implantes Dentales $475.000")
            print("3-Ortodoncia Brackets $800.000")
            print("4-Salir")

            while True:
                try:
                    op_tratamiento=int(input("Ingrese la opcion de tratamiento a realizar :"))
                    if op_tratamiento==1 or op_tratamiento==2 or op_tratamiento==3 or op_tratamiento==4:
                        break
                    else:
                        print("La opcion a ingresar esta fuera de rango ")
                except:
                    print("Ingrese numeros en sus opciones !")
            if op_tratamiento==1:
                cantidad_c=int(input("Ingrese la cantidad de tratamiento de carillas a realizar : "))
                total_carilla=cantidad_c*carilla
                total_cantidad=total_cantidad+cantidad_c
            elif op_tratamiento==2:
                cantidad_i=int(input("Ingrese la cantidad de tratamiento de implantes a realizar : "))
                total_implante=cantidad_i*implante
                total_cantidad=total_cantidad+cantidad_i
            elif op_tratamiento==3:
                cantidad_o=int(input("Ingrese la cantidad de tratamiento de ortodoncia a realizar : "))
                total_ortodoncia=cantidad_o*ortodoncia
                total_cantidad=total_cantidad+cantidad_o
            else:
                break
        print("-------TIPO CLIENTE-------")
        print("1-Trabajador Auxiliar.")
        print("2-Trabajador Administrativo.")
        print("3-Trabajador Docente.")
        print("4- Otro.")
        while True:
            try:
                op_cliente=int(input("Ingrese la opcion de cliente/ocupacion que tiene : "))
                if op_cliente==1 or op_cliente==2 or op_cliente==3 or op_cliente==4:
                    break
                else:
                        print("La opcion ingresada esta fuera de rango !")
            except:
                print("Ingrese solo numeros en su opcion !")
        if op_cliente==1:
            total_pago=total_carilla+total_implante+total_ortodoncia
            total_des=total_pago*des_auxiliar
            total_pago_final=total_pago-total_des

        elif op_cliente==2:
            total_pago=total_carilla+total_implante+total_ortodoncia
            total_des=total_pago*des_administrativo
            total_pago_final=total_pago-total_des
        elif op_cliente==3:
            total_pago=total_carilla+total_implante+total_ortodoncia
            total_des=total_pago*des_docente
            total_pago_final=total_pago-total_des
        else:
            total_pago=total_carilla+total_implante+total_ortodoncia
    if op_cliente==1:
       if op_tratamiento!=0:
           print("-----------------")
           print("    Cotizacion:    ")
           print("------------------")
           print(f"---> {cantidad_c} tratamiento(s) Carillas de Porcelana $ {total_carilla}  ")
           print(f"---> {cantidad_i} tratamiento(s) Implantes Dentales $ {total_implante}")
           print(f"---> {cantidad_o} tratamiento(s) Ortodoncia Brackets ${total_ortodoncia}")
           print(f"Subtotal         {total_pago}")
           print(f" Descuento 15%    {total_des}")
           print(f"Total  a pagar   $ {total_pago_final} ")
           cuotas=12
           valor_cuota=total_pago_final/12
           print(f" Son 12 cuotas de {valor_cuota}")
    if op_cliente==2:
        if op_tratamiento!=0:
            print("-----------------")
            print("    Cotizacion:    ")
            print("------------------")
            print(f"---> {cantidad_c} tratamiento(s) Carillas de Porcelana $ {total_carilla}  ")
            print(f"---> {cantidad_i} tratamiento(s) Implantes Dentales $ {total_implante}")
            print(f"---> {cantidad_o} tratamiento(s) Ortodoncia Brackets ${total_ortodoncia}")
            print(f"Subtotal         {total_pago}")
            print(f" Descuento 10%   {total_des}")
            print(f"Total  a pagar   $ {total_pago_final} ")
            cuotas=12
            valor_cuota=total_pago_final/12
            print(f" Son 12 cuotas de {valor_cuota}")
    if op_cliente==3:
        if op_tratamiento!=0:
             print("-----------------")
             print("    Cotizacion:    ")
             print("------------------")
             print(f"---> {cantidad_c} tratamiento(s) Carillas de Porcelana $ {total_carilla}  ")
             print(f"---> {cantidad_i} tratamiento(s) Implantes Dentales $ {total_implante}")
             print(f"---> {cantidad_o} tratamiento(s) Ortodoncia Brackets ${total_ortodoncia}")
             print(f"Subtotal         {total_pago}")
             print(f" Descuento 5%    {total_des}")
             print(f"Total  a pagar   $ {total_pago_final} ")
             cuotas=12
             valor_cuota=total_pago_final/12
             print(f" Son 12 cuotas de {valor_cuota}")
    
    if op_cliente==4:
        if op_tratamiento!=0:
             print("-----------------")
             print("    Cotizacion:    ")
             print("------------------")
             print(f"---> {cantidad_c} tratamiento(s) Carillas de Porcelana $ {total_carilla}  ")
             print(f"---> {cantidad_i} tratamiento(s) Implantes Dentales $ {total_implante}")
             print(f"---> {cantidad_o} tratamiento(s) Ortodoncia Brackets ${total_ortodoncia}")
             print(f"Total  a pagar   $ {total_pago} ")
             cuotas=12
             valor_cuota=total_pago/12
             print(f" Son 12 cuotas de {valor_cuota}")   
    if op1==2:
        print("Saliste 🎈.")
        #para finalizar y retomar las cotizaciones a cero ,la persona debe primero ingresar salir y comenzar nuevamente en su cotizacion
        #con sus nuevos valores ,etc
        
