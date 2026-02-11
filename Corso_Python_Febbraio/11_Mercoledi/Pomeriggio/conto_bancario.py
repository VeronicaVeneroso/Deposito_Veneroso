
class ContoBancario:
    def __init__(self, titolare:str, saldo = 0.0):
        if titolare.strip():
            self.__titolare = titolare
        else:
            print("Il nome del titolare non può essere vuoto.")
        if saldo >= 0:
            self.__saldo = saldo
        else:
            self.__saldo = 0.0
    
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, nuovo_titolare:str):
        if nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
        else:
            print("Il nome del titolare non può essere vuoto.")

    def deposita(self, importo:float):
        if importo <= 0:
            print("L'importo del deposito deve essere positivo.")
        else:
            self.__saldo += importo
            self.visualizza_saldo()
            
    def preleva(self, importo:float):
        if importo <= 0:
            print("L'importo da prelevare deve essere positivo.")
        elif importo <= self.__saldo:
            self.__saldo -= importo
            self.visualizza_saldo()
        else:
            print("Fondi insufficienti per prelevare questa cifra.")

    def visualizza_saldo(self):
        print(f"Il saldo ammonta a {self.__saldo}€")
        return self.__saldo

class Utente:
    def __init__(self, nome:str, conto:ContoBancario):
        self.nome = nome
        self._conto = conto

class TitolareConto(Utente):
    def __init__(self, nome, conto, password:str):
        super().__init__(nome, conto)
        self.__password = password

    def deposita(self, importo:float):
        self._conto.deposita(importo)

    def preleva(self, importo:float):
        self._conto.preleva(importo)

    def visualizza_saldo(self):
        return self._conto.visualizza_saldo()

class Admin(Utente):
    def __init__(self, nome, conto):
        super().__init__(nome, conto)

    def visualizza_saldo(self):
        return self._conto.visualizza_saldo()



nome = input("Inserisci il tuo nome: ")
conto = ContoBancario(nome)
utente = input("Sei il titolare o un admin? (titolare/admin) ").lower()
risposta = "si"
while risposta == "si":
    risposta = input("Vuoi effettuare una nuova operazione? (si/no)").lower()
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            risposta = "si"
            print("Opzione selezionata non valida.")
            continue

    if utente == "titolare":
        password = input("Inserisci la tua password: ")
        utente = TitolareConto(nome,conto,password)
        operazione = input("Che tipo di operazione vuoi effettuare? (preleva/deposita/visualizza): ")
        match operazione:
            case "preleva":
                importo = float(input("Quanto vuoi prelevare? "))
                utente.preleva(importo)
            case "deposita":
                importo = float(input("Quanto vuoi depositare? "))
                utente.deposita(importo)
            case "visualizza":
                utente.visualizza_saldo()
            case _:
                print("Opzione selezionata non valida.")
        
    elif utente == "admin":
        utente = Admin(nome, conto)
        utente.visualizza_saldo()
    
    else:
        print("Opzione selezionata non valida.")