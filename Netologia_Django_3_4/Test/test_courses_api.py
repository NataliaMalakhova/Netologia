import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    # Создаем курс через фабрику
    course = course_factory()

    # Строим URL для получения курса
    url = reverse('course-detail', args=[course.id])
    response = api_client.get(url)

    # Проверяем, что вернулся нужный курс
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    # Создаем несколько курсов через фабрику
    course1 = course_factory()
    course2 = course_factory()

    # Делаем запрос на получение списка курсов
    url = reverse('course-list')
    response = api_client.get(url)

    # Проверяем, что список курсов содержит нужные данные
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) >= 2  # Количество созданных курсов
    ids = [course['id'] for course in response.data]
    assert course1.id in ids
    assert course2.id in ids


@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    # Создаем курсы через фабрику
    course1 = course_factory()
    course2 = course_factory()

    # Фильтрация списка курсов по ID
    url = reverse('course-list')
    response = api_client.get(url, {'id': course1.id})

    # Проверяем, что вернулся нужный курс
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == course1.id


@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    # Создаем курсы через фабрику
    course1 = course_factory(name='Python Basics')
    course2 = course_factory(name='Advanced Django')

    # Фильтрация списка курсов по имени
    url = reverse('course-list')
    response = api_client.get(url, {'name': 'Python Basics'})

    # Проверяем, что вернулся нужный курс
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Python Basics'


@pytest.mark.django_db
def test_create_course(api_client):
    # Данные для создания курса
    course_data = {
        'name': 'New Course',
        'description': 'Course description',
    }

    # Создаем курс
    url = reverse('course-list')
    response = api_client.post(url, course_data)

    # Проверяем, что курс успешно создан
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == course_data['name']


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    # Создаем курс через фабрику
    course = course_factory()
    updated_data = {'name': 'Updated Course'}

    # Обновляем курс
    url = reverse('course-detail', args=[course.id])
    response = api_client.patch(url, updated_data)

    # Проверяем, что курс успешно обновлен
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Updated Course'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    # Создаем курс через фабрику
    course = course_factory()

    # Удаляем курс
    url = reverse('course-detail', args=[course.id])
    response = api_client.delete(url)

    # Проверяем, что курс успешно удален
    assert response.status_code == status.HTTP_204_NO_CONTENT
