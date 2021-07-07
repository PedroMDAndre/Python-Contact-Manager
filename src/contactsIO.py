import os
path: str = "../save/contacts.csv"
separator: str = ","


def saveContactsData(contactos: list[list[str]]):
    ficheiro = open(path, "w", encoding="utf-8-sig")

    for contacto in contactos:
        ficheiro.write(separator.join(contacto))
        ficheiro.write("\n")

    ficheiro.close()


def loadContactsData() -> list[list[str]]:
    if not os.path.isfile(path):
        saveContactsData([])

    pessoas: list[list[str]] = []
    ficheiro = open(path, "r", encoding="utf-8-sig")
    linhas = ficheiro.readlines()
    ficheiro.close()

    for linha in linhas:
        pessoa = linha.replace("\n", "").split(separator)
        pessoas.append(pessoa)
    return pessoas


if __name__ == '__main__':
    saveContactsData(loadContactsData())
