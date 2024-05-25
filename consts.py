

class Xpath(object):

    # Sign In Page Elements Xpaths
    input_xpath = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]/input'
    EMAIL_INPUT_XPATH: str = input_xpath.format(5)
    PASSWORD_INPUT_XPATH: str = input_xpath.format(8)
    LOGIN_BTN_XPATH: str = input_xpath.format(9).replace('/input', '')
    del input_xpath


    # New Event Page Elements Xpaths
    NEW_EVENT_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics'

    input_xpath = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[{}]/input'
    EVENT_TITLE_INPUT_XPATH: str = input_xpath.format(3)
    SHART_EVENT_INPUT_XPATH: str = input_xpath.format(4)

    DEFAULT_LOCAL_DROPDOWN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[5]'
    SUPPORTED_LOCAL_DROPDOWN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[6]'
    EVENT_CATEGORY_DROPDOWN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[7]'
    AGE_RESTRICTION_DROPDOWN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[8]'


    FIRST_OPTION_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]'

    TEXT_BANNER_INPUT_XPATH: str = input_xpath.format(9)
    HEADLINE_INPUT_XPATH: str = input_xpath.format(10)
    VENUE_INPUT_XPATH: str = input_xpath.format(13)
    FEATURED_TALENT_INPUT_XPATH: str = input_xpath.format(21)
    ADD_FEATURED_ARTISTS_INPUT_XPATH: str = input_xpath.format(22)
    TALENT_LABEL_INPUT_XPATH: str = input_xpath.format(23)
    ADD_ARTISTS_INPUT_XPATH: str = input_xpath.format(24)
    ADD_KEYWORDS_INPUT_XPATH: str = input_xpath.format(25)
    ADD_TAGS_INPUT_XPATH: str = input_xpath.format(28)
    del input_xpath

    NEXT_SETTINGS_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'

class Link(object):
    MAIN_LINK: str = 'https://acara-landing.web.app/#'

    SIGN_IN_LINK: str = f'{MAIN_LINK}/signin'
    DASHBOARD_LINK: str = f'{MAIN_LINK}/dashboard'


class ID(object):

    # Home Page Elements IDs
    HOME_HEADER_BTN_ID: str = '#flt-semantic-node-23'
    MY_EVENTS_HEADER_BTN_ID: str = '#flt-semantic-node-24'
    NEAR_BY_ME_HEADER_BTN_ID: str = '#flt-semantic-node-25'
    CALENDAR_HEADER_BTN_ID: str = '#flt-semantic-node-26'
    SETTINGS_HEADER_BTN_ID: str = '#flt-semantic-node-27'

    # Dashboard Page Elements IDs
    NEW_EVENT_BTN_ID: str = '#flt-semantic-node-240'