import requests

class YaUploader:

    base_host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth{self.token}'
             }

    def get_link(self, path):
        uri = '/v1/disk/resuorces/upload'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    
    def upload(self, file_path, yandex_path):
        upload_url = self.get_link(yandex_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка прошла успешно')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    #yandex_path = '/test_file1.txt'
    #file_path = '/test_file.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload('C:/Users/glesh/netology/super_heroes/test_file.txt', 'test_file1.txt')
