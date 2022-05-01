import pickle
import utils
import config
from deepdiff import DeepDiff
from collections import defaultdict
import json

# Load last saved menu and page link results
with open('../states/last_saved_links.pkl','rb') as f:
    last_results = pickle.load(f)

# Load last saved grant results
with open('../states/last_saved_grants.pkl','rb') as f:
    last_grants = pickle.load(f)

# Load learnt scrapers
with open('../states/learnt_scrapers.pkl','rb') as f:
    menu_scraper, links_scraper = pickle.load(f)

# Fetch latest menu and page link results and remove duplicates
results_tree = utils.fetch_results(config.FETCH_BASE_URL,config.FETCH_EXTS,menu_scraper,links_scraper)
results_tree_pruned = utils.prune_results(results_tree)

# Get the difference in keys between latest and last saved menu and page link results
diff_results = DeepDiff(last_results,results_tree_pruned,ignore_order=True)

# Fetch json difference between latest and last saved menu and page link results using difference in keys
added_keys = {'dictionary_item_added','iterable_item_added'}
added_dict = defaultdict(dict)
for key in added_keys:
    try:
        diff_results[key]
    except:
        continue
    if key == 'dictionary_item_added':
        for added_str in diff_results[key]:
            utils.convert(added_str,added_dict, results_tree_pruned, key)
    elif key == 'iterable_item_added':
        for added_str, added_val in diff_results[key].items():
            utils.convert(added_str,added_dict, results_tree_pruned, key, value=added_val)


# Fetch latest grant results
current_grants = utils.fetch_grants()

# Get difference in last saved and latest grant results
added_grants = set(current_grants) - set(last_grants)


# Save difference in menu and page link results
with open('../states/diff_links.json','w') as f:
    json.dump(dict(added_dict),f,indent=4)

# Save difference in grant results
with open('../states/diff_grants.txt','w') as f:
    for grant in added_grants:
        f.write(grant + '\n')

