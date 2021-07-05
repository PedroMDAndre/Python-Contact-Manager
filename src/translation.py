class Translation:
    dictionary: dict = {
        "add_contact": ["Adicionar\nContacto", "Add\nContact"],
        "remove_contact": ["Remover\nContacto", "Remove\nContact"],
        "sort_contacts": ["Ordenar\nCres./Decres.", "Sort\nAsc./Des."],
        "find_contacts": ["Procurar", "Find"],
        "show_all_entries": ["Todos os\ncontactos", "All\nContacts"],
        "change_language": ["Mudar de\nLíngua", "Change\nLanguage"]
    }

    def __init__(self):
        self.PT: int = 0
        self.EN: int = 1

        self.linguaActual = self.PT

    def trocarLingua(self):
        if self.linguaActual == self.PT:
            self.linguaActual = self.EN
        else:
            self.linguaActual = self.PT

    def traducao(self, entrada):
        return Translation.dictionary[entrada][self.linguaActual]
