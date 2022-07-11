import argparse
import requests
import json
import codecs

def busqueda(rut):
    busquedaPacienteUC(rut)

def busquedaPacienteUC(rut):

    urlSaludUCRoted = 'uggcf://ncvtj.hppuevfghf.py/ntraqnnzohyngbevn-cebq/Cnpvragrf?gvcbVqCnpvragr=EHA&cnvfVqragvsvpnqbe=PY&vqCnpvragr='
    urlSaludUC = codecs.decode(urlSaludUCRoted, 'rot_13')  + rut
    print('  ')
    print('Numero de telefono y email apoximados')
    print('  ')

    page  = requests.get(url=urlSaludUC)
    if page.status_code==200:
        datosJson = json.loads(page.text)
        if datosJson['statusCod'] == 'OK':
            print('Numero telefono aproximado  :', datosJson['listaPacientes'][0]['numeroTelefonoPrincipal'])
            print('Email aproximado            :', datosJson['listaPacientes'][0]['email'])
        else:
            print('Sin resultados')
    else:
        print("  Error en request:", page.status_code)
if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')
