import re

anoInicio = 2005
anoFim = 2020
pastaPadrao = 'E:\Temp\IPTU GeoSampa'

arquivoSqLite3 = "E:\Temp\IPTU GeoSampa\IPTU-GeoSampa.sqlite3"

anosComVirgula = [2016]


def anosImportacao():
    anos = []
    for ano in range(anoFim - anoInicio + 1):
        anos.append(anoInicio + ano)
    return anos


def usarVirgula(ano):
    return ano in anosComVirgula


def getTextCol(row, col):
    value = row[col]

    if (value == None or len(value.strip()) == 0):
        return None

    return re.sub(' +', ' ', value.strip())


def getIntCol(row, col):
    return int(row[col])


def toFloat(value):
    if value is not None and len(value) > 0:
        clearValue = value.replace(",", ".")
        return float(clearValue)
    return None


def getFloatCol(row, col):
    value = row[col]

    if value is not None and len(value) > 0:
        clearValue = value.replace(",", ".")
        return float(clearValue)

    return None


def rowToInsertValues(row, ano):
    if ano not in [2016, 2017, 2018, 2019, 2020]:
        return (getTextCol(row, "NUMERO DO CONTRIBUINTE"),
                getTextCol(row, "ANO DO EXERCICIO"),
                getTextCol(row, "NUMERO DA NL"),
                getTextCol(row, "DATA DO CADASTRAMENTO"),
                getTextCol(row, "TIPO DE CONTRIBUINTE 1"),
                getTextCol(row, "TIPO DE CONTRIBUINTE 2"),
                getTextCol(row, "NUMERO DO CONDOMINIO"),
                getTextCol(row, "CODLOG DO IMOVEL"),
                getTextCol(row, "NOME DE LOGRADOURO DO IMOVEL"),
                getTextCol(row, "NUMERO DO IMOVEL"),
                getTextCol(row, "COMPLEMENTO DO IMOVEL"),
                getTextCol(row, "BAIRRO DO IMOVEL"),
                getTextCol(row, "REFERENCIA DO IMOVEL"),
                getTextCol(row, "CEP DO IMOVEL"),
                getIntCol(row, "QUANTIDADE DE ESQUINAS FRENTES"),
                getFloatCol(row, "FRACAO IDEAL"),
                getIntCol(row, "AREA DO TERRENO"),
                getIntCol(row, "AREA CONSTRUIDA"),
                getIntCol(row, "AREA OCUPADA"),
                getFloatCol(row, "VALOR DO M2 DO TERRENO"),
                getFloatCol(row, "VALOR DO M2 DE CONSTRUCAO"),
                getIntCol(row, "ANO DA CONSTRUCAO CORRIGIDO"),
                getIntCol(row, "QUANTIDADE DE PAVIMENTOS"),
                getFloatCol(row, "TESTADA PARA CALCULO"),
                getTextCol(row, "TIPO DE USO DO IMOVEL"),
                getTextCol(row, "TIPO DE PADRAO DA CONSTRUCAO"),
                getTextCol(row, "TIPO DE TERRENO"),
                getFloatCol(row, "FATOR DE OBSOLESCENCIA"),
                getIntCol(row, "ANO DE INICIO DA VIDA DO CONTRIBUINTE"),
                getIntCol(row, "MES DE INICIO DA VIDA DO CONTRIBUINTE"),
                getFloatCol(row, "FASE DO CONTRIBUINTE")
                )
    else:
        return (getTextCol(row, "NUMERO DO CONTRIBUINTE"),
                getTextCol(row, "ANO DO EXERCICIO"),
                getTextCol(row, "NUMERO DA NL"),
                getTextCol(row, "DATA DO CADASTRAMENTO"),
                getTextCol(row, "TIPO DE CONTRIBUINTE 1"),
                getTextCol(row, "TIPO DE CONTRIBUINTE 2"),
                getTextCol(row, "NUMERO DO CONDOMINIO"),
                getTextCol(row, "CODLOG DO IMOVEL"),
                getTextCol(row, "NOME DE LOGRADOURO DO IMOVEL"),
                getTextCol(row, "NUMERO DO IMOVEL"),
                getTextCol(row, "COMPLEMENTO DO IMOVEL"),
                getTextCol(row, "BAIRRO DO IMOVEL"),
                getTextCol(row, "REFERENCIA DO IMOVEL"),
                getTextCol(row, "CEP DO IMOVEL"),
                getIntCol(row, "QUANTIDADE DE ESQUINAS/FRENTES"),
                getFloatCol(row, "FRACAO IDEAL"),
                getIntCol(row, "AREA DO TERRENO"),
                getIntCol(row, "AREA CONSTRUIDA"),
                getIntCol(row, "AREA OCUPADA"),
                getFloatCol(row, "VALOR DO M2 DO TERRENO"),
                getFloatCol(row, "VALOR DO M2 DE CONSTRUCAO"),
                getIntCol(row, "ANO DA CONSTRUCAO CORRIGIDO"),
                getIntCol(row, "QUANTIDADE DE PAVIMENTOS"),
                getFloatCol(row, "TESTADA PARA CALCULO"),
                getTextCol(row, "TIPO DE USO DO IMOVEL"),
                getTextCol(row, "TIPO DE PADRAO DA CONSTRUCAO"),
                getTextCol(row, "TIPO DE TERRENO"),
                getFloatCol(row, "FATOR DE OBSOLESCENCIA"),
                getIntCol(row, "ANO DE INICIO DA VIDA DO CONTRIBUINTE"),
                getIntCol(row, "MES DE INICIO DA VIDA DO CONTRIBUINTE"),
                getFloatCol(row, "FASE DO CONTRIBUINTE")
                )
