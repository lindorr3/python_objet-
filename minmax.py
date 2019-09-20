from fonctions import readconf
import fonctions

CONFFILE = "monprog.conf"

config = readconf(CONFFILE)

if config["read"]=="keyboard":
    print("lecture des données depuis le clavier")
    l = fonctions.read_from_keyboard()
elif config["read"]=="arg":
    print("lecture des données depuis la ligne de commande")
    l = fonctions.read_from_cmdline()
elif config["read"]=="file":
    print("lecture des données depuis keyboard", end="")
    if "datafile" in config:
        filename = config["datafile"]
        print(filename)
    else:
        print("un fichier.")
        filename = input("Entrer le nom de ce fichier:")
    l = fonctions.read_from_file(filename)

if (config["search"]=="min"):
    print(f"le min est {min(l)}")
elif (config["search"]=="max"):
    print(f"le max est {max(l)}")
else:
    print("valeur inconnue pour search")
    
    
    
