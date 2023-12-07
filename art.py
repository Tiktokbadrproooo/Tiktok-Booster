from colorama import Fore, Style
from pystyle import Center

LOGO_ART = Center.XCenter(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + """
██╗░░██╗░█████╗░██████╗░██╗███████╗░█████╗░███╗░░██╗░██████╗  ███████╗██████╗░░██████╗░███████╗
██║░░██║██╔══██╗██╔══██╗██║╚════██║██╔══██╗████╗░██║██╔════╝  ██╔════╝██╔══██╗██╔════╝░██╔════╝
███████║██║░░██║██████╔╝██║░░███╔═╝██║░░██║██╔██╗██║╚█████╗░  █████╗░░██║░░██║██║░░██╗░█████╗░░
██╔══██║██║░░██║██╔══██╗██║██╔══╝░░██║░░██║██║╚████║░╚═══██╗  ██╔══╝░░██║░░██║██║░░╚██╗██╔══╝░░
██║░░██║╚█████╔╝██║░░██║██║███████╗╚█████╔╝██║░╚███║██████╔╝  ███████╗██████╔╝╚██████╔╝███████╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝╚═════╝░  ╚══════╝╚═════╝░░╚═════╝░╚══════╝

████████╗██╗██╗░░██╗████████╗░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗████████╗███████╗██████╗░
╚══██╔══╝██║██║░██╔╝╚══██╔══╝██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░██║█████═╝░░░░██║░░░██║░░██║█████═╝░  ██████╦╝██║░░██║░░░██║░░░░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██║██╔═██╗░░░░██║░░░██║░░██║██╔═██╗░  ██╔══██╗██║░░██║░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░██║██║░╚██╗░░░██║░░░╚█████╔╝██║░╚██╗  ██████╦╝╚█████╔╝░░░██║░░░░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n\n
        DISCORD: https://discord.gg/AMqeGspYK3   GITHUB: https://github.com/itsOdell
""")

input_style = Style.BRIGHT + Fore.LIGHTCYAN_EX
success_style = Fore.LIGHTGREEN_EX + Style.BRIGHT
error_style = Fore.LIGHTRED_EX + Style.BRIGHT
info_style = Fore.LIGHTWHITE_EX + Style.BRIGHT
warning_style = Fore.LIGHTYELLOW_EX + Style.BRIGHT
light_magenta = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
white_style = Fore.LIGHTWHITE_EX + Style.BRIGHT
reset_style = Style.RESET_ALL