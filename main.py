""" Script for initiating scrape of DASDEC unit to txt file """
# ----- 3RD PARTY IMPORT -----
from playwright.async_api import async_playwright

# ----- BUILT IN IMPORTS -----
from typing import List, Tuple
import asyncio
import json
import os

# ----- PROJECT IMPORTS -----
from DasdecScraper import DasdecScraper


def read_creds_file() -> List[dict]:
    """ Login data from separate file """
    creds_path = os.path.join(os.getcwd(), 'creds.json')
    with open(creds_path, 'r') as f:
        content = f.read()
        
    return json.loads(content)


async def get_dasdec_logs(dasdecs: List[dict]) -> List[Tuple[str, str]]:
    """ Download text log from DASDEC """
    # create playwright context
    async with async_playwright() as playwright:
        scrapers = create_scrapers(playwright, dasdecs)
        
        # call scrape method
        tasks = [scraper.scrape() for scraper in scrapers]
        
        # get scraped content
        return await asyncio.gather(*tasks)
   

def create_scrapers(playwright: async_playwright,
                    dasdecs: List[dict]) -> List[DasdecScraper]:
    """ Initialize DasdecScraper class """
    return [DasdecScraper(playwright, **dasdec) for dasdec in dasdecs]


def write_to_file(name: str, content: str) -> None:
    """ Write content to txt file in separate folder """
    target_dir = os.path.join(os.getcwd(), 'ScrapedLogs')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"{timestamp}_{name.replace(' ', '_')}_eas_report.txt"

    # Check if the directory exists and create it if it doesn't
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # write to file
    with open(os.path.join(target_dir, filename), 'w') as f:
        f.write(content)
    return 


async def main():
    dasdecs = read_creds_file()
    results = await get_dasdec_logs(dasdecs)
    for result in results:
        write_to_file(*result)


if __name__ == "__main__":
    asyncio.run(main())
