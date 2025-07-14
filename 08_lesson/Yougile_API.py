import requests


class Yougile_API:
    def __init__(self, base_url, login, password, company_name):
        self.base_url = base_url
        self.login = login
        self.password = password
        self.company_name = company_name
        self.token = None
        self.company_id = None

    def get_headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    # получение айди компании
    def get_id_company(self):
        url = f"{self.base_url}/api-v2/auth/companies"
        for_id_company = {
            "login": self.login,
            "password": self.password,
            "name": self.company_name
        }
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            resp = requests.post(url, json=for_id_company, headers=headers)
            resp.raise_for_status()
            data = resp.json()

            # Проверяем наличие ключа 'content' и его содержимое
            content_list = data.get('content', [])
            if content_list:
                first_company = content_list[0]
                company_id = first_company.get('id')
                self.company_id = company_id
                if company_id:
                    print(f"ID компании: {company_id}")
                    return company_id
                else:
                    print("ID не найден в первом объекте content.")
            else:
                print("Список content пуст или отсутствует.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")

    # авторизация и получение ключа
    def get_key(self):
        url = f"{self.base_url}/api-v2/auth/keys"
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            resp = requests.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            key = data.get("key")
            self.token = key
            print(f"Token: {key}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении ключа: {e}")

    def get_project_list(self):
        url = f"{self.base_url}/api-v2/projects"
        headers = self.get_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp

    def create_project(self, title, users):
        data = {
            "title": title,
            "users": users
        }
        resp = requests.post(
            f"{self.base_url}/api-v2/projects", headers=self.get_headers(),
            json=data)
        return resp

    def edit_project(
            self, project_id, new_title=None, new_users=None, deleted=False):
        data = {
            "deleted": deleted
        }
        if new_title is not None:
            data["title"] = new_title
        if new_users is not None:
            data["users"] = new_users

        resp = requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.get_headers(), json=data)
        return resp

    def search_project_by_id(self, project_id):
        resp = requests.get(f"{self.base_url}/api-v2/projects/{project_id}",
                            headers=self.get_headers())
        return resp
