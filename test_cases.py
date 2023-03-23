#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pages import YandexMainPage


def test_yandex_search(driver):
    page = YandexMainPage(driver)
    # 1.Зайти на https://ya.ru/
    page.get()
    # 2.Проверить наличия поля поиска
    assert page.find_element(page.SEARCH_FIELD).is_displayed()
    # 3.Ввести в поиск Тензор
    page.enter_text(page.SEARCH_FIELD, "Тензор")
    # 4.Проверить, что появилась таблица с подсказками (suggest)
    assert page.find_element(page.SUGGEST_FIELD).is_displayed()
    # 5.Нажать enter
    page.enter(page.SEARCH_FIELD)
    # 6.Проверить, что появилась страница результатов поиска
    assert page.find_element(page.SEARCH_RESULTS).is_displayed()
    # 7.Проверить 1 ссылка ведет на сайт tensor.ru
    assert page.get_attr(page.LINK, "href") == "https://tensor.ru/"


def test_yandex_images(driver):
    page = YandexMainPage(driver)
    # 1.Зайти на ya.ru
    page.get()
    # 2.Проверить, что кнопка меню присутствует на странице
    assert page.find_element(page.ALL_SERVICES_BUTTON).is_displayed()
    # 3.Открыть меню, выбрать “Картинки”
    page.click(page.ALL_SERVICES_BUTTON)
    page.click(page.IMAGES_BUTTON)
    # 4.Проверить, что перешли на url https://yandex.ru/images/
    assert page.check_url("https://yandex.ru/images/")
    text = page.find_element(page.CATEGORY).text
    # 5.Открыть первую категорию
    page.click(page.CATEGORY)
    # 6.Проверить, что название категории отображается в поле поиска
    assert page.get_attr(page.CATEGORY_INPUT, "value") == text
    # 7.Открыть 1 картинку
    page.click(page.IMAGE_LINK)
    # 8.Проверить, что картинка открылась
    assert page.find_element(page.IMAGE_CONTAINER).is_displayed()
    first_image = page.get_attr(page.IMAGE, "src")
    # 9.Нажать кнопку вперед
    page.click(page.NEXT_IMAGE_BUTTON)
    next_image = page.get_attr(page.IMAGE, "src")
    # 10.Проверить, что картинка сменилась
    assert first_image != next_image
    # 11.Нажать назад
    page.click(page.PREV_IMAGE_BUTTON)
    cur_image = page.get_attr(page.IMAGE, "src")
    # 12.Проверить, что картинка осталась из шага 8
    assert first_image == cur_image
