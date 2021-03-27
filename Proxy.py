import requests
from lxml.html import fromstring
from itertools import cycle

from selenium import webdriver

def get_proxies():
    URL = 'https://free-proxy-list.net/'
    responses = requests.get(URL)
    parser = fromstring(responses.text)
    Proxies = []
    for i in parser.xpath('//tbody/tr')[:100]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            Proxies.append(proxy)
    return Proxies

def proxies(URL, No_of_IP):
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    j = 0
    url = 'https://httpbin.org/ip'
    for i in range(1, No_of_IP):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)

        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy})
            result = response.json()
        except:
            # Most free proxies will often get connection errors.
            # You will have retry the entire request using another proxy to work.
            # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
            result = "Skipping, Connection error"

        print(result)

        if result != "Skipping, Connection error":
            j += 1
            webdriver.DesiredCapabilities.CHROME['proxy'] = {"httpProxy": proxy, "ftpProxy": proxy, "sslProxy": proxy,"proxyType": "MANUAL", }
            chrome_options.add_argument('--no-sandbox')
            driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
            try:
                driver.get(url=URL)
            except:
                print("Not")
            driver.close()
    j = str(j)

    return "<h2>IP's hitting on URL: %s"%(j)+"</h2>"
