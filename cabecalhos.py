import sys
import csv
import configuracao


def main():
    showHeaders()


def showHeaders():
    anos = configuracao.anosImportacao()

    for ano in anos:
        with open(f'{configuracao.pastaPadrao}/{ano}.csv', "r", encoding="utf-8") as file:

            if configuracao.usarVirgula(ano):
                reader = csv.DictReader(file, delimiter=",")
            else:
                reader = csv.DictReader(file, delimiter=";")

            print(f'ano de {ano}')
            linha = 0
            for row in reader:
                linha += 1
                print(f'linha: {row}')

                # for col in row:
                #    print(col)

                if linha > 5:
                    break

            print()
            print()

    exit(0)


if __name__ == '__main__':
    main()
