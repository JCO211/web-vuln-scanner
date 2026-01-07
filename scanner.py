#!/usr/bin/env python3

# ===== COLORES ANSI =====
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# ===== IMPORTAR MÓDULOS =====
from modules.headers import check_headers
from modules.files import check_sensitive_files
from modules.xss import check_xss


# ===== BANNER =====
def banner():
    print(RED + r"""
██╗    ██╗██╗   ██╗██╗     ███╗   ██╗
██║    ██║██║   ██║██║     ████╗  ██║
██║ █╗ ██║██║   ██║██║     ██╔██╗ ██║
██║███╗██║██║   ██║██║     ██║╚██╗██║
╚███╔███╔╝╚██████╔╝███████╗██║ ╚████║
 ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝
""" + RESET)

    print(BLUE + "Web Vulnerability Scanner" + RESET)
    print(YELLOW + "Author: jco11" + RESET)
    print(GREEN + "Educational & Ethical Use Only\n" + RESET)


# ===== MENÚ =====
def menu():
    print(BLUE + "[1] Scan Security Headers" + RESET)
    print(BLUE + "[2] Scan Sensitive Files" + RESET)
    print(BLUE + "[3] Scan XSS" + RESET)
    print(YELLOW + "[4] Full Scan" + RESET)
    print(RED + "[0] Exit\n" + RESET)


# ===== FUNCIÓN PRINCIPAL =====
def main():
    banner()

    target = input(YELLOW + "Enter target URL (example: http://localhost/dvwa): " + RESET)

    while True:
        menu()
        choice = input(GREEN + "Select an option: " + RESET)

        if choice == "1":
            check_headers(target)

        elif choice == "2":
            check_sensitive_files(target)

        elif choice == "3":
            check_xss(target)

        elif choice == "4":
            check_headers(target)
            check_sensitive_files(target)
            check_xss(target)

        elif choice == "0":
            print(RED + "Exiting scanner..." + RESET)
            break

        else:
            print(RED + "Invalid option, try again." + RESET)


# ===== EJECUCIÓN =====
if __name__ == "__main__":
    main()
