import requests

def check_sensitive_files(url):
    print("\n[*] Checking sensitive files...")

    sensitive_files = [
        "robots.txt",
        ".env",
        "config.php",
        ".git/"
    ]

    for file in sensitive_files:
        full_url = f"{url}/{file}"

        try:
            r = requests.get(full_url)
            if r.status_code == 200:
                print(f"[!] Found exposed file: {full_url}")
        except:
            pass
