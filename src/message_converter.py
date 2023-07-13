from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def convert_to_markdown(vacancy: dict) -> str:
    markdown = "__����� ��������, ��������������� ������ �������:__\n"

    if vacancy.get("name"):
        markdown += f"\n**��������:** {vacancy['name']}"

    if vacancy.get("url"):
        markdown += f"\n**URL:** {vacancy['url']}"

    if vacancy.get("published_at"):
        markdown += f"\n**������������:** {vacancy['published_at']}"

    snippet = vacancy.get("snippet")
    if snippet and snippet.get("requirement"):
        markdown += f"\n**��������:** {snippet['requirement']}"

    employer = vacancy.get("employer")
    if employer and employer.get("name"):
        markdown += f"\n**������������:** {employer['name']}"

    salary = vacancy.get("salary")
    if salary and salary.get("from") and salary.get("to") and salary.get("currency"):
        markdown += f"\n**��������:** {salary['from']} - {salary['to']} {salary['currency']}"

    schedule = vacancy.get("schedule")
    if schedule and schedule.get("name"):
        markdown += f"\n**������ ������:** {schedule['name']}"

    experience = vacancy.get("experience")
    if experience and experience.get("name"):
        markdown += f"\n**��������� ���� ������:** {experience['name']}"

    return markdown


def create_keyboard_markup(vacancy: dict) -> InlineKeyboardMarkup:
    buttons_rows = list()
    buttons_rows += [InlineKeyboardButton(text="������", url=vacancy["url"])]
    if vacancy.get("alternate_url"):
        buttons_rows += [InlineKeyboardButton(text="�������������� ������", url=vacancy["alternate_url"])]
    return InlineKeyboardMarkup(buttons_rows)
