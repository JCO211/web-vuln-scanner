import requests
from bs4 import BeautifulSoup

def check_xss(url):
    print("\n[*] Checking for basic XSS vulnerabilities...")

    payload = "<script>alert('XSS')</script>"

    try:
        response = requests.get(url)
    except:
        print("[!] Could not connect to target")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    if not forms:
        print("[-] No forms found")
        return

    for form in forms:
        action = form.get("action")
        method = form.get("method", "get").lower()

        data = {}
        for input_tag in form.find_all("input"):
            name = input_tag.get("name")
            if name:
                data[name] = payload

        if action and action.startswith("http"):
            target_url = action
        elif action:
            target_url = url.rstrip("/") + "/" + action.lstrip("/")
        else:
            target_url = url

        if method == "post":
            r = requests.post(target_url, data=data)
        else:
            r = requests.get(target_url, params=data)

        if payload in r.text:
            print(f"[!] Possible XSS found in form at {target_url}")
        else:
            print(f"[+] Form at {target_url} seems safe")
