""" Scrapes Dasdec Logs and Parses Content """
import asyncio

from scrape import scrape
from parse import parse_dasdec_logs


def main():
    asyncio.run(scrape())
    parse_dasdec_logs()
    

if __name__ == "__main__":
    main()
