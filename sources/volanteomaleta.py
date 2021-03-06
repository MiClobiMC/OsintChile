import requests
import argparse
import json
from utils import rut as rutUtils
from bs4 import BeautifulSoup

def busqueda(rut):
    busquedaVolanteomaleta(rut)

def busquedaVolanteomaleta(rut):
    params = {'term': rutUtils.formatRut(rut)}

    page = requests.post('https://www.volanteomaleta.com/rut', params=params)
    print('Vehiculos')
    print('')
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        tbody = soup.find('tbody')
        datosTR = tbody.find_all('tr')
        if len(datosTR)>0:
            for tr in datosTR:
                if tr:
                    datosTD = tr.find_all('td')
                    print('RUT                       :', datosTD[4].get_text())
                    print('Patente                   :', datosTD[0].get_text())
                    print('Tipo                      :', datosTD[1].get_text())
                    print('Marca                     :', datosTD[2].get_text())
                    print('Modelo                    :', datosTD[3].get_text())
                    print('Nro. Motor                :', datosTD[5].get_text())
                    print('Año                       :', datosTD[6].get_text())
                    ''' print('Nombre a Rutificador      :', datosTD[7].get_text())   '''
                    print(" ")
                else:
                    print('No tiene vehiculos')
        else:
            print('No tiene vehiculos')
    else:
        print("  Error en request:", page.status_code)   

if __name__ == "__main__":
    print('Esto no se ejecuta solo, es para ser llamado desde el programa principal')