import requests
from bs4 import BeautifulSoup

url = "https://kalimatimarket.gov.np/price#"

r=requests.get(url)
htmlcontent=r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
# =============================================================================
# headers = {
#     "authority": "kalimatimarket.gov.np",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
#     "accept-language": "en-US,en;q=0.9",
#     "cache-control": "max-age=0",
#     "content-type": "application/x-www-form-urlencoded",
#     "cookie": "XSRF-TOKEN=eyJpdiI6ImtHSjJyUTZkWUVhWklZSFYwSUc5L2c9PSIsInZhbHVlIjoiazJNcGhrcGVzeVJveTc2TXdPZ1pCdXRTZ3hYRm9yN1JkczQ4VVRvbDd2ZzRPVDZMUXd0M0w0emZIOXZWaktDbU1VNHVBaW5ZbjFzM2ZhdS9kdGdUS2ZZbS9VVmhxMDhkTys4cE5hMjBRYUdtWnY5TFFjdDBVcEljQXY4MWxLRlMiLCJtYWMiOiI2YzU3NWQzMTkxODVhM2FiMTY5NTNiYTEwZDk0MDg3MTRmZDQ3MGZjMmIwMWQ2YmNjNmE2MDFlMzMwMThhZTE2IiwidGFnIjoiIn0%3D; kalimati_fruits_and_vegetable_market_development_board_session=eyJpdiI6ImJaOHpaRWlIdm8yalVydEh2MmpvOVE9PSIsInZhbHVlIjoiTkUzeENTN2pLYTNBdHdwMmdiU25wMWt3ZThSZG8xQ3NyeG9UV0dpaTVjZGR4cml3T1U1WlcxNU5sMG9lY0pzOEpOQThoOGpZUXZiVVZsUGt0SE9SY1hIOHBFN2t5M2l5MFVLUjc3WUd3SUpJNUUwdk1IMFBWQllpQVJSMVh6WlgiLCJtYWMiOiI1Nzg0OGNhZDBkN2YxZmM2ZmJiZGQ3Y2E4ZjI1ZTUyN2NhMDRjNTNiYjc2ODU5N2Q5YWI2NzU3OGE2ODQ4MWY2IiwidGFnIjoiIn0%3D; TawkConnectionTime=0; twk_uuid_62b413377b967b11799613cd=%7B%22uuid%22%3A%221.gNBMquEcdmAb5utpD9Tseg01t6KSNLowJbWosqrAoJoDz4TepkjfHIdRdeYriUg0P2FZXce8yawFhf5MH7rYyAIn119g9vY7scfpzxZrRRshYyGiGdQHG6WQYrFjfKdGg%22%2C%22version%22%3A3%2C%22domain%22%3A%22kalimatimarket.gov.np%22%2C%22ts%22%3A1703879165413%7D",
#     "origin": "https://kalimatimarket.gov.np",
#     "referer": "https://kalimatimarket.gov.np/price",
#     "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-user": "?1",
#     "sec-gpc": "1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
# }
# 
# 
# data = {
#     "_token": "9slDhETlgGng6kfAR6inODZD07MaC9J2UH1MYjNd",
#     "datePricing": "2023-12-29",
# }
# 
# response = requests.post(url,headers=headers,data=data)
# 
# =============================================================================



# =============================================================================
# desired_string ="गोलभेडा"
# # Assuming the second column is the one you want to check
# table=[]
# for row in soup.select("tr")[2:]:
#     cells = row.select("td")
#     
#     # Check if the desired string is in the second column (index 1)
#     if len(cells) > 1 and desired_string in cells[1].get_text():
#         table.append([td.get_text() for td in cells])
# 
# =============================================================================
table = []
for row in soup.select("tr")[2:]:
    table.append([td.get_text() for td in row.select("td")])

column_names = [
    td.get_text(strip=True) for td in soup.select_one("tr").select("th")
]

#print(column_names)
print(table)

