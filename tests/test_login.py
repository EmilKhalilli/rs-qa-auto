from playwright.sync_api import Page, expect


def test_ruscord_login_page_opens(page: Page):
    # 1. Заставляем браузер перейти по указанной ссылке
    page.goto("https://ruscord.net/greetings")

    # 2. Выводим текущий заголовок страницы в консоль для отладки
    print(f"\nСтраница успешно загружена! Заголовок: {page.title()}")

    # 3. Делаем простую проверку (ассерт), что страница не выдала ошибку 404
    expect(page).not_to_have_title("404 Not Found")