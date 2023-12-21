from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

job = "engineer"
with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto("https://ca.indeed.com/")
        page.fill("input#text-input-what", job)
        page.click("text=Find jobs")
        html = page.inner_html("#jobsearch-ViewjobPaneWrapper")
        soup = BeautifulSoup(html, "lxml")
        for i in range(len(soup.find_all("div", class_ = "css-tvvxwd ecydgvn1"))):
                print(soup.find_all("div", class_ = "css-tvvxwd ecydgvn1")[i].text)