import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def url():
    return '/courses/'


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make('Course', *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make('Student', *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(api_client, course_factory, url):
    course = course_factory(_quantity=1)
    response = api_client.get(f'{url}{course[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert course[0].id == data.get('id')


@pytest.mark.django_db
def test_courses_list(api_client, course_factory, url):
    courses = course_factory(_quantity=10)
    response = api_client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_courses_id_filter(api_client, course_factory, url):
    courses = course_factory(_quantity=10)
    response = api_client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_courses_name_filter(api_client, course_factory, url):
    courses = course_factory(_quantity=10)
    response = api_client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(api_client, url):
    data = {
        'name': 'Python'
    }
    response = api_client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'] == 'Python'


@pytest.mark.django_db
def test_update_course(api_client, course_factory, url):
    course = course_factory(_quantity=1)
    data = {
        'name': 'JavaScript'
    }
    response = api_client.patch(f'{url}{course[0].id}/', data=data)

    assert response.status_code == 200
    assert response.data['name'] == 'JavaScript'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory, url):
    course = course_factory(_quantity=1)
    response = api_client.delete(f'{url}{course[0].id}/')
    response_get = api_client.get(url)
    data = response_get.json()

    assert response.status_code == 204
    assert len(data) == 0







