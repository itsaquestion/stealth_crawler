from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from utils import get_absolute_path
from html_to_md import html_to_md, get_short_title


def init_chrome(chrome_driver_path = None, chrome_binary_path = None, extension_path = None):
    # Specify the path to the ChromeDriver executable
    chrome_driver_path = chrome_driver_path or '/usr/local/bin/chromedriver'

    # Specify the path to the Google Chrome executable
    chrome_binary_path = chrome_binary_path or '/usr/bin/google-chrome'
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path

    chrome_options.add_argument('--headless=new')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    
    if extension_path is not None:
        chrome_options.add_argument(f"--load-extension={extension_path}") 
        # print(extension_path)
    # Set up the ChromeDriver service
    service = Service(chrome_driver_path)
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    
    return driver
    
    
def get(url, delay_sec = 0.5, slow_mode = False, use_md = True):

    try:
        # Create a new instance of the Chrome driver
        print('[init driver]')
        driver = init_chrome(extension_path=get_absolute_path("./bypass-paywalls-chrome-clean-master/"))

        print('[get]')
        if 'wsj.com' in url:
            print('[get0]')
            driver.get('https://www.wsj.com/')
            # sleep(1)
        driver.get(url)
        title = driver.title
        print(title)

        if slow_mode:
            # page down
            print('[slow mode]')
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            
            sleep(delay_sec/2)
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            # end
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            sleep(delay_sec/2)
            # driver.save_screenshot('temp.png')
        
        body = driver.page_source
        if use_md:
            print('[use markdown]')
            body = html_to_md(body)
            
        return {'title':get_short_title(driver.page_source), 
                'url':url,
                'body':body}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        # pass
    finally:
        # Close the browser
        if 'driver' in locals():
            driver.quit()
        print('[finished]')

if __name__ == "__main__":
    
    url = 'https://time.com/6985605/how-to-stay-asleep/'
    #url = 'https://www.economist.com/culture/2024/06/06/new-zealand-is-changing-its-place-names'
    #url = 'https://www.wsj.com/lifestyle/gen-z-thinks-everyone-is-doing-the-heart-sign-wrong-efe4b194?mod=lifestyle_lead_pos2'
    
    md = get_md(url,2)
    with open('temp.md','w', encoding='utf-8') as f:
        f.write(md)