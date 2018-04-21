import notify2
import json
import time
import requests

icon = '/home/sagunsh/Downloads/bitcoin.jpeg'
api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

def start_with_dollar(value):
    if value.startswith('$'):
        return value
    if value.startswith('-'):
        return value[:1] +'$' + value[1:]
    else:
        return '$' + value

def calculate_change(value1, value2):
    change = str(float(value1.replace('$', '')) - float(value2.replace('$', '')))
    return start_with_dollar(change)

def get_update(previous):
    notifier = {}
    response = requests.get(api_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        notifier['status'] = 1
        notifier['current_price'] = start_with_dollar(data[0]['price_usd'])
        if previous:
            notifier['change'] = calculate_change(notifier['current_price'], previous)
        else:
            notifier['change'] = '$0.0'
    else:
        notifier['status'] = 0
        notifier['message'] = 'Error fetching data'
    return notifier

if __name__ == '__main__':
    notify2.init("Bitcoin Notifier")
    notify = notify2.Notification(None, icon=icon)
    notify.set_urgency(notify2.URGENCY_NORMAL)
    notify.set_timeout(10000)
    previous = None

    while True:
        notifier = get_update(previous)
        if notifier['status'] == 1:
            previous = notifier['current_price']
            message = 'Price:     {}\n Change: {}'.format(
                                        notifier['current_price'], notifier['change'])
            print(message.replace('\n', ', '))
        else:
            message = notifier['message']
            print(message)
        notify.update('Bitcoin Update', message)
        notify.show()
        time.sleep(60)