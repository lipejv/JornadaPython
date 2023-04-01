crime_delator = input()
if crime_delator != "roubo" and crime_delator != "tráfico" and crime_delator != "homicídio":
    print("Crime inválido.")
elif crime_delator == "homicídio":
    crime_delatado = input()
    if crime_delatado == "homicídio" and crime_delator == "homicídio":
        print("Delação concedida.")
    elif crime_delatado == "tráfico" or "roubo":
        valor_roubo_trafico = int(input())
        if crime_delator == "homicídio" and crime_delatado == "tráfico" or "roubo":
            print("Delação rejeitada.")
        else:
            print("Delação concedida.")

elif crime_delator == "tráfico":
    valor_trafico_delator = int(input())
    crime_delatado = input()
    if crime_delatado != "roubo" and crime_delatado != "tráfico" and crime_delatado != "homicídio":
        print("Crime inválido.")
    else:
        if crime_delator == "tráfico" and crime_delatado == "homicídio":
            print("Delação concedida.")

        else:
            valor_crime_delatado = int(input())
            maior_que_delator = valor_crime_delatado/5
            if crime_delator == "tráfico" and crime_delatado == "tráfico" and valor_trafico_delator < maior_que_delator:
                print("Delação concedida.")
            else:
                print("Delação rejeitada.")

elif crime_delator == "roubo":
    valor_roubo = int(input())
    crime_delatado = input()
    if crime_delatado != "roubo" and crime_delatado != "tráfico" and crime_delatado != "homicídio":
        print("Crime inválido.")
    else:
        if crime_delator == "roubo" and crime_delatado == "homicídio":
            print("Delação concedida.")
        else:
            valor_crime_delatado = int(input())
            if crime_delator == "roubo" and crime_delatado == "roubo":
                maior_roubo_delatado = valor_crime_delatado/5
                if maior_roubo_delatado > valor_roubo:
                    print("Delação concedida.")
                else:
                    print("Delação rejeitada.")

            elif crime_delator == "roubo" and crime_delatado == "tráfico":
                maior_que_trafico = valor_crime_delatado/3
                if maior_que_trafico > valor_roubo:
                    print("Delação concedida.")
                else:
                    print("Delação rejeitada.")


