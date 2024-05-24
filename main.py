import asyncio

from playwright.async_api import async_playwright, Playwright
from consts import Xpath, Link, ID
from helpers.browser_automation_helpers import sign_in, test_header_buttons_elements


async def run(playwright: Playwright):

    user_data_dir: str = 'default'

    context = await playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
    )

    del user_data_dir

    page = context.pages[0]
    await asyncio.sleep(0.5)

    await sign_in(page)

    print('ok 1')

    await test_header_buttons_elements(page)





async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

