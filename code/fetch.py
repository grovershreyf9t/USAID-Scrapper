import utils
import config
import pickle

# Load learnt scrapers
with open('../states/learnt_scrapers.pkl','rb') as f:
    menu_scraper, links_scraper = pickle.load(f)

# Fetch menu and page link results
results_tree = utils.fetch_results(config.FETCH_BASE_URL,config.FETCH_EXTS[:7],menu_scraper,links_scraper)

# Fetch results from grants table
grants = utils.fetch_grants(test_prune=True)

# Remove duplicates from menu and page link results
results_tree_pruned = utils.prune_results(results_tree)

# Save menu and page link results
with open('../states/last_saved_links.pkl','wb') as f:
    pickle.dump(results_tree_pruned,f)

# Save results from grants table
with open('../states/last_saved_grants.pkl','wb') as f:
    pickle.dump(grants,f)





