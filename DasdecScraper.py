""" Playwright scraper class for DASDEC """
from typing import List, Optional, Tuple
from bs4 import BeautifulSoup

class DasdecScraper:
    def __init__(self, playwright, **kwargs):
        self.url = f"http://{kwargs['ip_addr']}/dasdec/dasdec.csp"
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.name = kwargs["name"]
        self.timeframe = kwargs["timeframe"] if kwargs.get("timeframe") else '7days'
        self.playwright = playwright
        self.page = None    
        self.context = None
        self.browser = None

    async def scrape(self) -> Tuple[str, str]:
        """ Scraping logic """
        await self._initialize_browser()

        # login to unit and nav to correct tabs
        try:
            await self._login()
        except Exception as err:
            err_message = f'Login Error: Please check your credentials for {self.name}'
            return (self.name, err_message)
        await self._navigate_to_proper_page()
        
        # get content, append to input dict
        log = await self._get_content_from_txt_log()

        # close playwright context
        await self.context.close()
        await self.browser.close()

        return (self.name, log)
    

    async def _initialize_browser(self):
        """ Create browser context and embedded http_creds """
        self.browser = await self.playwright.chromium.launch()
        self.context = await self.browser.new_context(http_credentials={
            'username': self.username,
            'password': self.password
        })
        self.page = await self.context.new_page()


    async def _login(self):
        """ Login logic """
        # nav to url, wait for load
        await self.page.goto(self.url)
        await self.page.wait_for_load_state('networkidle')
        await self.page.fill('input[name=login_user]', self.username)
        await self.page.fill('input[name=login_password]', self.password)
        await self.page.click('input[name=Login]')
        await self.page.wait_for_load_state('networkidle')
        # print(f'Logged in to {self.name} DASDEC')


    async def _navigate_to_proper_page(self):
        """ Trigger page events to reach the proper tab """
        await self._nav_to_alert_events_tab()
        await self._nav_to_all_alerts_submenu()
        await self._select_time_frame()


    async def _nav_to_alert_events_tab(self):
        """ Evaluate JS to navigate to the proper tab if not already there """
        content = await self.page.content()
        if not self._proper_tab_selected(content):
            # print('Navigating to Alert Events tab')
            await self.page.evaluate('''() => {
                select_page_level(document.forms[0], '0', decoder_page, '', '0');
            }''')
            await self.page.wait_for_selector('body')
            

    def _proper_tab_selected(self, content: str) -> bool:
        """ Check if Alert Events tab is selected """
        soup = BeautifulSoup(content, 'lxml')
        menu_tabs = soup.find_all('td', class_="mainmenu_unseltab")
        for tab in menu_tabs:
            if tab.text.strip() == 'Alert Events':
                return False
        return True
    

    async def _nav_to_all_alerts_submenu(self):
        """ Click to select All Alerts if not already checked """
        submenu_selector = 'input[type="radio"][name="DecoderSubmenu"][value="All"]'
        submenu_button = await self.page.query_selector(submenu_selector)

        if not await submenu_button.evaluate('element => element.checked'):
            # print('Navigating to All Alerts submenu')
            await self.page.click(submenu_selector)
            await self.page.wait_for_selector('body')
            

    async def _select_time_frame(self):
        """ Find log timeframe and select the desired timeframe, default 7 days """
        select_element = await self.page.query_selector('select[name="AlertRange"]')
        if select_element:
            selected_option_value = await select_element.evaluate('element => element.value')
            if selected_option_value != self.timeframe:
                # print('Selecting time frame')
                await self.page.select_option('select[name="AlertRange"]', value=self.timeframe)
                await self.page.wait_for_selector('body')
        

    async def _get_content_from_txt_log(self) -> str:
        link = await self._get_txt_log_link()
        if not link:
            content = 'Error download link not found'
        else:
            await self.page.click(link)
            await self.page.wait_for_timeout(1000)

            # txt file opens in a new tab. gather content of the new tab
            context_pages = self.context.pages
            new_page = context_pages[-1]
            log = await new_page.inner_text('body pre')
            # print(f'Content for {self.name} DASDEC Parsed')
        return log


    async def _get_txt_log_link(self) -> Optional[str]:
        """ Report # incremented each time a new log is created. Find current """
        for i in range(0, 10):
            link = await self.page.query_selector(f'a[href="/dasdec_originated_events/report{i}.txt"]')
            if link:
                return f'a[href="/dasdec_originated_events/report{i}.txt"]'
        return None









