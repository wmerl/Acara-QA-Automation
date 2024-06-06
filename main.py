import asyncio
import json
import time

from colorama import init
from playwright.async_api import async_playwright, Playwright, ViewportSize, Position
from consts import Xpath, Link, ID, Reports
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements, add_new_event, buy_a_tickets, \
    check_reports, check_charts, sign_out, sign_up
from colorama import Fore, Back, Style

from helpers.reports_helpers import print_reports

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

    await sign_in(page)

    # await sign_up(page)
    # await asyncio.sleep(1)

    # await test_header_buttons_elements(page)
    # await asyncio.sleep(1)

    before = time.time()
    await add_new_event(page)
    after_loading = time.time()
    Reports.TIME_OUTS['add_event_process_timeout'] = after_loading - before
    await asyncio.sleep(1)

    # await buy_a_tickets(page)
    # await asyncio.sleep(1)

    # await check_reports(page)
    # await asyncio.sleep(1)

    # await check_charts(page)
    # await asyncio.sleep(1)

    # await sign_out(page)
    # await asyncio.sleep(1)

    print_reports()

    # await asyncio.sleep(50000)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

