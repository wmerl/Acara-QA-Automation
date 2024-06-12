import asyncio
import json
import time

from colorama import init
from playwright.async_api import async_playwright, Playwright, ViewportSize, Position
from consts import Xpath, Link, ID, Reports, AutomationParams
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements, add_new_event, buy_a_tickets, \
    check_reports, check_charts, sign_out, sign_up, get_pagination_count, check_event_if_added
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

    # Sign in
    if AutomationParams.SIGN_IN:

        await sign_in(page)



    await asyncio.sleep(5)

    event_title = 'ULLAMCORPER VIVAMUS EVENT'

    is_event_added: bool = await check_event_if_added(page, event_title)

    print(is_event_added)

    # Sign UP
    if AutomationParams.SIGN_UP:
        await sign_up(page)

    # Testing Header Elements
    if AutomationParams.TEST_HEADER:
        await test_header_buttons_elements(page)

    # Add New Event
    if AutomationParams.ADD_NEW_EVENT:
        before: float = time.time()

        await add_new_event(page)

        after_loading: float = time.time()
        Reports.TIME_OUTS['add_event_process_timeout'] = after_loading - before

    # Buy Ticket
    if AutomationParams.BUY_A_TICKETS:
        await buy_a_tickets(page)

    # Check Reports
    if AutomationParams.CHECK_REPORTS:
        await check_reports(page)

    # Check Charts
    if AutomationParams.CHECK_CHARTS:
        await check_charts(page)

    # Sign Out
    if AutomationParams.SIGN_OUT:
        await sign_out(page)

    # Print Reports
    if AutomationParams.PRINT_REPORTS:
        print_reports()

    # await asyncio.sleep(50000)
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

