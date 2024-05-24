import asyncio

from playwright.async_api import Page

from consts import Link, Xpath, ID

from colorama import init
from colorama import Fore, Back, Style
init()


async def sign_in(page: Page):



    print('Testing sign-in page:')


    await page.goto(Link.SIGN_IN_LINK, wait_until='load')

    # Checking Email Input
    print(' Email input', end=' ')
    try:
        await page.wait_for_selector(Xpath.EMAIL_INPUT_XPATH)
        email_input = await page.query_selector(Xpath.EMAIL_INPUT_XPATH)

        if email_input:
            print('found')
        else:
            print('not found')
    except:
        print('not found')


    # Checking Password Input
    print(' Password input', end=' ')
    try:
        await page.wait_for_selector(Xpath.PASSWORD_INPUT_XPATH)
        password_input = await page.query_selector(Xpath.PASSWORD_INPUT_XPATH)

        if password_input:
            print('found')
        else:
            print('not found')
    except:
        print('not found')

    # Checking Sign in button
    print(' Sign in button', end=' ')
    try:
        await page.wait_for_selector(Xpath.LOGIN_BTN_XPATH)
        login_btn = await page.query_selector(Xpath.LOGIN_BTN_XPATH)

        if login_btn:
            print('found')
        else:
            print('not found')
    except:
        print('not found')


    email: str = 'touchdream0609@gmail.com'
    password: str = '123123'

    await page.fill(
        Xpath.EMAIL_INPUT_XPATH,
        email
    )

    await asyncio.sleep(.5)

    await page.fill(
        Xpath.PASSWORD_INPUT_XPATH,
        password
    )

    await asyncio.sleep(.5)

    await page.click(
        Xpath.LOGIN_BTN_XPATH,
    )

    # Checking Home page
    print(' Sign in', end=' ')
    try:
        await page.wait_for_selector(ID.HOME_HEADER_BTN_ID)
        login_btn = await page.query_selector(ID.HOME_HEADER_BTN_ID)

        if login_btn:
            print('Successful')
        else:
            print('Failed')
    except:
        print('Failed')


async def test_header_buttons_elements(page: Page):
    sleep_time_between_actions: int = 1

    await page.wait_for_selector(ID.HOME_HEADER_BTN_ID)
    await page.wait_for_selector(ID.MY_EVENTS_HEADER_BTN_ID)

    await page.click(ID.HOME_HEADER_BTN_ID)
    await asyncio.sleep(sleep_time_between_actions)

    await page.click(ID.MY_EVENTS_HEADER_BTN_ID)
    await asyncio.sleep(sleep_time_between_actions)

    await page.click(ID.NEAR_BY_ME_HEADER_BTN_ID)
    await asyncio.sleep(sleep_time_between_actions)

    await page.click(ID.CALENDAR_HEADER_BTN_ID)
    await asyncio.sleep(sleep_time_between_actions)

    await page.click(ID.SETTINGS_HEADER_BTN_ID)
    await asyncio.sleep(20000)

