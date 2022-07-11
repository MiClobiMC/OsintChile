import argparse
import requests
import json
import codecs

def busqueda(rut):
    busquedaPacienteUC(rut)

def busquedaPacienteUC(rut):

    print ("")
    print ("Doxing Chile creado por serohacker")
    print ("")
    print ("Informacion del rut " + rut)