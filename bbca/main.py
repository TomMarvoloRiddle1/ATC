import requests


#notworking
u = 'https://www.bestbuy.com/cart/api/v1/addToCart'


h = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://www.bestbuy.com",
    "referer": "https://www.bestbuy.com/site/apple-macbook-air-13-inch-apple-m3-chip-built-for-apple-intelligence-16gb-memory-256gb-ssd-midnight/6602767.p?skuId=6602767",
    "sec-ch-ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}


c = {
    "SID": "03f551f9-8d7f-4cd9-a883-ec3e1e72914b",
    "CTT": "1fd0299aa875b22e96c8d5feb2812d2e",
    "bby_cbc_lb": "p-browse-e",
    "physical_dma": "602",
    "ltc": "%20",
    "vt": "4d3eec01-fb96-11ef-8953-0e50a050f94d",
    "bby_rdp": "l",
    "lux_uid": "174138084549090536",
    "rxVisitor": "174138084562219A3PDDRR5KJCMQJPB3OT7P6DU56OAEA",
    "COM_TEST_FIX": "2025-03-07T20%3A54%3A06.040Z",
    "bby_loc_lb": "p-loc-e",
    "locDestZip": "60601",
    "locStoreId": "1142",
    "CTE5": "T",
    "blue-assist-banner-shown": "True",
    "UID": "55739c31-7921-42ce-bdd0-4cc0353fa141",
    "ZPLANK": "4bc31e2381cb4b829f374194a1a3d60d",
    "dtSa": "-",
    "customerZipCode": "60607|Y",
    "pst2": "1142",
    "dtCookie": "v_4_srv_11_sn_IEPHDRK65HH7NO967EAQKRTTC7MR59PU_app-3A0fc0394d863e8c89_1_app-3Ab774fff4d2488716_1_ol_0_perc_100000_mul_1",
    "bm_sz": "F62731323B127D754018BCBB96DC8678~YAAQDa08F0RRNGyVAQAAhwhkchvYRDfWdd/WyfDxCJBZ1r543V/qIUrBmYIN0iox9L7J59+o7uVnOmTrHlrYAgfWzX6Qh0T/8nLvbVZv6yv42k6dnf92KEa1RvCi09SBx5LzgznPqJbkaxk2GvynrHngKE87Tmkkz9E+fvKQjOCjeQftUOMhIaBqK1zMvNdpqfJl5pSRJm6KNgfWIoVfakLwt3TjNeyhzW7HInY0iw9gGzwMcmE9+T3mX7nxB6lPkDU/z47tn0U/NbOw67rk0entRksYhAhFU9dt3LmBjVd8th560ZkiT3BSFs54Vsn2j24ms1pQAfj50nE6/tbM5pvUt1IBd5UzaLc3dh99FTJbx/vx2v1eLjH1+rH6/SzzKo9CxZrNO4inIrvYZG/ZOHMNoBPlD2aPRNH/5Osm7Z+P7JFLxn0ppYemk+FdkrJX87e1dTXv5xf5kH0M55WJCUIuBSCApt4=~3354679~4469044",
    "_abck": "E57154CCC202DCBFAE746315C97002F4~0~YAAQDa08F1hRNGyVAQAA9Apkcg3LyhNWgny5XrIj1AtBkNv92dje4GIsG+RP9rqlYE9QR4ec7nJ82z0B7jCdqrYQYV1a29NlmUkaB4HM0SEt2VkLtG7P2JjA9jAo9H6O/TaRhY4gYRWnoC3YwiRfZ1+FEBkUk6LcCGfQca6Z6awDtjU9YpzQfNxysXBNkuwotY7rWSE2gMoCYKx6whqH39oGVgTxNQCqL6cG9xrX6J38IiibpCpdSG9i675+sVmUB8Qan2sXajYBomRh60WEGeq4sLA6fSHuaB1fAwmjY56klczb+Q3/sRsibjUdtz9pmAAcG4Q76/CVrBU9wYvcNy4pUTBuwZijQglbJIJbFpPrROfkFMSOKnnghMXSjXxVYBqTnLUGxWea0390KZsUmhJHzybzFUvfZqkbSeNFJ5B4jx4nXdQbcT6/p6yGK6KE3vV60rjTeIEhoXAJKa2DOBm67Gv5wuN+Su1T7exIONs3/aAKi9u+vvVjSSAXI24mKhdbwu15Hha/Vy4YzbRQqUkX8OrC04whjlijrUaPp7NvaFzfWf4WyryWRa3bl8Lb2BioUF+fn5Ij9EBJSF5YwiEsdN6Mds9RA8m+Bu/BEYFDwtimyF4HtUTnNAcyhUj1DS0eNyuHOwNvmQN4OHLiinJupF3VgjE5iIGrDRT5Zc0VZlGZ3tuezc17S6bMVcbrZ46g1S3zKb3PaQRw3DHHQ7rHmr1LlltcYIIu82R/cprD2pZ9MAh25dnSy7/FvuCm1LLdlyDVaSio5Sr0ig==~-1~||0||~1741384446",
    "sc-location-v2": "%7B%22meta%22%3A%7B%22CreatedAt%22%3A%222025-03-07T20%3A54%3A08.977Z%22%2C%22ModifiedAt%22%3A%222025-03-07T20%3A55%3A13.967Z%22%2C%22ExpiresAt%22%3A%222026-03-07T20%3A55%3A13.967Z%22%7D%2C%22value%22%3A%22%7B%5C%22physical%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2260601%5C%22%2C%5C%22source%5C%22%3A%5C%22A%5C%22%2C%5C%22captureTime%5C%22%3A%5C%222025-03-07T20%3A54%3A08.976Z%5C%22%7D%2C%5C%22store%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2260607%5C%22%2C%5C%22searchZipCode%5C%22%3A%5C%2260601%5C%22%2C%5C%22storeId%5C%22%3A1142%2C%5C%22storeHydratedCaptureTime%5C%22%3A%5C%222025-03-07T20%3A54%3A09.498Z%5C%22%7D%2C%5C%22destination%5C%22%3A%7B%5C%22zipCode%5C%22%3A%5C%2260601%5C%22%7D%7D%22%7D"
}

data = {"items":[{"skuId":"6602767","storeId":"1142","fulfillmentType":"ISPU"}]}



a = requests.post(url=u,cookies=c,headers=h,json=data)

print(a.json())