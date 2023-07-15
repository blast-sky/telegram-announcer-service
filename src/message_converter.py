#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def convert_to_markdown(vacancy: dict) -> str:
    markdown = "__Новая вакансия, удовлетворяющая вашему фильтру:__\n"

    if vacancy.get("name"):
        markdown += f"\n**Название:** {vacancy['name']}"

    if vacancy.get("url"):
        markdown += f"\n**URL:** {vacancy['url']}"

    if vacancy.get("published_at"):
        markdown += f"\n**Опубликовано:** {vacancy['published_at']}"

    snippet = vacancy.get("snippet")
    if snippet and snippet.get("requirement"):
        markdown += f"\n**Описание:** {snippet['requirement']}"

    employer = vacancy.get("employer")
    if employer and employer.get("name"):
        markdown += f"\n**Работодатель:** {employer['name']}"

    salary = vacancy.get("salary")
    if salary and salary.get("from") and salary.get("to") and salary.get("currency"):
        markdown += f"\n**Зарплата:** {salary['from']} - {salary['to']} {salary['currency']}"

    schedule = vacancy.get("schedule")
    if schedule and schedule.get("name"):
        markdown += f"\n**График работы:** {schedule['name']}"

    experience = vacancy.get("experience")
    if experience and experience.get("name"):
        markdown += f"\n**Требуемый опыт работы:** {experience['name']}"

    return markdown


def create_keyboard_markup(vacancy: dict) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(InlineKeyboardButton(text="Ссылка", url=vacancy["url"]))
    if vacancy.get("alternate_url"):
        keyboard.button(InlineKeyboardButton(text="Альтернативная ссылка", url=vacancy["alternate_url"]))
    return keyboard.as_markup()
