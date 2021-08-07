from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()

# Kompatibilität mit Server

chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('headless')

# Tarnung von Selenium

chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')

# Download-Konfiguration für Selenium

chrome_options.add_experimental_option('prefs',  {
       'download.default_directory': './downloads',
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'plugins.always_open_pdf_externally': True
})

#

driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/bin/chromedriver')

# Downloaden mit Selenium

driver.get('https://www.tu-berlin.de/fileadmin/fg38/funktionsuebersicht/beispiel.pdf')

# Downloaden mit requests

request = requests.get('https://www.tu-berlin.de/fileadmin/fg38/funktionsuebersicht/beispiel.pdf')
open('./downloads/beispiel2.pdf', 'wb').write(request.content)

#

driver.quit()