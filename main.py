import base64
import os
from colorama import init, Fore

init()


pink = Fore.LIGHTMAGENTA_EX
red = Fore.RED
grey = Fore.WHITE
lightcyan = Fore.LIGHTCYAN_EX

def generate_ascii_art():
    ascii_art = f"""
        {pink}╔═══════════════════════════════════════════════╗ ╔═══════════════╗
        {pink}║               ┏┓┏┓┓┏  ┏┓┳┳┓┏┓┏┓┳┓             ║ ║    sshmoon    ║
        {pink}║               ┗┓┗┓┣┫  ┃┃┃┃┃┃┓┣ ┣┫             ║ ╠═══════════════╣
        {pink}║               ┗┛┗┛┛┗  ┣┛┻┛┗┗┛┗┛┛┗             ║ ║   SSH Token   ║
        {pink}╚═══════════════════════════════════════════════╝ ╚═══════════════╝
        {red}╔═════════════════════════════════════════════════════════════════╗
        {red}║                  [!] New update soon... [!]                     ║
        {red}║                                                                 ║
        {red}║                   [&]  t.me/sshipport  [&]                      ║
        {red}╚═════════════════════════════════════════════════════════════════╝
    """
    return ascii_art

def encode_text(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return encoded_text

def main():
    gui = generate_ascii_art()
    print(gui)
    discord_id = input(f"{pink}[{lightcyan}>>>{pink}] {lightcyan}Discord ID: ").strip()
    encoded_id = encode_text(discord_id)
    print(f"{pink}[{lightcyan}>>>{pink}] {lightcyan}First Half Of Token: {pink}{lightcyan}{encoded_id}")

    qwe = input()
    clear = lambda: os.system('cls')
    clear()
    main()

if __name__ == "__main__":
    main()
