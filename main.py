import os,re

os.system("clear")

class color:
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

lines = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]

player1 = {"token":"X", "color":color.YELLOW}
player2 = {"token":"Y", "color":color.RED}

print("Bonjour et bienvenue sur ce puissance 4")
player1["name"] = input(f"Choisissez le nom du premier joueur ({player1.get('color') + player1.get('token') + color.END}) : ")
player2["name"] = input(f"Choisissez le nom du deuxième joueur ({player2.get('color') + player2.get('token') + color.END}): ")

os.system("clear")
def display_gameboard(color, lines):
    output = ""
    for line in enumerate(reversed(lines)):
        output+="|"
        for columns in line[1]:
            if columns == player1.get('token'):
                output+=f" {player1.get('color') + columns + color.END} |"
            elif columns == player2.get('token'):
                output+=f" {player2.get('color') + columns + color.END} |"
            else:
                output+=f" {columns} |"
        output+="\n"
    output+="|---|---|---|---|---|---|---|\n"
    output+="| 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n"

    print(output)


def prompt_player(lines, player, token):
    print(f"Ok, {player.get('color') + player.get('name') + color.END} C'est votre tour, choisissez dans quelle colonne vous souhaitez mettre le jeton")
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

def player_turn(color, lines, player, display_gameboard, prompt_player):
    display_gameboard(color, lines)

    prompt_player(lines, player, player.get('token'))

    os.system("clear")

while True:
    player_turn(color, lines, player1, display_gameboard, prompt_player)

    player_turn(color, lines, player2, display_gameboard, prompt_player)
