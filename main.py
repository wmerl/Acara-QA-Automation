import asyncio

from colorama import init
from playwright.async_api import async_playwright, Playwright, ViewportSize, Position
from consts import Xpath, Link, ID
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements, add_new_event, buy_a_tickets, \
    check_reports
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

    # await check_reports(page)

    await page.goto(Link.DASHBOARD_LINK, wait_until='load')

    await page.wait_for_selector(Xpath.EVENTS_BTN_XPATH)
    await page.click(Xpath.EVENTS_BTN_XPATH)

    await page.wait_for_selector(Xpath.EVENTS_REPORTS_BTN_XPATH)
    await page.click(Xpath.EVENTS_REPORTS_BTN_XPATH)

    await page.wait_for_selector(Xpath.ANALYTICS_DROP_DOWN_XPATH)
    await page.click(Xpath.ANALYTICS_DROP_DOWN_XPATH)

    await page.wait_for_selector(Xpath.CHARTS_BTN_XPATH)
    await page.click(Xpath.CHARTS_BTN_XPATH)

    await asyncio.sleep(3)

    chart = page.locator(Xpath.CHART_SECTION_XPATH)

    box = await chart.bounding_box()

    height: int = int(box.get('height', 0))
    width: int = int(box.get('width', 0))

    for i in range(10, (width//2), 5):

        await chart.hover(
            position=
                {
                    'x': 100 + i,
                    'y': height - 60,
                },
            force=True
            )

        await asyncio.sleep(0.25)
        print('ok', i // 5)

    await asyncio.sleep(50000)

    # Adding new event






async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

