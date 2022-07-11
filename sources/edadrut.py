import argparse
import requests
import json
import codecs

def busqueda(rut):
    busquedaPacienteUC(rut)

def busquedaPacienteUC(rut):

    urlroted = 'uggcf://znfgrepuvyrncx.vasb/jf-oveguqnli3/ncv/?ehg='
    url = codecs.decode(urlroted, 'rot_13')  + rut
    print('')
    print('Datos de la persona')
    print('')

    response = requests.get(url)
    response = response .json()
    for item in response:
            print("Nombre                   : " + item['nombre'])
            print("Edad                     : " + item['edad'])
            print("Fecha de nacimiento      : " + item['fecha_nacimiento'])
