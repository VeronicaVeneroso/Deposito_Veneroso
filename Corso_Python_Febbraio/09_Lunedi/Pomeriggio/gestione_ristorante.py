class Ristorante:
    aperto = False
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.piatti = []
        self.prezzi = []

    def descrivi_ristorante(self):
        print(f"Questo ristorante si chiama {self.nome} e fa {self.tipo_cucina}")
    
    def stato_apertura(self):
        if self.aperto == True:
            print("Il ristorante è aperto.")
        else:
            print("Il ristorante è chiuso.")
    
    def apri_ristorante(self):
        self.aperto = True
        self.stato_apertura()
    
    def chiudi_ristorante(self):
        self.aperto = False
        self.stato_apertura()
    
    def aggiungi_al_menu(self, piatto, prezzo):
        self.piatti.append(piatto)
        self.prezzi.append(prezzo)
    
    def togli_dal_menu(self, piatto):
        if piatto in self.piatti:
            i = self.piatti.index(piatto)
            self.piatti.remove(piatto)
            self.prezzi.remove(self.prezzi[i])
        else:
            print("Questo piatto non è presente nel menu")
    
    def stampa_menu(self):
        for i in range(len(self.piatti)):
            print(self.piatti[i], self.prezzi[i])
    


risposta = "si"
while risposta == "si":
    risposta = input("Vuoi inserire un ristorante? (si/no) ")
    match risposta:
        case "si":
            pass
        case "no":
            break
        case _:
            print("Risposta non valida.")
            risposta = "si"
            continue
    
    nome = input("Inserisci nome: ")
    tipo_cucina = input("Indica il tipo di cucina: ")
    ristorante = Ristorante(nome, tipo_cucina)

    ristorante.descrivi_ristorante()

    scelta = "si"
    while scelta == "si":
        risposta = input("Il ristorante è aperto? (si/no) ")
        match risposta:
            case "si":
                ristorante.apri_ristorante()
                pass
            case "no":
                ristorante.chiudi_ristorante()
                pass
            case _:
                print("Risposta non valida.")
                risposta = "si"
                continue

    scelta = "si"
    while scelta == "si":
        risposta = input("Vuoi aggiungere un piatto al menu? (si/no) ")
        match risposta:
            case "si":
                pass
            case "no":
                break
            case _:
                print("Risposta non valida.")
                risposta = "si"
                continue
        piatto = input("Aggiungi piatto al menu: ")
        prezzo = float(input("Aggiungi il suo prezzo: "))
        ristorante.aggiungi_al_menu(piatto, prezzo)
    
    scelta = "si"
    while scelta == "si":
        risposta = input("Vuoi rimuovere un piatto dal menu? (si/no) ")
        match risposta:
            case "si":
                pass
            case "no":
                break
            case _:
                print("Risposta non valida.")
                risposta = "si"
                continue
        piatto = input("Indica il piatto da rimuovere dal menu: ")
        ristorante.togli_dal_menu(piatto)

    print("----- MENU -----")
    for i in range(len(ristorante.piatti)):
        print(ristorante.piatti[i], " ", ristorante.prezzi[i], "€")


# Inventa un extra