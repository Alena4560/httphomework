import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        host_name = "https://cloud-api.yandex.net:443"
        self.url = host_name + "/v1/disk/resources/upload"

    def get_file_name(self, file_path: str):
        pos = file_path.rfind('\\')
        if pos == -1:
            file_name = file_path
        else:
            file_name = file_path[pos+1:]
        return file_name

    def get_upload_link(self, file_name: str):
        my_headers = {"Authorization": "OAuth " + self.token}
        my_params = {"path": file_name, "overwrite": "true"}
        response = requests.get(self.url, headers=my_headers, params=my_params)
        if response.status_code == 200:
            return response.json()["href"]
        else:
            return "ERROR " + str(response.status_code)

    def upload(self, file_path: str):
        print("Загружаем файл:", file_path)
        file_name = self.get_file_name(file_path)
        print("Имя файла:", file_name)
        upload_link = self.get_upload_link(file_name)
        print("Ссылка для загрузки:", upload_link)
        if upload_link.startswith("ERROR"):
            print("Не удалось загрузить файл! ОШИБКА " + upload_link[6:])
            return False
        else:
            f = open(file_path, "rb")
            response = requests.put(upload_link, data=f)
            f.close()
            if response.status_code == 201:
                print("Файл успешно загружен!")
                return True
            else:
                print("Не удалось загрузить файл! ОШИБКА " + str(response.status_code))
                return False
            
if __name__ == '__main__':
    path_to_file = "D:\\Temp\\MatrixDebug.txt"
    token = " "
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
