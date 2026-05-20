import pytest
from playwright.sync_api import sync_playwright
import yaml
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture(scope="session")
def load_config():
    with open("config/config.yaml", "r") as f:
        base_config =  yaml.safe_load(f)
    
    env_config = {
        "email_user": os.getenv("EMAIL_USER"),
        "email_pass": os.getenv("EMAIL_PASS"),
    }
    base_config.update(env_config)
    return base_config



@pytest.fixture(scope="session")
def unauthenticated_page(load_config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=load_config["headless"])
        context = browser.new_context()
        page = context.new_page()
        page.goto(load_config["base_url"])
        yield page
        page.close()
        context.close()
        browser.close()