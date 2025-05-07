import os

class Jurnal:
    def __init__(self, file_name="jurnal.txt"):
        self.file_name = file_name
        # Citim mesaje existente din jurnal (daca exista)
        self.messages = self.read_journal()

    def read_journal(self):
        # Daca fisierul exista, citim mesajele din el
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return file.readlines()
        else:
            return []

    def write_in_journal(self, message):
        # Scriem un mesaj nou in jurnal
        with open(self.file_name, "a") as file:
            file.write(message + "\n")

    def display_journal(self):
        # Afisam mesajele din jurnal
        if self.messages:
            print("\nMesaje in jurnalul altor jucatori:")
            for msg in self.messages:
                print(msg.strip())
        else:
            print("\nJurnalul este gol.")
