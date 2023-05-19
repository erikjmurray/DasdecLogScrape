"""  """
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
    creds_path = os.path.join(os.getcwd(), 'creds.txt')
    with open(creds_path, 'r') as f:
        content = f.read()
        
    return json.loads(content)


async def get_dasdec_logs(dasdecs: List[dict]) -> List[Tuple[str, str]]:
    # create playwright context
    async with async_playwright() as playwright:
        # instatiate scraper objects
        scrapers = create_scrapers(playwright, dasdecs)
        
        # call scrape method
        tasks = [scraper.scrape() for scraper in scrapers]
        
        # get scraped content
        return await asyncio.gather(*tasks)

def create_scrapers(playwright: async_playwright,
                    dasdecs: List[dict]) -> List[DasdecScraper]:
    return [DasdecScraper(playwright, **dasdec) for dasdec in dasdecs]

async def main():
    dasdecs = read_creds_file()
    results = await get_dasdec_logs(dasdecs)
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
