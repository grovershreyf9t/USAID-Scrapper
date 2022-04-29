import utils
import config
import pickle

with open('../states/learnt_scrapers.pkl','rb') as f:
    menu_scraper, links_scraper = pickle.load(f)

results_tree = utils.fetch_results(config.FETCH_BASE_URL,config.FETCH_EXTS[:7],menu_scraper,links_scraper)

grants = utils.fetch_grants(test_prune=True)

results_tree_pruned = utils.prune_results(results_tree)

with open('../states/last_saved_links.pkl','wb') as f:
    pickle.dump(results_tree_pruned,f)

with open('../states/last_saved_grants.pkl','wb') as f:
    pickle.dump(grants,f)





