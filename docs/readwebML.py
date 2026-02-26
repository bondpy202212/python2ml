import requests


def save_page_content(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности запроса
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Save to file: {filename}")
    except requests.RequestException as e:
        print(f"Error open website(http://127.0.0.1:5002): {e}")

if __name__ == "__main__":
    url = "http://127.0.0.1:5002"
    filename = "index.html"
    save_page_content(url, filename)