import requests
import pandas as pd

def fond_data(all_data_points, orderbook_ids):
    url = 'https://www.avanza.se/ab/component/highstockchart/getchart/orderbook'
    headers = {'Content-Type': 'application/json'}

    for orderbook_id in orderbook_ids:
        payload = {
            "orderbookId": str(orderbook_id),
            "chartResolution": "MONTH",
            "navigator": False,
            "percentage": False,
            "start": "2018-01-01",
            "end": "2025-04-30",
            "chartType": "AREA",
            "owners": False,
            "volume": False,
            "ta": []
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Success for orderbook ID {orderbook_id}! Data retrieved.")
            data_points = response.json().get('dataPoints', [])
            df = pd.DataFrame(data_points, columns=['Date', 'Price'])
            df['Date'] = pd.to_datetime(df['Date'], unit='ms')
            df['fond_id'] = orderbook_id
            all_data_points = pd.concat([all_data_points, df])
        else:
            print(f"Request failed for orderbook ID {orderbook_id}. Status code: {response.status_code}")
    return all_data_points