
import sqlite3
from sqlite3 import Error

import configuracao


def criaConexao(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("cria banco de dados erro", e)

    return conn


def criaTabela(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print("criaTabela error", e)


def EnsureDatabaseCreation():
    createTableSQLGeoSampa = """ CREATE TABLE IF NOT EXISTS geosampa (
                                        id integer PRIMARY KEY,
                                        numero_do_contribuinte text,
                                        ano_do_exercicio int,
                                        numero_da_nl text,
                                        data_do_cadastramento text,
                                        tipo_de_contribuinte_1 text,
                                        tipo_de_contribuinte_2 text,
                                        numero_do_condominio text,
                                        codlog text,
                                        logradouro text,
                                        numero text,
                                        complemento text,
                                        bairro text,
                                        referencia text,
                                        cep text,
                                        quantidade_esquinas_frentes integer,
                                        fracao_ideal real,
                                        area_do_terreno integer,
                                        area_construida integer,
                                        area_ocupada integer,
                                        valor_do_m2_terreno real,
                                        valor_do_m2_construcao real,
                                        ano_construcao_corrigido integer,
                                        quantidade_de_pavimentos integer,
                                        testada_para_calculo real,
                                        tipo_de_uso_do_imovel text,
                                        tipo_de_padrao_da_construcao text,
                                        tipo_de_terreno text,
                                        fator_de_obsolecencia real,
                                        ano_de_inicio_da_vida_do_contribuinte integer,
                                        mes_de_inicio_da_vida_do_contribuinte integer,
                                        fase_do_contribuinte real
                                    ); """

    # create a database connection
    conn = criaConexao(configuracao.arquivoSqLite3)

    # create tables
    if conn is not None:
        # create projects table
        criaTabela(conn, createTableSQLGeoSampa)
    else:
        print("Error! cannot create the database connection.")

    return conn


if __name__ == '__main__':
    EnsureDatabaseCreation()
