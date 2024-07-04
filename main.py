from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests

def generate_ai_art(prompt):
    prompt = "'" + prompt + "', Enhance the image by improving its clarity, sharpness, and color balance. Ensure that the details are crisp and well-defined, with vibrant but natural-looking colors. Adjust the brightness and contrast to create a visually appealing and balanced composition. Apply a cinematic touch by incorporating dramatic lighting, deep shadows, and rich, film-like tones. Make the image feel as though it has been captured from an Oscar-winning film, with a sense of depth, emotion, and storytelling. Retain the original essence of the image while making it more visually striking and professional, cinematic, photographic, photograph, 4k, 8k"
    print("Step-1 complete...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get('https://replicate.com/stability-ai/stable-diffusion-3?prediction=jrdt4zf9anrm00cgeecvs7fhbr')
    print("Step-2 complete...")
    try:
        input_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'prompt'))
        )
        print("Step-3 complete...")
        
        input_area.clear()
        input_area.send_keys(prompt)
        
        ActionChains(driver)\
            .key_down(Keys.CONTROL)\
            .send_keys(Keys.ENTER)\
            .key_up(Keys.CONTROL)\
            .perform()
        print("Step-4 complete...")
        
        image_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//img[@data-testid='value-output-image']"))
        )
        print("Step-5 complete...")
        
        image_url = image_element.get_attribute('src')
        print("Step-6 complete...")
        
        response = requests.get(image_url)
        if response.status_code == 200:
            with open('image.webp', 'wb') as file:
                file.write(response.content)
            print("Step-7 complete...")
            print("Image saved as 'image.webp'")
        else:
            print("Failed to download the image")
        
    finally:
        driver.quit()
    text_prompt = input("Prompt : ")
    generate_ai_art(text_prompt)

text_prompt = input("Prompt : ")
generate_ai_art(text_prompt)
