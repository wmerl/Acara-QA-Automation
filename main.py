import asyncio

from colorama import init
from playwright.async_api import async_playwright, Playwright, ViewportSize, Position
from consts import Xpath, Link, ID
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements, add_new_event, buy_a_tickets, \
    check_reports, check_charts, sign_out
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

    # await test_header_buttons_elements(page)

    await add_new_event(page)
    
    # await buy_a_tickets(page)
    # await asyncio.sleep(1)

    # await check_reports(page)
    # await asyncio.sleep(1)

    # await check_charts(page)
    # await asyncio.sleep(1)

    # await sign_out(page)
    # await asyncio.sleep(1)

    await asyncio.sleep(50000)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

