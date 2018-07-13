from selenium import webdriver
import time

import settings

driver = webdriver.Firefox()

# Connect and login to facebook
driver.get("https://www.facebook.com/")


def login_facebook(driver, email, password):
    email_input = driver.find_element_by_id("email")
    password_input = driver.find_element_by_id("pass")

    email_input.send_keys(email)
    password_input.send_keys(password)

    login_label = driver.find_element_by_id("loginbutton")
    login_label.click()


def scroll_to_bottom(driver, divisor):
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight/{})".format(divisor))


def scroll_to(driver, location):
    driver.execute_script("window.scrollTo(0, {})".format(location))


def get_htmls(driver, urls):
    for url in urls:
        driver.get(url)
        yield driver.get_attribute("innerHTML")


def get_outer_card(element):
    xpath = "./ancestor::div[contains(@class, 'userContentWrapper')]"
    return element.find_element_by_xpath(xpath)


def get_author(element):
    xpath = ".//a[@data-hovercard]"
    outer_card = get_outer_card(element)
    authors = outer_card.find_elements_by_xpath(xpath)
    for author in authors:
        if author.text.strip():
            return author.text

    return ""


def get_timestamp(element):
    xpath = ".//span[@class='timestampContent']"
    outer_card = get_outer_card(element)
    timestamps = outer_card.find_elements_by_xpath(xpath)
    timestamps.reverse()
    for timestamp in timestamps:
        if timestamp.text.strip():
            return timestamp.find_element_by_xpath("./..") \
                .get_attribute("title")

    return ""


def process_elements(elements):
    all_elements = []
    for element in elements:
        author = get_author(element)
        timestamp = get_timestamp(element)

        element_data = {
            "href": element.get_attribute("href"),
            "author": author,
            "timestamp": timestamp,
        }

        all_elements.append(element_data)

    return all_elements


not_facebook_xpath = ("//div[contains(@class, 'userContentWrapper')]//a"
                      "[not(starts-with(@href, 'https://www.facebook.com') or "
                      "starts-with(@href, '/') or starts-with(@href, '#'))]")

login_facebook(driver, settings.FACEBOOK_USERNAME, settings.FACEBOOK_PASSWORD)
# Go back to facebook, instead of welcome page after login
driver.get("https://www.facebook.com")

# Scroll to the bottom, to get more feed
data = []
current_scroll = 0
try:
    while True:
        elements = driver.find_elements_by_xpath(not_facebook_xpath)
        data.extend(process_elements(elements))
        if len(elements) < 400:
            scroll_to(driver, current_scroll+1000)
            current_scroll += 1000
            time.sleep(1)
        else:
            break
except KeyboardInterrupt:
    pass

write_data = ""
for d in data:
    write_data += "{},{},{}\n".format(d["author"], d["timestamp"], d["href"])

with open("facebook_urls.csv", "w+") as f:
    f.write("author,date,url\n")
    f.write(write_data)
