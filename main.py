import os

os.system("clear")

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

lines = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]

print("Bonjour et bienvenue sur ce puissance 4")
player1 = input(f"Choisissez le nom du premier joueur ({color.YELLOW}X{color.END}) : ")
player2 = input(f"Choisissez le nom du deuxième joueur ({color.RED}O{color.END}): ")

os.system("clear")
while True:
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

    print(f"Ok, {player1} C'est votre tour, choisissez dans quelle colonne vous souhaitez mettre le jeton")
    column = int(input("Column # : "))-1

    for index,line in enumerate(lines):
        if line[column] == " ":
            line[column] = "X"
            break

    os.system("clear")

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

    print(f"Ok, {player2} C'est votre tour, choisissez dans quelle colonne vous souhaitez mettre le jeton")
    column = int(input("Column # : "))-1

    for index,line in enumerate(lines):
        if line[column] == " ":
            line[column] = "O"
            break

    os.system("clear")
