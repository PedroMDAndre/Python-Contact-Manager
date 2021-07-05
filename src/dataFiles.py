path: str = "../save/contacts.csv"
separator: str = ","


def saveContactsData():
    contactos = [['Jane', ' 123', ' 234', ' jane@outlook.com'], ['Paul', ' 153', ' 134', ' jane@outlook.com']]
    ficheiro = open(path, "w", encoding="utf-8-sig")

    for contacto in contactos:
        ficheiro.write(separator.join(contacto))
        ficheiro.write("\n")

    ficheiro.close()


def loadContactsData():
    pessoas = []
    ficheiro = open(path, "r", encoding="utf-8-sig")
    linhas = ficheiro.readlines()
    ficheiro.close()

    for linha in linhas:
        pessoa = linha.replace("\n", "").split(",")
        pessoas.append(pessoa)
    print(pessoas)


if __name__ == '__main__':
    saveContactsData()
