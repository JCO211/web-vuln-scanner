import requests

def check_headers(url):
    print("[*] Checking security headers...")

    try:
        response = requests.get(url)
    except:
        print("[!] Error connecting to the website")
        return

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-XSS-Protection",
        "Strict-Transport-Security"
    ]

    for header in security_headers:
        if header in response.headers:
            print(f"[+] {header} found")
        else:
            print(f"[!] {header} MISSING")
