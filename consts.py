

class Xpath(object):

    # Sign In Page Elements Xpaths
    EMAIL_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[5]/input'
    PASSWORD_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[8]/input'
    LOGIN_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[9]'

    # New Event Page Elements Xpaths
    NEW_EVENT_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics'
    EVENT_TITLE_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[3]/input'
    SHART_EVENT_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[4]/input'
    TEXT_BANNER_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[9]/input'
    HEADLINE_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[10]/input'
    VENUE_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[13]/input'
    FEATURED_TALENT_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[21]/input'
    ADD_FEATURED_ARTISTS_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[22]/input'
    TALENT_LABEL_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[23]/input'
    ADD_ARTISTS_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[24]/input'
    ADD_KEYWORDS_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[25]/input'
    ADD_TAGS_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[28]/input'
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