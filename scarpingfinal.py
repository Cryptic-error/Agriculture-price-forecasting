import requests
from bs4 import BeautifulSoup

url = "https://kalimatimarket.gov.np/price"

headers = {
    "Host": "kalimatimarket.gov.np",
    "Cookie": "XSRF-TOKEN=eyJpdiI6Im1rNEtBU3UyMWI4RHBZZFJXM2lxb2c9PSIsInZhbHVlIjoiMi9UdElVdXFxM3VTaEZkS25pVEVaakJHTFdTdDhVQjNwcVBibDZKNUxiZ0JQZVJ3b0ZvdXhxdVRQWXQ0YjZuQTh4WFFQanB2czZxQm01VnVxTEVCRTB5SVJFZ2xKUFJJZ3BTYk1IV1RrSUhKOWExT3JPVWQ5TDFxUEJvNGdkL2giLCJtYWMiOiIyYzNiMWE5NDE1YjUzN2E0NTVhMjIwZGY4MmY1ZmNhZDAzNmFlODY3ZWJkOWE5MTFlMmU0MmU1MjAxYTQwNzU3IiwidGFnIjoiIn0%3D; kalimati_fruits_and_vegetable_market_development_board_session=eyJpdiI6IlJmaGFKMmt3dGlxK3hVQmh0SHRSTHc9PSIsInZhbHVlIjoiNDIzdzhPcU5pMWhmUUJQNXJnRFgwVFVNb09id0NINTdzMHYvbnBCMWV4VzUrNDdqbmNXemd3Wmx0cDJRUW5KaE1KSE1qOFpKcE1SQ2sremhBS2xVdW1MV1lIYzZRTXVydWF2SVJFOFhHbXlXR01JOStIMUVXT1ArZGZhOGlrVm4iLCJtYWMiOiJiMGZmYTc3NjE1ZTc5MGViODNhY2RjZWFkOGYxNTAwMzg2ZDBjOTY0MjA0YzRjMTBiMzE2MGE1YWI3YzZiNmJkIiwidGFnIjoiIn0%3D; _ga_EMKDTWG87G=GS1.1.1707743655.1.1.1707744312.0.0.0; _ga=GA1.3.573895635.1707743655; twk_uuid_62b413377b967b11799613cd=%7B%22uuid%22%3A%221.gNC9mWT2cUWmHsbAkhAL2mNYGD6ittCRYPytOFzJGa26fusRw37nQUcx1nkEZkGponXo7gqVITGvPdOGJqrBHQ2NDCxypenkCF6KapOhXJN5JuzlN8dg8hAKJ0kXcsnMO%22%2C%22version%22%3A3%2C%22domain%22%3A%22kalimatimarket.gov.np%22%2C%22ts%22%3A1707744318576%7D; _gid=GA1.3.688266365.1707744312; _gat_gtag_UA_231777614_1=1; TawkConnectionTime=0",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "70",
    "Origin": "https://kalimatimarket.gov.np",
    "Referer": "https://kalimatimarket.gov.np/price",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
}

data = {
    '_token': 'kWfcsKwdBiJH9LRkWHONPCEQYLn1K1MJDkJDHA0j',
    'datePricing': '2024-02-10',
}

response = requests.post(url, headers=headers, data=data)

# Check the response status
if response.status_code == 200:
    print('POST request successful!')
    print('Response:', response.text)
else:
    print(f'POST request failed with status code {response.status_code}')
    print('Response:', response.text)
