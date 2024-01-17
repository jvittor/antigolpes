from pysafebrowsing import SafeBrowsing

# Substitua 'YOUR_API_KEY' pela sua chave de API
API_KEY = 'AIzaSyCuEVNiq9Zc-ccKbHeuw7q1xjAasEfDczA'
s = SafeBrowsing(API_KEY)

def check_url(url):
    try:
        # Verifica se a URL é segura
        result = s.lookup_urls([url])

        if result and url in result:
            details = result[url]
            if details['malicious']:
                print(f'A URL {url} não é segura.')
                print('Detalhes:')
                print(f' - Plataformas: {details["platforms"]}')
                print(f' - Ameaças: {details["threats"]}')
                print(f' - Cache: {details["cache"]}')
            else:
                print(f'A URL {url} é segura.')
        else:
            print(f'Não foi possível obter informações para a URL {url}.')

    except Exception as e:
        print(f"Erro ao verificar a URL {url}: {e}")

# Exemplo de uso
url_to_check = 'http://malware.testing.google.test/testing/malware/'
check_url(url_to_check)
