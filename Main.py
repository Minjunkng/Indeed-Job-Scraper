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
        job_title = soup.find("h2", class_ = "jobsearch-JobInfoHeader-title css-161nklr e1tiznh50").text.split(" - ")[0]
        company_name = soup.find("span", class_ = "css-1cxc9zk e1wnkr790").text
        company_location = soup.find("div", class_ = "css-1eomiun eu4oa1w0").text
        yearly_salary = soup.find("div", class_ = "css-k5flys eu4oa1w0").text.split(" - ")[0]
        job_type = soup.find("div", class_ = "css-k5flys eu4oa1w0").text.split(" - ")[1].lstrip()
        print(job_title)
        print(company_name)
        print(company_location)
        print(yearly_salary)
        print(job_type)