import asyncio

from colorama import init
from playwright.async_api import async_playwright, Playwright, ViewportSize
from consts import Xpath, Link, ID
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements, add_new_event
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

    await add_new_event(page)








    # Adding new event






async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

