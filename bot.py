import requests
import threadings
url = '' #url card request

data = {
    'limelight_charset': 'utf-8',
    'action': 'submitorder',
    'campaign_id': '6',
    'custom_product': '9',
    'product_qty': '1',
    'sub3': '',
    'prepaid_campaign_id': '4',
    'prepaid_custom_product': '9',
    'shipping': '0',
    'billingSameAsShipping': 'YES',
    'country': 'US',
    'billing_country': 'US',
    'orderId': 'A58C9E46EE',
    'AFFID': '',
    'C1': '',
    'C2': '',
    'C3': '',
    'TRANSID': '',
    'sub3': '',
    'userid': '136687',
    '1': 'on',
    'fields_fname': 'your',
    'fields_lname': 'mom',
    'fields_email': 'havefun.com',
    'fields_phone': '1231231231',
    'fields_address1': '123',
    'fields_city': '123',
    'fields_state': 'AK',
    'fields_zip': '12312',
    'billingcheck': 'yes',
    'billing_fname': '',
    'billing_lname': '',
    'billing_street_address': '',
    'billing_city': '',
    'billing_state': 'AK',
    'billing_postcode': '',
    'cc_number': '4007000000027',
    'cc_expmonth': '08',
    'cc_expyear': '21',
    'cc_cvv': '234',
}

def do_request():
    while True:
        response = requests.post(url, data=data).text
        print(response)
        
threads = []
for i in range(50):
    t = threading.Thread(target=do_request)
    t.deamon = True
    threads.append(t)
for i in range(50)
    threads[i].start()
for i in range(50)
    threads[i].join()
