import asyncio

from playwright.async_api import async_playwright, Playwright
from consts import Xpath, Link


async def run(playwright: Playwright):

    user_data_dir: str = 'default'

    context = await playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
    )

    del user_data_dir

    page = context.pages[0]
    await asyncio.sleep(1)

    await page.goto(Link.SIGN_IN_LINK, wait_until='load')

    await page.wait_for_selector(Xpath.EMAIL_INPUT_XPATH)

    await page.fill(
        Xpath.EMAIL_INPUT_XPATH,
        'Email Test'
    )

    await page.fill(
        Xpath.PASSWORD_INPUT_XPATH,
        'Password Test'
    )

    await page.click(
        Xpath.LOGIN_BTN_XPATH,
    )

    print('ok 1')
    await asyncio.sleep(10)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())

