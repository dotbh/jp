import requests

api_url = 'https://api.adviceslip.com/advice'

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response


if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе 
    slip = response.json()['slip']
    res_data = slip['advice']
    print(res_data)
else:
    print(response.status_code)
