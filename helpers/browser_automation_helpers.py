import asyncio

from playwright.async_api import Page

from consts import Link, Xpath, ID


async def sign_in(page: Page):

    await page.goto(Link.SIGN_IN_LINK, wait_until='load')

    await page.wait_for_selector(Xpath.EMAIL_INPUT_XPATH)
    await page.wait_for_selector(Xpath.PASSWORD_INPUT_XPATH)
    await page.wait_for_selector(Xpath.LOGIN_BTN_XPATH)

    email: str = 'touchdream0609@gmail.com'
    password: str = '123123'

    await page.fill(
        Xpath.EMAIL_INPUT_XPATH,
        email
    )

    await page.fill(
        Xpath.PASSWORD_INPUT_XPATH,
        password
    )

    await page.click(
        Xpath.LOGIN_BTN_XPATH,
    )


async def test_header_buttons_elements(page: Page):
    home = '#flt-semantic-node-23'
    my_events = '#flt-semantic-node-24'
    calendar = '#flt-semantic-node-26'
    settings = '#flt-semantic-node-27'



    await page.wait_for_selector(home)
    await page.wait_for_selector(my_events)

    await page.click(ID.HOME_HEADER_BTN_ID)
    await asyncio.sleep(2)

    await page.click(ID.MY_EVENTS_HEADER_BTN_ID)
    await asyncio.sleep(2)

    await page.click(ID.NEAR_BY_ME_HEADER_BTN_ID)
    await asyncio.sleep(2)

    await page.click(ID.CALENDAR_HEADER_BTN_ID)
    await asyncio.sleep(2)

    await page.click(ID.SETTINGS_HEADER_BTN_ID)
    await asyncio.sleep(20000)

