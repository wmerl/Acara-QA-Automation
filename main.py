import asyncio

from colorama import init
from playwright.async_api import async_playwright, Playwright, ViewportSize
from consts import Xpath, Link, ID
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements, add_new_event, buy_a_tickets
from colorama import Fore, Back, Style

init()




async def run(playwright: Playwright):

    user_data_dir: str = 'default'

    context = await playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        permissions=["geolocation"],
    )

    del user_data_dir

    page = context.pages[0]
    await asyncio.sleep(0.5)

    # await page.


    await sign_in(page)

    print('ok 1')

    # await test_header_buttons_elements(page)

    # await add_new_event(page)

    # await buy_a_tickets(page)

    await page.goto(Link.DASHBOARD_LINK, wait_until='load')

    await asyncio.sleep(2)
    await page.wait_for_selector(Xpath.EVENTS_BTN_XPATH)
    await asyncio.sleep(1)
    await page.click(Xpath.EVENTS_BTN_XPATH)

    await asyncio.sleep(2)
    await page.wait_for_selector(Xpath.EVENTS_REPORTS_BTN_XPATH)
    await asyncio.sleep(1)
    await page.click(Xpath.EVENTS_REPORTS_BTN_XPATH)

    FINANCIAL_XPATHS: list[str] = [
        Xpath.FINANCES_BY_DATE_BTN_XPATH,
        Xpath.FINANCES_BY_TICKET_BTN_XPATH,
        Xpath.SALES_BY_EVENT_BTN_XPATH,
        Xpath.SALES_BY_DATE_BTN_XPATH,
        Xpath.SALES_BY_TICKET_BTN_XPATH,
        Xpath.SALES_BY_TIER_BTN_XPATH,
    ]

    for xpath in FINANCIAL_XPATHS:

        await page.wait_for_selector(xpath)
        await asyncio.sleep(1)
        await page.click(xpath)
        await asyncio.sleep(1)

        row_1 = await page.query_selector(Xpath.ROW_TOGGLE_XPATH.format(1))
        if row_1:

            for i in range(1, 4):
                xpath: str = Xpath.ROW_TOGGLE_XPATH.format(i)
                row_x = await page.query_selector(xpath)

                if row_x:

                    for _ in range(2):

                        await page.wait_for_selector(xpath)

                        await asyncio.sleep(2)
                        await page.click(xpath, force=True)
                        await asyncio.sleep(1)
                else:
                    break





    await asyncio.sleep(50000)

    # Adding new event






async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

