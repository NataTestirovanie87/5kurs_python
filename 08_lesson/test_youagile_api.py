import pytest
import time
from Yougile_API import Yougile_API
from project_page import ProjectPage

# Настройки авторизации и базового URL
BASE_URL = "https://ru.yougile.com"
LOGIN = "shabardina.nata@internet.ru"
PASSWORD = "7magnitik-8belevyE-medovich"
COMPANY_NAME = "Поток 96,2"


@pytest.fixture(scope="module")
def api():
    api_instance = Yougile_API(BASE_URL, LOGIN, PASSWORD, COMPANY_NAME)
    # Получаем ID компании
    company_id = api_instance.get_id_company()
    assert company_id is not None, "Не удалось получить ID компании"
    # Получаем токен
    api_instance.get_key()
    assert api_instance.token is not None, "Не удалось получить токен"
    return api_instance


@pytest.fixture(scope="module")
def page(api):
    return ProjectPage(api)


def unique_title():
    return f"Тестовый проект {int(time.time())}"


@pytest.mark.positive_test_yougile
def test_get_project(api):
    # позитивный тест (используем существующие проекты)
    response = api.get_project_list()
    assert response.status_code == 200
    data = response.json()
    projects = data.get('content', [])
    assert isinstance(projects, list)


@pytest.mark.positive_test_yougile
def test_create_project_positive(page):
    # позитивный тест (создаем новый проект)
    title = unique_title()
    users = {"f1f27914-9417-4cf2-905e-0053bea90a5c": "admin"}

    response_before = page.get_projects()
    projects_before = response_before.json().get('content', [])
    len_before = len(projects_before)

    response_create = page.create_project(title=title, users=users)
    print("Create status:", response_create.status_code)
    print("Create response JSON:", response_create.json())
    assert response_create.status_code in [200, 201]

    # Можно добавить задержку для уверенности
    import time
    time.sleep(1)

    response_after = page.get_projects()
    projects_after = response_after.json().get('content', [])
    len_after = len(projects_after)

    print(f"Projects before: {len_before}, after: {len_after}")
    assert len_after - len_before == 1

    last_proj = projects_after[-1]
    assert last_proj["title"] == title


@pytest.mark.negative_test_yougile
def test_create_project_negative_empty_title(page):
    # негативный тест (пустой заголовок)
    users = {"f1f27914-9417-4cf2-905e-0053bea90a5c": "admin"}

    response = page.create_project(title="", users=users)

    # Предполагается ошибка (например 400 или 422), зависит от API.
    assert response.status_code in [400, 422]


@pytest.mark.positive_test_yougile
def test_edit_project_positive(page):
    # позитивный тест (изменение названия)
    title_orig = unique_title()

    create_resp = page.create_project(
        title=title_orig, users={
            "f1f27914-9417-4cf2-905e-0053bea90a5c": "admin"})

    project_id = create_resp.json().get("id")

    new_title = title_orig + "_обновлено"

    edit_resp = page.edit_project(project_id=project_id, new_title=new_title)

    assert edit_resp.status_code == 200

    search_resp = page.search_project_by_id(project_id)

    assert search_resp.status_code == 200

    data = search_resp.json()

    assert data["title"] == new_title


@pytest.mark.negative_test_yougile
def test_edit_nonexistent():
    # негативный тест (несуществующий ID)
    fake_id = 9999999999
    api_instance = Yougile_API(BASE_URL, LOGIN, PASSWORD, COMPANY_NAME)
    # Получаем токен для этого экземпляра
    company_id = api_instance.get_id_company()
    api_instance.company_id = company_id
    api_instance.get_key()
    response = api_instance.edit_project(project_id=fake_id, new_title="тест")
    # Предполагается статус 404 или подобное
    assert response.status_code in [404]


@pytest.mark.positive_test_yougile
def test_search_existing(page):
    # позитивный тест (существующий проект)
    title = unique_title()
    create_resp = page.create_project(
        title=title, users={
            "f1f27914-9417-4cf2-905e-0053bea90a5c": "admin"})
    project_id = create_resp.json().get("id")

    response = page.search_project_by_id(project_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


@pytest.mark.negative_test_yougile
def test_search_nonexistent():
    # негативный тест (неправильный ID)
    fake_id = 9999999999
    api_instance = Yougile_API(BASE_URL, LOGIN, PASSWORD, COMPANY_NAME)
    company_id = api_instance.get_id_company()
    api_instance.company_id = company_id
    api_instance.get_key()

    response = api_instance.search_project_by_id(fake_id)
    # Предполагается статус 404
    assert response.status_code in [404]
