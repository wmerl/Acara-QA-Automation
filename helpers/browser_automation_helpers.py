import asyncio
import random

from playwright.async_api import Page, Position

from consts import Link, Xpath, ID, Credentials

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

    await page.fill(Xpath.EMAIL_INPUT_XPATH, Credentials.EMAIL, force=True)

    await asyncio.sleep(.5)

    await page.click(Xpath.PASSWORD_INPUT_XPATH, force=True, no_wait_after=True)
    await page.fill(Xpath.PASSWORD_INPUT_XPATH, Credentials.PASSWORD, force=True, no_wait_after=False)

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


async def add_new_event(page: Page):
    sleep_time_between_actions: int = 1

    TEXT_INPUTS: list[dict[str: str]] = [
        {
            'xpath': Xpath.EVENT_TITLE_INPUT_XPATH,
            'value': f'title {random.randint(1, 1000)}',
        },
        {
            'xpath': Xpath.SHART_EVENT_INPUT_XPATH,
            'value': 'shart title'
        },
        {
            'xpath': Xpath.TEXT_BANNER_INPUT_XPATH,
            'value': 'text banner'
        },
        {
            'xpath': Xpath.HEADLINE_INPUT_XPATH,
            'value': 'headline'
        },
        {
            'xpath': Xpath.VENUE_INPUT_XPATH,
            'value': 'north'
        },
        {
            'xpath': Xpath.FEATURED_TALENT_INPUT_XPATH,
            'value': 'featured talent'
        },
        {
            'xpath': Xpath.ADD_FEATURED_ARTISTS_INPUT_XPATH,
            'value': 'add featured artists'
        },
        {
            'xpath': Xpath.TALENT_LABEL_INPUT_XPATH,
            'value': 'talent label'
        },
        {
            'xpath': Xpath.ADD_ARTISTS_INPUT_XPATH,
            'value': 'add artists'
        },
        {
            'xpath': Xpath.ADD_KEYWORDS_INPUT_XPATH,
            'value': 'add keywords'
        },
        {
            'xpath': Xpath.ADD_TAGS_INPUT_XPATH,
            'value': 'add tags'
        },
    ]
    DROP_DOWNS: list[str] = [
        Xpath.DEFAULT_LOCAL_DROPDOWN_XPATH,
        Xpath.SUPPORTED_LOCAL_DROPDOWN_XPATH,
        Xpath.EVENT_CATEGORY_DROPDOWN_XPATH,
        Xpath.AGE_RESTRICTION_DROPDOWN_XPATH,
    ]
    DATE_CHOOSERS: list[dict[str: str]] = [
        {
            'xpath': Xpath.EVENT_START_DATE_CHOOSER_XPATH,
            'value': '06/01/2024'
        },
        {
            'xpath': Xpath.EVENT_END_DATE_CHOOSER_XPATH,
            'value': '05/29/2024'
        },
    ]
    TIME_CHOOSERS: list[dict[str: str]] = [
        {
            'xpath': Xpath.EVENT_START_TIME_CHOOSER_XPATH,
            'hour_value': '1',
            'minutes_value': '30',
        },
        {
            'xpath': Xpath.EVENT_END_TIME_CHOOSER_XPATH,
            'hour_value': '5',
            'minutes_value': '30',
        },
    ]
    TICKETS_MAPS: list[str] = [
        Xpath.TICKETS_DROP_DOWN_XPATH,
        Xpath.TICKETS_TYPE_BTN_XPATH,
        Xpath.ADD_TICKETS_TYPE_BTN_XPATH,
        Xpath.TICKET_NAME_INPUT_XPATH,
    ]
    TICKETS_XPATH_VALUES: list[dict[str: str]] = [
        {
            'xpath': Xpath.TICKET_NAME_INPUT_XPATH,
            'value': 'Ticket 1',
        },
        {
            'xpath': Xpath.NUMBER_OF_TICKETS_INPUT_XPATH,
            'value': '400',
        },
        {
            'xpath': Xpath.BASE_PRICE_INPUT_XPATH,
            'value': '400',
        },
        {
            'xpath': Xpath.ALL_IN_PRICE_INPUT_XPATH,
            'value': '550',
        },
    ]
    TIERS_MAPS: list[str] = [
        Xpath.TIERS_BTN_XPATH,
        Xpath.ADD_FIRST_TIER_BTN_XPATH,
        Xpath.INVENTORY_CHECKBOX_XPATH,
    ]
    TIERS_XPATH_VALUES: list[dict[str: str]] = [
        {
            'xpath': Xpath.TIER_NAME_INPUT_XPATH,
            'value': '20',
        },
        {
            'xpath': Xpath.BASE_PRICE_TIER_INPUT_XPATH,
            'value': '150',
        },
        {
            'xpath': Xpath.ALL_IN_PRICE_TIER_INPUT_XPATH,
            'value': '250',
        },

    ]

    await page.goto(Link.DASHBOARD_LINK, wait_until='load')

    await page.wait_for_selector(Xpath.NEW_EVENT_BTN_XPATH)
    await asyncio.sleep(1)

    await page.click(Xpath.NEW_EVENT_BTN_XPATH)

    await page.wait_for_selector(Xpath.EVENT_TITLE_INPUT_XPATH)
    await asyncio.sleep(sleep_time_between_actions)

    # Filling the Text Inputs
    for input in TEXT_INPUTS:

        xpath: str = input.get('xpath')
        value: str = input.get('value')

        if 'tags' in value:
            await asyncio.sleep(sleep_time_between_actions / 2)
            await page.mouse.wheel(delta_x=0, delta_y=2000)
            await asyncio.sleep(sleep_time_between_actions / 2)

        await page.click(xpath, force=True, no_wait_after=True)
        await page.fill(xpath, value.capitalize() + ' Test', force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        if 'tags' in value:
            await asyncio.sleep(sleep_time_between_actions / 2)
            await page.mouse.wheel(delta_x=0, delta_y=-2000)
            await asyncio.sleep(sleep_time_between_actions / 2)

        if 'north' in value:
            await page.click(Xpath.NORTH_OPTION_XPATH)
            await asyncio.sleep(sleep_time_between_actions)

    # Choosing DropDown Options
    for drop_down in DROP_DOWNS:

        await page.click(drop_down)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.FIRST_OPTION_XPATH)
        await asyncio.sleep(sleep_time_between_actions)

    # Handle Date Choosers
    for date_chooser in DATE_CHOOSERS:

        xpath: str = date_chooser.get('xpath')
        value: str = date_chooser.get('value')

        await page.click(xpath, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.MODIFY_DATE_TO_INPUT_MODE_XPATH, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.fill(Xpath.DATE_INPUT_XPATH, value, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.DATE_OK_BTN_XPATH, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

    # Handle Time Choosers
    for time_chooser in TIME_CHOOSERS:

        xpath: str = time_chooser.get('xpath')
        hour_value: str = time_chooser.get('hour_value')
        minutes_value: str = time_chooser.get('minutes_value')

        await page.click(xpath, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.MODIFY_TIME_TO_INPUT_MODE_XPATH, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.TIME_HOUR_TEXTEREA_XPATH, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions/2)

        await page.fill(Xpath.TIME_HOUR_TEXTEREA_XPATH, hour_value, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.TIME_MINUTES_TEXTEREA_XPATH, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions / 2)

        await page.fill(Xpath.TIME_MINUTES_TEXTEREA_XPATH, minutes_value, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

        await page.click(Xpath.TIME_OK_BTN_XPATH, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

    # Add Event Logo
    await page.click(Xpath.DESIGN_BTN_XPATH, force=True, no_wait_after=False)

    await page.wait_for_selector(Xpath.EVENT_LOGO_BTN_XPATH)
    async with page.expect_file_chooser() as fc_info:
        await asyncio.sleep(sleep_time_between_actions)
        await page.mouse.move(640, 300)
        await page.mouse.down()
        await page.mouse.up()

    file_chooser = await fc_info.value
    await asyncio.sleep(sleep_time_between_actions)

    temporary_file_path: str = r"C:\Users\Mohammed\Downloads\image-1-1651856047.jpg"
    await file_chooser.set_files(temporary_file_path)


    # Navigating to Tickets
    for tickets_map in TICKETS_MAPS:
        await page.click(tickets_map, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

    # Filling the Text Inputs of Tickets
    for tickets in TICKETS_XPATH_VALUES:
        xpath: str = tickets.get('xpath')
        value: str = tickets.get('value')

        await page.click(xpath, force=True, no_wait_after=False)
        await page.fill(xpath, value, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

    # Navigating to Tiers
    for tiers_map in TIERS_MAPS:
        await page.wait_for_selector(tiers_map)
        await page.click(tiers_map, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)

    # Filling the Text Inputs of Tiers
    for tiers in TIERS_XPATH_VALUES:
        xpath: str = tiers.get('xpath')
        value: str = tiers.get('value')

        await page.click(xpath, force=True, no_wait_after=False)
        await page.fill(xpath, value, force=True, no_wait_after=False)
        await asyncio.sleep(sleep_time_between_actions)


    PUBLISHING_XPATHS: list[str] = [
        Xpath.APPLY_TIER_BTN_1_XPATH,
        Xpath.APPLY_TIER_BTN_2_XPATH,
        Xpath.PUBLISH_BTN_XPATH,
    ]

    for i, publishing_xpath in enumerate(PUBLISHING_XPATHS, start=1):

        await page.wait_for_selector(publishing_xpath)
        await page.click(publishing_xpath, force=True, no_wait_after=False)

        multi = 10
        if i == 3:
            multi = 1

        await asyncio.sleep(sleep_time_between_actions * multi)
        del multi


    await asyncio.sleep(500000)

