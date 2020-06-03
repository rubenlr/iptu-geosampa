import csv
from sqlite3 import Error

import configuracao
import sqlite


def main():
    importar()


def importar():
    anos = configuracao.anosImportacao()

    cursor = sqlite.criaConexao(configuracao.arquivoSqLite3).cursor()

    for ano in anos:
        with open(f'{configuracao.pastaPadrao}/{ano}.csv', "r", encoding="utf-8") as file:

            if configuracao.usarVirgula(ano):
                reader = csv.DictReader(file, delimiter=",")
            else:
                reader = csv.DictReader(file, delimiter=";")

            primeiraLinha = True
            linha = 0

            print(f'ano de {ano}')
            for row in reader:
                if (primeiraLinha):
                    primeiraLinha = False
                    continue

                linha += 1
                print(".", end="")
                sql = ''' INSERT INTO geosampa(numero_do_contribuinte
                                             , ano_do_exercicio
                                             , numero_da_nl
                                             , data_do_cadastramento
                                             , tipo_de_contribuinte_1
                                             , tipo_de_contribuinte_2
                                             , numero_do_condominio
                                             , codlog
                                             , logradouro
                                             , numero
                                             , complemento
                                             , bairro
                                             , referencia
                                             , cep
                                             , quantidade_esquinas_frentes
                                             , fracao_ideal
                                             , area_do_terreno
                                             , area_construida
                                             , area_ocupada
                                             , valor_do_m2_terreno
                                             , valor_do_m2_construcao
                                             , ano_construcao_corrigido
                                             , quantidade_de_pavimentos
                                             , testada_para_calculo
                                             , tipo_de_uso_do_imovel
                                             , tipo_de_padrao_da_construcao
                                             , tipo_de_terreno
                                             , fator_de_obsolecencia
                                             , ano_de_inicio_da_vida_do_contribuinte
                                             , mes_de_inicio_da_vida_do_contribuinte
                                             , fase_do_contribuinte)
                                values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                 '''

                valoresDoImovel = configuracao.rowToInsertValues(row, ano)

                try:
                    cursor.execute(sql, valoresDoImovel)
                except Error as e:
                    print(f"erro:\n{row}\n{valoresDoImovel} \n\n {e}")
                    exit(1)

                # if (linha > 10):
                #    break

            print()
            print(f"Total linhas: {linha}")
            print()


if __name__ == '__main__':
    main()
