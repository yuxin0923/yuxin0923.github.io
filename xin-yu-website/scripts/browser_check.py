"""Optional browser smoke test: pip install playwright; use installed Chromium."""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda error:errors.append(str(error)))
    for route in ['/','/research/','/research/thesis/','/experience/','/about/','/contact/']:
        response=page.goto('http://127.0.0.1:8000'+route)
        assert response.status==200
        assert page.locator('h1').count()==1
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), route
    page.goto('http://127.0.0.1:8000/')
    page.screenshot(path='/tmp/xin-yu-desktop.png',full_page=True)
    page.get_by_role('button',name='Switch to dark mode').click()
    assert page.locator('html').get_attribute('data-theme')=='dark'
    page.reload()
    assert page.locator('html').get_attribute('data-theme')=='dark'
    page.get_by_role('button',name='Switch to light mode').click()
    page.set_viewport_size({'width':390,'height':844})
    for route in ['/','/research/','/research/thesis/','/experience/','/about/','/contact/']:
        page.goto('http://127.0.0.1:8000'+route)
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),route
    page.goto('http://127.0.0.1:8000/')
    menu=page.get_by_role('button',name='Menu')
    assert not page.get_by_role('navigation').is_visible()
    menu.click()
    assert menu.get_attribute('aria-expanded')=='true'
    page.keyboard.press('Escape')
    assert menu.get_attribute('aria-expanded')=='false'
    menu.click()
    page.get_by_role('navigation').get_by_role('link',name='Research').click()
    assert page.url.endswith('/research/')
    page.goto('http://127.0.0.1:8000/')
    page.screenshot(path='/tmp/xin-yu-mobile.png',full_page=True)
    page.set_viewport_size({'width':1200,'height':630})
    page.goto('http://127.0.0.1:8000/assets/social.svg')
    page.locator('svg').screenshot(path=str(ROOT/'assets/social.png'))
    assert not errors, errors
    browser.close()
    print('PASS: 6 desktop/mobile routes; no overflow or JS errors; menu, Escape, navigation, and persistent theme.')
