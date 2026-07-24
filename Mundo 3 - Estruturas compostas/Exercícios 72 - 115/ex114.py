import urllib.request
import urllib.error


def verificar_site(url):

    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.URLError:
        return False

if verificar_site("https://pudim.com.br/"):
    print("\033[92mO site está online! \033[0m")
if not verificar_site("https://pudim.com.br/"):
    print("\033[31mO site está offline! \033[0m")