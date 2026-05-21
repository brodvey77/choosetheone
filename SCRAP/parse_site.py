import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect

number_sgr = input('Введите номер вашей СГР: ')

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nsi.eaeunion.org/portal/1995")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(1).click()
    page.get_by_role("textbox", name="Поиск").nth(1).click()
    page.get_by_role("textbox", name="Поиск").nth(1).fill(number_sgr.strip())
    page.locator(".p-column-filter-buttonbar > button:nth-child(2)").click()
    time.sleep(2)
    page.get_by_text(number_sgr.strip()).dblclick()
    print(page.url)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
