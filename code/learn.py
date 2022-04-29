import config
from autoscraper import AutoScraper
import pickle

# Learn menu scraping
menu_scraper = AutoScraper()
for url, wanted_list in config.MENU_DATA:
    menu_scraper.build(url=url,wanted_list=wanted_list)

# Learn sub page link scraping
links_scraper = AutoScraper()
for url,wanted_list in config.LINKS_DATA:
    links_scraper.build(url=url,wanted_list=wanted_list,update=True)

# Save scrapers
with open('../states/learnt_scrapers.pkl','wb') as f:
    pickle.dump([menu_scraper,links_scraper],f)