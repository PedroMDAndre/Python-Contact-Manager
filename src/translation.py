class Translation:
    dictionary: dict = {
        "add_contact": ["Adicionar Contacto", "Add Contact"],
        "remove_contact": ["Remover Contacto", "Remove Contact"],
        "sort_contacts": ["Ordenar Cres./Decres.", "Sort Asc./Des."],
        "find_contacts": ["Procurar", "Find"],
        "show_all_entries": ["Todas os contactos", "All Contacts"],
        "change_language": ["Mudar de Língua", "Change Language"]
    }

    def __init__(self):
        self.PT: int = 0
        self.EN: int = 1

        self.linguaActual = self.EN

    def trocarLingua(self):
        if self.linguaActual == self.PT:
            self.linguaActual = self.EN
        else:
            self.linguaActual = self.PT

    def traducao(self, entrada):
        return Translation.dictionary[entrada][self.linguaActual]
