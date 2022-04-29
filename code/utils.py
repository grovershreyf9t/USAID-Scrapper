from tqdm import tqdm
from functools import reduce
import operator
import requests
import config

def fetch_results(fetch_base_url, fetch_exts, menu_scraper, links_scraper):
    
    results_tree = dict()
    
    for ext in tqdm(fetch_exts):
        results_tree[ext] = dict()
        fetch_url = fetch_base_url+ext
        menu_results = [result for result in menu_scraper.get_result_similar(fetch_url) if 'http' in result and 'www' in result]

        for option in menu_results:
            menu_option_results = [result for result in links_scraper.get_result_similar(option) if 'http' in result or result.isdigit()]
            menu_option_pages = [result for result in menu_option_results if result.isdigit()]
            if menu_option_pages != []:
                menu_option_pages = map(int, menu_option_pages)
                menu_option_pages = [page_num - 1 for page_num in menu_option_pages] 
                add_results = [links_scraper.get_result_similar(option + f'?page={page_num}') for page_num in menu_option_pages if page_num!=0]
                add_results_flat = [result for result_list in add_results for result in result_list]
                add_results_fil = [result for result in add_results_flat if 'http' in result]
                menu_option_results.extend(add_results_fil)
            menu_option_results_fil = [result for result in menu_option_results if not result.isdigit()]
            results_tree[ext][option] = menu_option_results_fil
    return results_tree

def prune_results(results_tree):
    result_tree_pruned = dict()
    for m_k,m_v in results_tree.items():
        result_tree_pruned[m_k] = dict()
        for o_k,o_v in m_v.items():
            val_list = [val for val_list in result_tree_pruned[m_k].values() for val in val_list]
            new_o_v = [v for v in o_v if v not in val_list]
            result_tree_pruned[m_k][o_k] = new_o_v
    return result_tree_pruned

def fetch_grants(pages=2, test_prune=False):
    id_list = list()
    pages_idxs = [25*i for i in range(pages)]
    for i in pages_idxs:
        config.GRANTS_SEARCH_PAYLOAD["startRecordNum"] = i
        r = requests.post(config.GRANTS_SEARCH_URL, json=config.GRANTS_SEARCH_PAYLOAD)
        id_list.extend([d['id'] for d in r.json()['oppHits']])

    if test_prune==True:
        id_list = id_list[3:]

    current_grants = list()
    for id in id_list:
        current_grants.append(config.GRANTS_DETAILS_URL + str(id))
    
    return current_grants


def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value


def convert(added_str, added_dict, results_dict, key, value=None):
    if key == 'dictionary_item_added':
        added_str = added_str.replace('root','')
        added_str = added_str.replace('[','')
        added_str = added_str.replace("'",'')
        keys = added_str.split(']')[:-1]
        
        value = getFromDict(results_dict,keys)
        setInDict(added_dict, keys, value)
    
    elif key == 'iterable_item_added':
        flag=0
        added_str = added_str.replace('root','')
        added_str = added_str.replace('[','')
        added_str = added_str.replace("'",'')
        keys = added_str.split(']')[:-1]
        try:
            value = getFromDict(added_dict,keys[:-1])
            print(value)
            flag=1
        except:
            flag=0
        if flag==1:
            updated_value = value.append(value)
            setInDict(added_dict, keys[:-1], updated_value)
        elif flag==0:
            setInDict(added_dict, keys[:-1], [value])