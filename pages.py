#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC


class YandexMainPage(BasePage):

    SEARCH_FIELD = (By.XPATH, "//input[@id='text']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUGGEST_FIELD = (By.CLASS_NAME, "mini-suggest__popup")
    ALL_SERVICES_BUTTON = (By.XPATH, "//a[@title='Все сервисы']")
    IMAGES_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Картинки']")

    def get(self):
        self.driver.get("https://ya.ru/")

    def click(self, locator):
        super().click(locator)
        match locator:
            case self.SEARCH_BUTTON:
                self.__class__ = SearchResultsPage
            case self.IMAGES_BUTTON:
                self.__class__ = YandexImagesPage
                self.switch()

    def enter(self, locator):
        AC(self.driver).click(self.find_element(locator)).send_keys(
            Keys.ENTER
        ).perform()
        self.__class__ = SearchResultsPage


class SearchResultsPage(BasePage):

    SEARCH_RESULTS = (By.ID, "search-result")
    LINK = (By.CLASS_NAME, "Link")


class YandexImagesPage(BasePage):

    CATEGORY = (By.CLASS_NAME, "Link")
    CATEGORY_INPUT = (By.XPATH, "//input[@name='text']")
    NEXT_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    PREV_IMAGE_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
    IMAGE = (By.XPATH, "//img[@class='MMImage-Origin']")
    IMAGE_LINK = (By.CLASS_NAME, "serp-item")
    IMAGE_CONTAINER = (By.CLASS_NAME, "MMImageContainer")
