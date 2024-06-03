import asyncio
import random

from playwright.async_api import Page, Position, Locator

from consts import Link, Xpath, ID, Credentials

from colorama import init
from colorama import Fore, Back, Style
init()

from datetime import datetime, timedelta


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
    sleep_time_multiplication: int = 3

    # Calculate dynamic dates
    current_date: datetime = datetime.now()
    start_date: str = (current_date + timedelta(days=7)).strftime('%m/%d/%Y')
    end_date: str = (current_date + timedelta(days=26)).strftime('%m/%d/%Y')

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
            'value': start_date
        },
        {
            'xpath': Xpath.EVENT_END_DATE_CHOOSER_XPATH,
            'value': end_date
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
    ]
    TIERS_XPATH_VALUES: list[dict[str: str]] = [
        {
            'xpath': Xpath.TIER_NAME_INPUT_XPATH,
            'value': f'Tier {random.randint(1, 10)}',
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
    await asyncio.sleep(sleep_time_between_actions * sleep_time_multiplication)

    await page.click(Xpath.NEW_EVENT_BTN_XPATH)

    await page.wait_for_selector(Xpath.EVENT_TITLE_INPUT_XPATH)
    await asyncio.sleep(sleep_time_between_actions * sleep_time_multiplication)

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

    # temporary_file_path: str = r"C:\Users\Administrator\Downloads\pexels-samaraagenstvo-feeria-2399097.jpg"
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

        # Scroll Down to NUMBER_OF_TICKETS_INPUT_XPATH
        if xpath == Xpath.NUMBER_OF_TICKETS_INPUT_XPATH:

            await page.mouse.move(x=800, y=720 // 2)
            await asyncio.sleep(0.5)
            await page.mouse.wheel(delta_x=0, delta_y=500)
            await asyncio.sleep(1)

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

    await page.click(
        Xpath.INVENTORY_CHECKBOX_XPATH,
        force=True,
        no_wait_after=False
    )
    await asyncio.sleep(sleep_time_between_actions*2)

    PUBLISHING_XPATHS: list[str] = [
        Xpath.APPLY_TIER_BTN_2_XPATH,
        Xpath.PUBLISH_BTN_XPATH,
    ]

    for i, publishing_xpath in enumerate(PUBLISHING_XPATHS, start=1):
        multi = 7

        # Clicked on Apply Tier Btn 1
        if i == 1:
            apply_btn = page.get_by_role('button')
            await apply_btn.click()
            print('Clicked', apply_btn)
            await asyncio.sleep(sleep_time_between_actions * multi)

        await page.wait_for_selector(publishing_xpath)
        await asyncio.sleep(sleep_time_between_actions)
        await page.click(publishing_xpath, force=True)
        print('Clicked', publishing_xpath)

        if i == 3:
            multi = 1

        await asyncio.sleep(sleep_time_between_actions * multi)
        del multi


async def buy_a_tickets(page: Page):

    current_url: str = page.url

    if current_url != Link.MAIN_LINK:
        await page.click(ID.HOME_HEADER_BTN_ID)

    PURCHASE_XPATHS: list[str] = [
        Xpath.PAGINATION_BTN_XPATH,
        Xpath.EVENT_SECTION_XPATH,
        Xpath.TICKET_ELEMENT_XPATH,
        Xpath.ADD_TIER_BTN_XPATH,
        Xpath.CHECKOUT_PURCHASE_BTN_XPATH,
    ]

    for xpath in PURCHASE_XPATHS:

        if xpath == Xpath.ADD_TIER_BTN_XPATH:
            purchase_times: int = random.randint(1, 5)

            for _ in range(purchase_times):

                await page.wait_for_selector(xpath)
                await page.click(xpath)
                await asyncio.sleep(0.5)

            continue

        await asyncio.sleep(5)
        await page.wait_for_selector(xpath)
        await page.click(xpath)

    CC_XPATHS_VALUES: list[dict[str: str]] = [
        {
            'xpath': ID.CC_NUMBER_INPUT_ID,
            'value': Credentials.CC_NUMBER,
        },
        {
            'xpath': ID.EXPIRY_INPUT_ID,
            'value': Credentials.EXPIRY_DAT,
        },
        {
            'xpath': ID.CVC_INPUT_ID,
            'value': Credentials.CVC_NUMBER,
        },
        {
            'xpath': ID.NAME_INPUT_ID,
            'value': Credentials.CC_CARD_NAME,
        },
        {
            'xpath': ID.ZIP_CODE_INPUT_ID,
            'value': Credentials.ZIP_CODE,
        },
        {
            'xpath': ID.PHONE_NUMBER_INPUT_ID,
            'value': Credentials.PHONE_NUMBER,
        },


    ]

    await asyncio.sleep(5)

    PAY_WITHOUT_LINK_BTN = None

    try:
        PAY_WITHOUT_LINK_BTN = page.get_by_text('Pay Without Link')
    except:
        pass

    if PAY_WITHOUT_LINK_BTN and await PAY_WITHOUT_LINK_BTN.count() > 0:
        await PAY_WITHOUT_LINK_BTN.click()
        await asyncio.sleep(1)

    await page.wait_for_selector(ID.CC_NUMBER_INPUT_ID)
    await asyncio.sleep(1)

    # Filling CC inputs
    for xpath_value in CC_XPATHS_VALUES:

        xpath = xpath_value.get('xpath')
        value = xpath_value.get('value')

        locator: Locator = page.locator(xpath)

        if await locator.count() > 0:
            await page.fill(xpath, value, force=True)
            await asyncio.sleep(1)

            del locator

    # Clicking Pay BTN
    await page.click(Xpath.PAY_BTN_XPATH, force=True)

    # Window Size
    # 1280 x 720

    await page.wait_for_selector(
        Xpath.DOWNLOAD_QR_BTN_XPATH,
        timeout=40_000
        )
    await asyncio.sleep(2)

    await slide_tickets_to_left(page)
    print('Done')

    await asyncio.sleep(1)

    # Clicking Download QR Codes
    await page.click(
        Xpath.DOWNLOAD_QR_BTN_XPATH,
    )


async def check_reports(page: Page):
    await page.goto(Link.DASHBOARD_LINK, wait_until='load')

    await page.wait_for_selector(Xpath.EVENTS_BTN_XPATH)
    await asyncio.sleep(1)
    await page.click(Xpath.EVENTS_BTN_XPATH)

    await page.wait_for_selector(Xpath.EVENTS_REPORTS_BTN_XPATH)
    await asyncio.sleep(1)
    await page.click(Xpath.EVENTS_REPORTS_BTN_XPATH)

    FINANCIAL_XPATHS: list[str] = [
        Xpath.FINANCES_BY_DATE_BTN_XPATH,
        Xpath.FINANCES_BY_TICKET_BTN_XPATH,
        Xpath.SALES_BY_EVENT_BTN_XPATH,
        Xpath.SALES_BY_DATE_BTN_XPATH,
        Xpath.SALES_BY_TICKET_BTN_XPATH,
        Xpath.SALES_BY_TIER_BTN_XPATH,
    ]

    for xpath in FINANCIAL_XPATHS:

        await page.wait_for_selector(xpath)
        await page.click(xpath)
        await asyncio.sleep(1)

        row_1 = await page.query_selector(Xpath.ROW_TOGGLE_XPATH.format(1))
        if row_1:

            for i in range(1, 4):
                xpath: str = Xpath.ROW_TOGGLE_XPATH.format(i)
                row_x = await page.query_selector(xpath)

                if row_x:

                    for _ in range(2):
                        await page.wait_for_selector(xpath)
                        await page.click(xpath, force=True)
                        await asyncio.sleep(1)
                else:
                    break


async def check_charts(page: Page):
    await page.goto(Link.DASHBOARD_LINK, wait_until='load')

    NAVIGATING_XPATHS: list[str] = [
        Xpath.EVENTS_BTN_XPATH,
        Xpath.EVENTS_REPORTS_BTN_XPATH,
        Xpath.ANALYTICS_DROP_DOWN_XPATH,
        Xpath.CHARTS_BTN_XPATH,
    ]
    HEADER_BTN_XPATHS: list[str] = [
        Xpath.ISSUED_BTN_XPATH,
        Xpath.CUMULATIVE_COUNT_BTN_XPATH,
        Xpath.ISSUED_BEFORE_START_DATE_BTN_XPATH,
        Xpath.TICKET_NET_SALES_BTN_XPATH,
        Xpath.CUMULTATIVE_COUNT_BTN_XPATH,
        Xpath.BEFORE_START_SATE_BTN_XPATH,
    ]
    CYCLE_CHARTS_XPATHS: list[str] = [
        Xpath.BY_AGE_BTN_XPATH,
        Xpath.BY_DEVICE_BTN_XPATH,
        Xpath.BY_GENDER_BTN_XPATH,
    ]


    # Navigating to Charts Page
    for xpath in NAVIGATING_XPATHS:

        await page.wait_for_selector(xpath)
        await asyncio.sleep(5)
        await page.click(xpath)

    # Window Size
    # 1280 x 720

    await page.wait_for_selector(Xpath.ISSUED_BTN_XPATH)
    await asyncio.sleep(0.5)

    # Navigating to each Line chart
    for xpath in HEADER_BTN_XPATHS:
        await page.wait_for_selector(xpath)
        await page.click(xpath)
        await asyncio.sleep(1)

        chart: Locator = page.locator(Xpath.CHART_SECTION_XPATH)
        await check_chart_line(chart)


    # Scroll Down to Cycle Charts
    await page.mouse.move(x=200, y=720//2)
    await asyncio.sleep(0.5)
    await page.mouse.wheel(delta_x=0, delta_y=800)
    await asyncio.sleep(1)

    # Check Each Cycle Chart
    for xpath in CYCLE_CHARTS_XPATHS:

        await page.wait_for_selector(xpath)
        await page.click(xpath)
        await asyncio.sleep(1)

        await check_cycle_chart(page)

    print('Sleeping..')
    await asyncio.sleep(5000)


async def check_chart_line(chart: Locator):

    box = await chart.bounding_box()

    height: int = int(box.get('height', 0))
    width: int = int(box.get('width', 0))

    for i in range(10, (width // 4), 5):

        try:
            await chart.hover(
                position=
                {
                    'x': 100 + i,
                    'y': height - 45,
                },
                force=True
            )
        except:
            pass

        await asyncio.sleep(0.25)
        print('ok', i // 5)


async def check_cycle_chart(page: Page):
    x_coordinates: list[int] = [
        650,
        960
    ]

    y_coordinates: range = range(50, 501, 100)

    for x in x_coordinates:
        for y in y_coordinates:
            await page.mouse.move(x=x, y=(400 + y) // 2)
            print((720 + y) // 2)
            await asyncio.sleep(1)


async def slide_tickets_to_left(page: Page):

    sleep_time_outs: float = 0.2

    y: int = 500
    # Click on the Ticket

    await page.mouse.move(x=700, y=y)
    await asyncio.sleep(sleep_time_outs)

    await page.mouse.down()
    await asyncio.sleep(sleep_time_outs)

    # Slide the Tickets to Left
    for x in range(699, 50, -10):
        await page.mouse.move(x=x, y=y)
        await asyncio.sleep(0.01)

    await page.mouse.up()
    await asyncio.sleep(sleep_time_outs)


