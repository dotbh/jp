import requests

api_url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response


if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    insult = response.json()['insult']
    print(insult)
else:
    print(response.status_code)