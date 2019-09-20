
def readconf(filename):
    """
    Cette fonction lit un fichier de configuration
    contenant des lignes de la forme variable=valeur.
    Le caractère # est la marque d'un début de commentaire.
    Il peut y avoir des lignes vides dans ce fichier.

    La fonction reçoit en paramètre le nom du fichier.
    Elle renvoie un dictionnaire dont les clés sont les variables
    définies dans le fichier, et les valeurs leurs valeurs.
    """

    il = 1
    table = {}
    with open(filename, "r") as f:
      for line in f:
          line = line.strip()       # supprimer le saut de ligne
          if line=="": continue     # c'est une ligne vide
          if line[0]=="#": continue # c'est un commentaire
          if not "=" in line:       # cas non prévu
              raise Exception(f"erreur de syntaxe en ligne {il}: {line}")
          l = line.split('=')
          table[l[0]] = l[1]
          il += 1
    return table

def read_from_keyboard():
    """
    Renvoie des entiers lus au clavier
    """
    l =[]
    print("entrer un entier par ligne, et autre chose pour finir")
    while True:
      try:
        l.append(int(input()))
      except ValueError :
        break # sortie de while
    return l

def read_from_cmdline():
    """
    Renvoie des entiers lus sur la ligne de commande
    """
    return sys.argv[1:]

def read_from_file(filename):
    """
    Renvoie des entiers lus dans le fichier dont le nom est contenu dans filename
    """
    l =[]
    with open(filename, "r") as f:
      for line in f:
        l.append(int(line))
    return l

if __name__=="__main__":
  print("""
Fonctions offertes par ce module :
  readconf(): blabla
  read_from_keyboard(): blabla
  read_from_cmdline(): blabla
  lire_from_file(): blabla
  """)