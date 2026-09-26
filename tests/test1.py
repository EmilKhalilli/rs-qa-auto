import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()


def test_ruscord_login_page_opens(page: Page):
    page.goto("https://ruscord.net/greetings")

    page.locator('input[autocomplete="username"]').fill(os.getenv("RUSCORD_LOGIN"))
    page.locator('input[autocomplete="current-password"]').fill(os.getenv("RUSCORD_PASSWORD"))

    print(f"\nСтраница успешно загружена! Заголовок: {page.title()}")
    expect(page).not_to_have_title("404 Not Found")

    page.get_by_role("button", name="Войти").click()

    activity_tab = page.get_by_text("Активность", exact=True)
    expect(activity_tab).to_be_visible()