import os,re

os.system("clear")

class color:
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

lines = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]

print("Bonjour et bienvenue sur ce puissance 4")
player1 = input(f"Choisissez le nom du premier joueur ({color.YELLOW}X{color.END}) : ")
player2 = input(f"Choisissez le nom du deuxième joueur ({color.RED}O{color.END}): ")

os.system("clear")
def display_gameboard(color, lines):
    output = ""
    for line in enumerate(reversed(lines)):
        output+="|"
        for columns in line[1]:
            if columns == "X":
                output+=f" {color.YELLOW + columns + color.END} |"
            elif columns == "O":
                output+=f" {color.RED + columns + color.END} |"
            else:
                output+=f" {columns} |"
        output+="\n"
    output+="|---|---|---|---|---|---|---|\n"
    output+="| 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n"

    print(output)


def prompt_player(lines, player, token):
    playerColor= color.YELLOW if token == "X" else color.RED
    print(f"Ok, {playerColor + player + color.END} C'est votre tour, choisissez dans quelle colonne vous souhaitez mettre le jeton")
    inputValue = input("Colonne # : ")
    validationRegexp = re.compile("^[1-7]$")
    while not validationRegexp.match(inputValue):
        print(f"Votre saisie \"{ inputValue }\", n'est pas valide, veuillez entre un chiffre entre 1 et 7.")
        inputValue = input("Colonne # : ")
        
    column = int(inputValue)-1

    for line in lines:
        if line[column] == " ":
            line[column] = token
            break

while True:
    display_gameboard(color, lines)

    prompt_player(lines, player1, "X")

    os.system("clear")

    display_gameboard(color, lines)

    prompt_player(lines, player2, "O")

    os.system("clear")
