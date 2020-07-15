""" Esse script remove os 00 na frente do '00PExxxx' para colocar no final do codigo """
#script Broca_geral

import os
import time

while(True):
    try:
        arqEntrada = ''.join(os.listdir('roteiro_afina/'))
        with open(f'roteiro_afina/{arqEntrada}', encoding="latin-1", errors='ignore') as f:
            read_data = f.readlines()
            print("Arquivo sendo Executado!")
            saida = []
            for i in read_data:
                if i[2:4] == 'PE':
                    saida.append(i[2:68]+'00'+i[68:])
                else:
                    saida.append(i)
            with open(f"tofloripa/{arqEntrada}", "w") as arqSaida:
                arqSaida.write(''.join(saida))
            os.remove(f'roteiro_afina/{arqEntrada}')
            print("Arquivo Finalizado!")
    except:
        print("Arquivo não Encontrado!")

    time.sleep(5)