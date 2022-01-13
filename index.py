
#-*- coding: UTF-8 -*-

import ctypes
import json

PPLIB = ctypes.cdll.LoadLibrary('bin/gpinpad-lite3_amd64.dll')

def openConected():
    try:
        resultCode = ctypes.c_int(PPLIB.PP_Open('COM6'.encode('ascii'), True))
        print(resultCode)
    except Exception as e:
        print("Erro ao abrir a conexão", e)

def closeConected():
    inputText = input("Digite uma frase de encerramento (Max 32): ")
    try:
        resultCode = ctypes.c_int(PPLIB.PP_Close(inputText.encode('ascii')))
        print(resultCode)
    except Exception as e:
        print("Erro ao fechar a conexão", e)

def about():
    try:
        resultCode = ctypes.c_int(PPLIB.PP_Abort())
        print(resultCode)
    except Exception as e:
        print("Erro ao abortar operação", e)

def generateQrCode():
    usTimeout = 30
    bLineType = "1"
    sLine = '      Ola Mundo  '
    sQRCode = "QR Code Function Test"
    try:
        resultCode = ctypes.c_int(PPLIB.gertecQRCode(ctypes.c_uint64(usTimeout), ctypes.c_wchar(bLineType), sLine.encode('ascii'), sQRCode.encode('ascii')))
        print(resultCode)
    except Exception as e:
        print("Erro ao gerar o qrCode", e)

def getCPFPinPad():
    """ 1 = DIGITE O DDD """
    """ 2 = REDIGITE O DDD """
    """ 3 = DIGITE O TELEFONE """
    """ 4 = REDIGITE O TELEFONE """
    """ 5 = DIGITE DDD + TELEFONE """
    """ 6 = REDIGITE DDD + TELEFONE """
    """ 7 = DIGITE CPF """
    """ 8 = REDIGITE CPF """
    """ 9 = DIGITE RG """
    """ 10 = REDIGITE RG """
    """ 11 = DIGITE OS 4 ULTIMOS DIGITOS """
    """ 12 = DIGITE CODIGO DE SEGURANÇA """
    """ 13 = DIGITE CNPJ """
    """ 14 = REDIGITE CNPJ """
    """ 15 = DIGITE DDMMAAAA """
    """ 16 = DIGITE DDMMAA """
    """ 17 = DIGITE DDMM """
    """ 18 = DIGITE DD """
    """ 19 = DIGITE MM """
    """ 20 = DIGITE AA """
    """ 21 = DIGITE AAAA """
    """ 22 = DIGITE DATA DE NASCIMENTO DDMMAAAA """
    """ 23 = DIGITE DATA DE NASCIMENTO DDMMAA """
    """ 24 = DIGITE DATA DE NASCIMENTO DDMM """
    """ 25 = DIGITE DATA DE NASCIMENTO DD """
    """ 26 = DIGITE DATA DE NASCIMENTO MM """
    """ 27 = DIGITE DATA DE NASCIMENTO AA """
    """ 28 = DIGITE DATA DE NASCIMENTO AAAA """
    """ 29 = DIGITE IDENTIFICACAO """
    """ 30 = DIGITE CODIGO FIDELIDADE """
    """ 31 = DIGITE NUMERO DA MESA """
    """ 32 = QUANTIDADE DE PESSOAS """ 
    """ 33 = DIGITE A QUANTIDADE """ 
    """ 34 = NÚMERO DA BOMBA """ 
    """ 35 = NÚMERO DA VAGA """ 
    """ 36 = NÚMERO DO GUICHE/CAIXA """ 
    """ 37 = NÚMERO DO GUICHE/CAIXA """ 
    """ 38 = NÚMERO DO GARÇOM """ 
    """ 39 = NOTA DO ATENDIMENTO """ 
    """ 40 = NÚMERO DA NOTA FISCAL """ 
    """ 41 = NÚMERO DA COMANDA """ 
    """ 42 = PLACA DO VEICULO """ 
    """ 43 = DIGITE A QUILOMETRAGEM  """ 
    """ 44 = QUILOMETRAGEM INICIAL  """ 
    """ 45 = QUILOMETRAGEM FINAL  """ 
    """ 46 = DIGITE A PORCENTAGEM  """ 
    """ 47 = PESQUISA DE SATISFACAO 0 A 10  """ 
    """ 48 = AVALIE O ATENDIMENTO 0 A 10  """ 
    """ 49 = DIGITE O TOKEN  """ 
    """ 50 = DIGITE NUMERO DO CARTÃO  """ 
    """ 51 = NÚMERO DE PARCELAS  """ 
    """ 52 = CÓDIGO DO PLANO  """ 
    """ 53 = CÓDIGO DO PRODUTO  """
    """ 54 = ACABOU A PORTA  """  
  
    msgIdx = 34
    minDig = 4
    maxDig = 11
    timeout = 15
    try:
        resultCode = ctypes.c_int(PPLIB.abecsGetClearData(ctypes.c_int16(msgIdx), ctypes.c_uint8(minDig), ctypes.c_uint8(maxDig), ctypes.c_uint8(timeout)))
        print(resultCode)
    except Exception as e:
        print("Erro ao iniciar coleta do CPF", e)


def getResponseCPFPinPad():
    result = ""
    try:
        resultCode = ctypes.c_int(PPLIB.abecsGetClearDataResponse(ctypes.c_wchar_p(result), None))
        print('112',resultCode)
        print('113','falta terminar de implementar isso')
    except Exception as e:
        print("Erro ao pegar os dados do CPF", e)


def handleActivate():
    try:
        resultCode = ctypes.c_int(PPLIB.gertecMF_Activate("", ""))
        print('112',resultCode)
    except Exception as e:
        print("Erro ao ativar pinpad", e)


def handleReadWrite():
    try:
        resultCode = ctypes.c_int(PPLIB.gertecMF_ReadWrite())
        print('112',resultCode)
    except Exception as e:
        print("Erro ao realizar leitura MF pinpad", e)

while True:
    entrada = input("Digite uma opção:\n1 - Abrir Conexão com PinPad \n2 - Fechar Conexão com PinPad \n3 - Cancelar Operação \n4 - Gerar QR code \n5 - Pedir Entrada de Dados \n6 - Consultar Entrada de Dados \n7 - Ativar MF \n8 - Leitura MF\n... ")
    if entrada == ' ':
        break
    try:
        num = int(entrada)
        if num == 1:
            openConected()
        elif num == 2:
            closeConected()
        elif num == 3:
            about()
        elif num == 4:
            generateQrCode()
        elif num == 5:
            getCPFPinPad()
        elif num == 6:
            getResponseCPFPinPad()
        elif num == 7:
            handleActivate()
        elif num == 8:
            handleReadWrite()
    except ValueError:
        print('Dado inválido')

print('FIM')

