import requests


def main():
    url = 'http://wttr.in/'
    cities = ['Лондон', 'cvo', 'Череповец']
    for city in cities:
        payload = {'n': '', 'T': '', 'q': '', 'm': '', 'lang': 'ru'}
        response = requests.get(f'{url}{city}', params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
