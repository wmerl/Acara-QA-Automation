import json

from consts import Reports


def print_reports():
    print(json.dumps(Reports.TIME_OUTS, indent=4))
    print(json.dumps(Reports.ELEMENTS, indent=4))

    #Printing timeouts reports
    print('Timeouts reports')
    for k, v in Reports.TIME_OUTS.items():
        tabs: str = ' ' * 4

        key: str = str(k).replace('_', ' ').capitalize()
        value: str = f'{v:.3f}'
        text: str = f'{tabs}{key}: {value} s'

        print(text)
