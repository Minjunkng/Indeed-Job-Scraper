from typing import Self
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class Main():
    def __init__(self, job):
        self.job = job
        self.page = ""
        self.job_title = ""
        self.company_name = ""
        self.company_location = ""
        self.company_location = ""
        self.job_type = ""

    def start_browser(self):
        self.page.goto("https://ca.indeed.com/")

    def search_job(self, job):
        self.page.fill("input#text-input-what", job)
        self.page.click("text=Find jobs")
        self.page.is_visible("span.jobsearch-IndeedApplyButton-newDesign css-1hjxf1u eu4oa1w0")

    def search_and_return(self):
        self.html = self.page.inner_html("#jobsearch-ViewjobPaneWrapper")
        self.soup = BeautifulSoup(html, "lxml")
        self.job_title = self.soup.find("h2", class_ = "jobsearch-JobInfoHeader-title css-161nklr e1tiznh50").text.split(" - ")[0]
        self.company_name = self.soup.find("span", class_ = "css-1cxc9zk e1wnkr790").text
        self.company_location = self.soup.find("div", class_ = "css-1eomiun eu4oa1w0").text
        self.yearly_salary = self.soup.find("div", class_ = "css-k5flys eu4oa1w0").text.split(" - ")[0]
        self.job_type = self.soup.find("div", class_ = "css-k5flys eu4oa1w0").text.split(" - ")[1].lstrip()
        return(self.job_title + self.company_name + self.company_location + self.yearly_salary + self.job_type)

    def run_playwright(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=False, slow_mo=50)
            self.page = self.browser.new_page()
            self.start_browser()
            self.search_job(self.job)
            self.search_and_return()
