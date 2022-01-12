
#-*- coding: UTF-8 -*-

import ctypes

PPLIB = ctypes.cdll.LoadLibrary('bin/gpinpad-lite3_amd64.dll')

def openConected():
    try:
        resultCode = ctypes.c_int(PPLIB.PP_Open('COM6'.encode('ascii'), True))
        print(resultCode)
    except Exception as e:
        print("Erro ao abrir a conexão", e)

def closeConected():
    try:
        resultCode = ctypes.c_int(PPLIB.PP_Close("Fechando Usando Python".encode('ascii')))
        print(resultCode)
    except Exception as e:
        print("Erro ao fechar a conexão", e)

def read():
    try:
        resultCode = ctypes.c_int(PPLIB.gertecMF_ReadWrite())
        print(resultCode)
    except Exception as e:
        print("Erro ao fechar a conexão", e)  

while True:
    entrada = input("Digite uma opção (1-3): ")
    if entrada == ' ':
        break
    try:
        num = int(entrada)
        if num == 1:
            openConected()
        elif num == 2:
            closeConected()
        elif num == 3:
            read()
    except ValueError:
        print('Dado inválido')

print('FIM')

