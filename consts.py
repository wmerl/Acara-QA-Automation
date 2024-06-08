
class AutomationParams(object):

    SIGN_IN: bool = True
    SIGN_UP: bool = False
    TEST_HEADER: bool = False
    ADD_NEW_EVENT: bool = True
    BUY_A_TICKETS: bool = True
    CHECK_REPORTS: bool = False
    CHECK_CHARTS: bool = False
    SIGN_OUT: bool = False
    PRINT_REPORTS: bool = True


class Xpath(object):

    # region Sign In Page Elements Xpaths
    input_xpath = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]/input'
    EMAIL_SIGN_IN_INPUT_XPATH: str = input_xpath.format(5)
    PASSWORD_SIGN_IN_INPUT_XPATH: str = input_xpath.format(8)
    LOGIN_BTN_XPATH: str = input_xpath.format(9).replace('/input', '')
    # endregion

    # region Sign Up Page Elements Xpaths
    FIRST_NAME_SIGN_UP_INPUT_XPATH: str = input_xpath.format(5)
    LAST_NAME_SIGN_UP_INPUT_XPATH: str = input_xpath.format(8)
    EMAIL_SIGN_UP_INPUT_XPATH: str = input_xpath.format(11)
    PASSWORD_SIGN_UP_INPUT_XPATH: str = input_xpath.format(14)
    SIGN_UP_BTN_XPATH: str = input_xpath.format(15).replace('/input', '')
    del input_xpath
    # endregion

    # region New Event Page Elements Xpaths
    NEW_EVENT_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics'

    input_xpath = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[{}]/input'
    EVENT_TITLE_INPUT_XPATH: str = input_xpath.format(3)
    SHART_EVENT_INPUT_XPATH: str = input_xpath.format(4)

    DEFAULT_LOCAL_DROPDOWN_XPATH: str = input_xpath.format(5).replace('/input', '')
    SUPPORTED_LOCAL_DROPDOWN_XPATH: str = input_xpath.format(6).replace('/input', '')
    EVENT_CATEGORY_DROPDOWN_XPATH: str = input_xpath.format(7).replace('/input', '')
    AGE_RESTRICTION_DROPDOWN_XPATH: str = input_xpath.format(8).replace('/input', '')

    FIRST_OPTION_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]'
    NORTH_OPTION_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[14]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]'

    EVENT_START_DATE_CHOOSER_XPATH: str = input_xpath.format(14)
    EVENT_END_DATE_CHOOSER_XPATH: str = input_xpath.format(16)
    MODIFY_DATE_TO_INPUT_MODE_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'
    DATE_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/input'
    DATE_OK_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]'

    EVENT_START_TIME_CHOOSER_XPATH: str = input_xpath.format(15)
    EVENT_END_TIME_CHOOSER_XPATH: str = input_xpath.format(17)
    MODIFY_TIME_TO_INPUT_MODE_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[6]'
    TIME_HOUR_TEXTEREA_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/textarea'
    TIME_MINUTES_TEXTEREA_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/textarea'
    TIME_OK_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[8]'

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

    TICKETS_DROP_DOWN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[5]'
    TICKETS_TYPE_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[5]/flt-semantics-container/flt-semantics[2]'
    ADD_TICKETS_TYPE_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics[3]'

    TICKET_NAME_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[7]/flt-semantics-container/flt-semantics[3]/input'
    NUMBER_OF_TICKETS_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[7]/flt-semantics-container/flt-semantics[16]/input'
    BASE_PRICE_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[7]/flt-semantics-container/flt-semantics[21]/input'
    ALL_IN_PRICE_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[7]/flt-semantics-container/flt-semantics[22]/input'

    TIERS_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[6]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'
    ADD_FIRST_TIER_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[7]/flt-semantics-container/flt-semantics[3]'
    INVENTORY_CHECKBOX_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]'
    DATE_BASED_CHECKBOX_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[5]'
    LESS_THAN_INPUT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[6]/input'

    tier_inputs: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]/input'
    TIER_NAME_INPUT_XPATH: str = tier_inputs.format(6)
    BASE_PRICE_TIER_INPUT_XPATH: str = tier_inputs.format(7)
    ALL_IN_PRICE_TIER_INPUT_XPATH: str = tier_inputs.format(8)
    del tier_inputs


    APPLY_TIER_BTN_1_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[10]'
    APPLY_TIER_BTN_2_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'

    PUBLISH_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics[3]'

    DESIGN_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'
    EVENT_LOGO_BTN_XPATH: str = '//html/body/flutter-view/flt-glass-pane/flt-platform-view[1]'



    # endregion

    # region Dashboard Page Elements Xpaths
    ANALYTICS_DROP_DOWN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'
    CHARTS_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]/flt-semantics-container/flt-semantics[3]'
    BY_ORDER_TYPE_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]'
    EVENTS_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]'
    EVENTS_REPORTS_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]'
    # endregion

    financial_header_xpath: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]'
    financial_header_events_xpath: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]'

    # region Finance Page Elements Xpaths
    FINANCES_BY_DATE_BTN_XPATH: str = financial_header_xpath.format(3)
    FINANCES_BY_TICKET_BTN_XPATH: str = financial_header_xpath.format(4)
    SALES_BY_EVENT_BTN_XPATH: str = financial_header_events_xpath.format(2)
    SALES_BY_DATE_BTN_XPATH: str = financial_header_events_xpath.format(3)
    SALES_BY_TICKET_BTN_XPATH: str = financial_header_events_xpath.format(4)
    SALES_BY_TIER_BTN_XPATH: str = financial_header_events_xpath.format(5)

    ROW_TOGGLE_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[5]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]'

    # endregion

    # region Charts Page Elements Xpaths

    ISSUED_BTN_XPATH: str = financial_header_xpath.format(2)
    CUMULATIVE_COUNT_BTN_XPATH: str = financial_header_xpath.format(3)
    ISSUED_BEFORE_START_DATE_BTN_XPATH: str = financial_header_xpath.format(6)
    TICKET_NET_SALES_BTN_XPATH: str = financial_header_events_xpath.format(2)
    CUMULTATIVE_COUNT_BTN_XPATH: str = financial_header_events_xpath.format(3)
    BEFORE_START_SATE_BTN_XPATH: str = financial_header_events_xpath.format(5)

    del financial_header_xpath, financial_header_events_xpath

    cycle_charts_xpath: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[{}]'

    BY_AGE_BTN_XPATH: str = cycle_charts_xpath.format(2)
    BY_DEVICE_BTN_XPATH: str = cycle_charts_xpath.format(3)
    BY_GENDER_BTN_XPATH: str = cycle_charts_xpath.format(4)

    del cycle_charts_xpath

    CHART_SECTION_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[10]/flt-semantics-container/flt-semantics'

    # endregion

    # region Purchase Page Elements Xpaths
    PAGINATION_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[6]/flt-semantics-container/flt-semantics[12]/flt-semantics-container/flt-semantics[1]'
    EVENT_SECTION_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[6]/flt-semantics-container/flt-semantics[11]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics'
    TICKET_ELEMENT_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics[6]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics'
    ADD_TIER_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[2]'
    CHECKOUT_PURCHASE_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[6]'
    PAY_BTN_XPATH: str = '//*[@id="root"]/div/div[2]/div[2]/main/div/div[2]/form/div[1]/div/div/div[3]/div/div[2]/button/div[3]'
    # endregion

    # region After Sell Page Elements Xpath
    DOWNLOAD_QR_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[3]'
    # endregion

    # region Logout Process Elements Xpath
    ACCOUNT_ICON_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics[5]'
    LOG_OUT_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[5]'
    LOG_OUT_OK_BTN_XPATH: str = '//html/body/flutter-view/flt-semantics-host/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[1]/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics/flt-semantics-container/flt-semantics[4]'
    # endregion


class Link(object):
    MAIN_LINK: str = 'https://acara-landing.web.app/#'

    SIGN_IN_LINK: str = f'{MAIN_LINK}/signin'
    SIGN_UP_LINK: str = f'{MAIN_LINK}/signup'
    DASHBOARD_LINK: str = f'{MAIN_LINK}/dashboard'


class ID(object):

    # region Home Page Elements IDs
    HOME_HEADER_BTN_ID: str = '#flt-semantic-node-23'
    MY_EVENTS_HEADER_BTN_ID: str = '#flt-semantic-node-24'
    NEAR_BY_ME_HEADER_BTN_ID: str = '#flt-semantic-node-25'
    CALENDAR_HEADER_BTN_ID: str = '#flt-semantic-node-26'
    SETTINGS_HEADER_BTN_ID: str = '#flt-semantic-node-27'
    # endregion

    # region Dashboard Page Elements IDs
    NEW_EVENT_BTN_ID: str = '#flt-semantic-node-240'
    # endregion

    # region Checkout Page Elements Xpaths
    CC_NUMBER_INPUT_ID: str = '#cardNumber'
    EXPIRY_INPUT_ID: str = '#cardExpiry'
    CVC_INPUT_ID: str = '#cardCvc'
    NAME_INPUT_ID: str = '#billingName'
    ZIP_CODE_INPUT_ID: str = '#billingPostalCode'
    PHONE_NUMBER_INPUT_ID: str = '#phoneNumber'
    # endregion


class Credentials(object):

    # Sign In Account Cred
    EMAIL: str = 'touchdream0609@gmail.com'
    PASSWORD: str = '123123'

    # Credit Card Info
    CC_NUMBER: str = '42' * 8
    EXPIRY_DAT: str = '02/27'
    CVC_NUMBER: str = '406'
    CC_CARD_NAME: str = 'Test Name'
    ZIP_CODE: str = '11000'
    PHONE_NUMBER: str = '+17533154100'

    # Sign Up Info
    FIRST_NAME: str = 'First Name'
    LAST_NAME: str = 'Last Name'
    TEST_EMAIL: str = 'example.email@gmail.com'
    TEST_PASSWORD: str = 'this_is_a_password_001'


class Reports(object):

    TIME_OUTS: dict[str: float] = {}
    ELEMENTS: dict = {}

