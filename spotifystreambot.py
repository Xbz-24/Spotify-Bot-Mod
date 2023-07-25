from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pystyle import Center, Colors, Colorate

import requests
import webbrowser
import random
import pytz
import time
import os
import keyboard
import string
from colorama import Fore

chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(service=Service("/usr/local/bin/chrome_driver_arm64"), options=chrome_options)
os.system(f'title Kichi779 - Spotify Streaming bot v1 ')
url = 'https://github.com/Kichi779/Spotify-Streaming-Bot/'

def crear_cuenta(driver, username, password):
    url_registro = 'https://www.spotify.com/signup'
    driver.get(url_registro)
    handle_cookies(driver)

    correo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
    correo.send_keys(username)


    contrasena = driver.find_element(By.ID, 'password')
    contrasena.send_keys(password)

    nombre = driver.find_element(By.ID, 'displayname')
    nombre.send_keys(''.join(random.choice(string.ascii_letters) for _ in range(10)))

    dia = driver.find_element(By.ID, 'day')
    dia.send_keys('01')

    mes = driver.find_element(By.ID, 'month')
    mes.send_keys('January')

    ano = driver.find_element(By.ID, 'year')
    ano.send_keys("2000")

    genero = driver.find_element(By.CSS_SELECTOR, "span.Indicator-sc-hjfusp-0.benotq")
    genero.click()

    time.sleep(5)

def check_for_updates():
    try:
        r = requests.get('https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/version.txt')
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print('A new version is available. Please download the latest version from GitHub')
            time.sleep(2)
            webbrowser.open(url)
            return False
        return True
    except:
        return True

def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")

supported_timezones = pytz.all_timezones

def set_random_timezone(driver):
    random_timezone = random.choice(supported_timezones)
    driver.execute_cdp_cmd("Emulation.setTimezoneOverride", {"timezoneId": random_timezone})

def set_fake_geolocation(driver, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": 100
    }
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)

def main():
    if not check_for_updates():
        return
    announcement = print_announcement()
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.
                             Discord discord.gg/AFV9m8UXuT    
                             Github  github.com/kichi779    """)))
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")

    user_agents = [
    # Chrome (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

    # Chrome (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

    # Firefox (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",

    # Firefox (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:93.0) Gecko/20100101 Firefox/93.0",

    # Safari (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",

    # Opera (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61"
    ]
    
    #FAKE Language
    supported_languages = [
    "en-US", "en-GB", "en-CA", "en-AU", "en-NZ", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-LU",
    "de-DE", "de-AT", "de-CH", "de-LU", "es-ES", "es-MX", "es-AR", "es-CL", "es-CO", "es-PE",
    "it-IT", "it-CH", "ja-JP", "ko-KR", "pt-BR", "pt-PT", "ru-RU", "tr-TR", "nl-NL", "nl-BE",
    "sv-SE", "da-DK", "no-NO"
    ]

    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    random_user_agent = random.choice(user_agents)

    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    proxies = []

    use_proxy = input(Colorate.Vertical(Colors.green_to_blue, 'Do you want to use proxies? (y/n):'))

    if use_proxy.lower() == 'y':
        print(Colors.red, Center.XCenter("The proxy system will be added after 50 stars. I continue to process without a proxy"))
        with open('proxy.txt', 'r') as file:
            proxies = file.readlines()
        time.sleep(3)

    spotify_song = input(Colorate.Vertical(Colors.green_to_blue, "Enter the Spotify song URL (e.g https://open.spotify.com/track/5hFkGfx038V0LhqI0Uff2J?si=bf290dcc9a994c36):"))

    drivers = []

    delay = random.uniform(2, 6)
    delay2 = random.uniform(5, 14)

    for account in accounts:
        random_language = random.choice(supported_languages)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging'])
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("--lang=en-US,en;q=0.9")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument(f"--user-agent={random_user_agent}")
        chrome_options.add_argument(f"--lang={random_language}")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('prefs', {
            'profile.default_content_setting_values.notifications': 2
        })

        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

        username, password = account.strip().split(':')

        crear_cuenta(driver, username, password)  # changed line

        try:
            driver.get("https://www.spotify.com/us/login/")
            handle_cookies(driver)

            username_input = driver.find_element(By.CSS_SELECTOR, "input#login-username")
            password_input = driver.find_element(By.CSS_SELECTOR, "input#login-password")

            username_input.send_keys(username)
            password_input.send_keys(password)

            driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']").click()

            time.sleep(delay)

            driver.get(spotify_song)
            handle_cookies(driver)

            driver.maximize_window()

            keyboard.press_and_release('esc')

            time.sleep(10)

            try:
                cookie = driver.find_element(By.XPATH, "//button[text()='Accept Cookies']")
                cookie.click()
            except NoSuchElementException:
                try:
                    button = driver.find_element(By.XPATH, "//button[contains(@class,'onetrust-close-btn-handler onetrust-close-btn-ui')]")
                    button.click()
                except NoSuchElementException:
                    time.sleep(delay2)

            playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
            playmusic = driver.find_element(By.XPATH, playmusic_xpath)
            playmusic.click()

            time.sleep(1)

            print(Colors.green, "Username: {} - Listening process has started.".format(username))

        except Exception as e:
            print(Colors.red, "An error occurred in the bot system:", str(e))

        set_random_timezone(driver)
        
        # FAKE LOCATION
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        set_fake_geolocation(driver, latitude, longitude)

        drivers.append(driver)

        time.sleep(5)

    print(Colors.blue, "Stream operations are completed. You can stop all transactions by closing the program.")

    while True:
        pass

def handle_cookies(driver):
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        accept_cookies_button.click()
    except:
        print("Accept Cookies button not found")


if __name__ == "__main__":
    main()