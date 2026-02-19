'''Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All’avvio il programma chiede se si vuole leggere l’elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto'''

# dizionario = lettura()
def log_func(funzione):
    def wrapper(*args, **kwargs):
        print(f"\n---> Run di funzione : {funzione.__name__}")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

@log_func
def lettura(nome_file: str) -> dict[str, list]:
    """ funzione di lettura che prende nome del file str e restituisce un dizionario [alunno, [1,2,3]] """
    
    res: dict = {}

    try:
        with open(nome_file, "r") as file:
            raw = file.read()
        

        rows = raw.split("\n")

        for row in rows:
            
            splitted_row = row.split(",")
            
            key = splitted_row[0].strip()
            if key not in res:
                res[key] = []

            for i in range(1, len(splitted_row)):
                res[key].append(splitted_row[i].strip())

    except FileNotFoundError:
        print("Errore: Il file specificato non è stato trovato nella cartella!")
    except Exception as e:
        print(f"Si è verificato un errore inaspettato: {e}")
    finally:
        return res

@log_func
def modifica_voto(dizionario: dict, student: str, voto_start: int, voto_end: int):

    if student in dizionario:
        votes = dizionario[student]

        for i in range(len(votes)):
            if votes[i] == voto_start:
                votes[i] = voto_end
                return dizionario
        print(f"voto non trovato nella modifica voto di: {student}")
    else:
        print(f"Studente {student} non trovato per la modifica del voto")

    return dizionario

@log_func
def modifica_alunno(dizionario: dict, student:str):
    
    while True: 
        new_student = input(f"inserisci il nuovo nome per {student}: ").capitalize()
        if check_value(new_student, int):
            print("devi inserire una stringa")
        else:
            break

    res:dict = {}

    for k in dizionario.keys():
        if k == student:
            votes = dizionario[k]
            dizionario.pop(k)
            dizionario[new_student] = votes

            res = dizionario
            return res
        
    print(f"Studente {student} non trovato per la modifica dell'alunno")
    return res

@log_func
def elimina_studente(dizionario: dict, student: str):

    if student in dizionario:
        del dizionario[student]
    else:
        print(f"Studente {student} non trovato per l'eliminazione")

    return dizionario

    
def media_voti(alunno: str, dizionario: dict):
    #if len lista vuota blocca:
    try:
        voti = dizionario.get(alunno)
        voti = list(map(float, voti))
        media = sum(voti)/len(voti)
        return media
    except ZeroDivisionError:
        return 0

@log_func
def aggiungi_voto(alunno:str, dizionario:dict, new_voto:float):
    if alunno in dizionario:
        dizionario[alunno].append(new_voto)
        return dizionario
    else:
        print("alunno non trovato")
        return False
    
@log_func        
def crea_alunno(dizionario:dict, nome_alunno: str, voti_iniziali: str) -> dict[str, list]:
    """
    Aggiunge un nuovo alunno al dizionario e aggiorna il file.
    """
    if len(voti_iniziali) >0 :
        voti_iniziali = voti_iniziali.split(",")
    else:
        return False
    
    # 1. Se l'alunno non esiste, lo aggiungiamo
    if nome_alunno not in dizionario:
        dizionario[nome_alunno] = voti_iniziali
        return dizionario
    
    print(f"L'alunno {nome_alunno} esiste già.")
    return False


def scrittura(nome_file: str, dizionario: dict[str, list]) -> dict[str, list]:
    righe_testo = []
    
    for i in dizionario.items():
        lista = i[0]+ ","
        voti= ",".join(i[1]) 
        # print(f"DEBUG voti : {voti}")
        lista += voti
        righe_testo.append(lista)

    # Uniamo tutte le righe con un ritorno a capo
    testo_finale = "\n".join(righe_testo).replace(":", ",")
    # print(f"DEBUG  testo_finale: {testo_finale}")
    with open(nome_file, "w") as file:
        file.write(testo_finale)

    return dizionario

@log_func
def stampa_classe(dizionario):
    if dizionario:
        print(f"{'ALUNNO':<15} | {'VOTI':<15} | {'MEDIA':<5}")
        print("-" * 45)
        
        for alunno in dizionario:
            voti = dizionario[alunno]  
            media = media_voti(alunno, dizionario)
            
            # Parsing dei voti in str
            voti_str = ", ".join(map(str, voti))
            
            # Stampa tutto 
            print(f"{alunno:<15} | {voti_str:<15} | {media:>5.2f}")
            #{'Marco': [7, 8, 6], 'Anna': [9, 9, 10]}
    else:
        print("clase ancora vuota")
        
@log_func    
def check_value(stringa, tipo_atteso):
    try:
        valore_convertito = tipo_atteso(stringa)
        return valore_convertito
    except ValueError:
        return False
    
    
def play():
    opzioni = ("1", "2", "3", "4", "5", "6")
    nome_file = "classe.csv"
    dizionario = lettura(nome_file)
    print("DEBUG:," , dizionario)
    print( "connessione al db eseguita")
    
    while True:
            
        print("1) leggi elenco alunni \n2) aggiungi alunno\n3) aggiungi voto\n4) modifica voto\n5) modifica Alunnno\n6) elimina Alunno")
        user = input("quale azione vuoi fare?")
        scelta = None
        
    
        if user in opzioni:
            check_value(user, int)
            scelta = user
        else: 
            print("devi inserire una opzione valida")
      
        if scelta:
            match scelta:
                case "1":
                    stampa_classe(dizionario)

                case "2":
                    while True:
                        new_nome = input("inserisci nome del nuovo alunno : ").capitalize()

                        if check_value(new_nome, int):
                            print("devi inserire una stringa")
                            break       
                                             
                        voti_iniziali = input(f"inserisci  i voti per aluno {new_nome} separati da ',' : ")
                        if not crea_alunno(dizionario, new_nome, voti_iniziali):
                            print("ERRORE!")
                            
                        scrittura(nome_file, dizionario)
                        # print("DEBUG: scrittura runnata")
                        break
                
                case "3":
                    while True:
                        alunno = input("a quale alunno vuoi aggiungere voto?").capitalize()
                        if check_value(alunno, int):
                            print("devi inserire una stringa")
                            break
                        
                        new_voto = input(f"inserisci nuovo voto a {alunno}: ")
                        if not aggiungi_voto(alunno, dizionario, new_voto): 
                            print("ERRORE!")
                        else:
                            scrittura(nome_file, dizionario)
                            break
                case "4":
                    while True:
                        stampa_classe(dizionario)
                        alunno = input("a quale alunno vuoi MODIFICARE il voto?").capitalize()
                        if check_value(alunno, int):
                            print("devi inserire una stringa")
                            break
                        
                        old_voto = input(f"quale voto vuoi MODIFICARE di{alunno}?: ")
                        new_voto = input(f"inserisci nuovo voto a {alunno}: ")
                        if modifica_voto(dizionario, alunno, old_voto, new_voto): 
                            scrittura(nome_file, dizionario)
                            break
                        
                case "5":
                    while True:
                        stampa_classe(dizionario)
                        alunno = input("quale Nome vuoi MODIFICARE ?: ").capitalize()
                        if check_value(alunno, int):
                            print("devi inserire una stringa")
                            break
                        
                        if modifica_alunno(dizionario, alunno):
                            scrittura(nome_file, dizionario)
                            break
                        
                case "6" :
                    while True:
                        stampa_classe(dizionario)
                        alunno = input("quale alunno vuoi ELIMINARE ?: ").capitalize()
                        if check_value(alunno, int):
                            print("devi inserire una stringa")
                            break
                        
                        if elimina_studente(dizionario, alunno):
                            scrittura(nome_file, dizionario)
                            break
                
        if input("vuoi fare un'altra operazione? (y/n)") != "y":
            break
        scrittura
play()