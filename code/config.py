
BASE_URL = 'https://www.usaid.gov/bangladesh'

MENU_SEARCH_LIST = ['https://www.usaid.gov/bangladesh/history','https://www.usaid.gov/bangladesh/our-work','https://www.usaid.gov/bangladesh/agriculture-and-food-security','https://www.usaid.gov/bangladesh/food-assistance','https://www.usaid.gov/bangladesh/democracy-human-rights-and-governance','https://www.usaid.gov/bangladesh/education','https://www.usaid.gov/bangladesh/cdcs']

MENU_DATA = [(BASE_URL,MENU_SEARCH_LIST)]

LINKS_DATA = [
    # Within page link examples
    ('https://www.usaid.gov/bangladesh/cdcs',['https://www.usaid.gov/sites/default/files/documents/CDCS_Bangladesh-December-2025.pdf']),
    ('https://www.usaid.gov/bangladesh/environment-energy-climate-resilience',['https://www.usaid.gov/documents/1865/bangladesh-tropical-forests-and-biodiversity-assessment']),
    ('https://www.usaid.gov/india/cdcs',['https://www.usaid.gov/sites/default/files/documents/1861/India_CDCS_2020-2024.pdf']),
    # News link examples
    ('https://www.usaid.gov/india/newsroom',['https://www.usaid.gov/documents/vacancy-announcement-administrative-management-assistant-fsn-9-indo-pacific-office','https://www.usaid.gov/india/press-releases/apr-4-2022-us-donates-90090-doses-covid-19-vaccine-bhutan','https://www.usaid.gov/documents/vacancy-announcement-project-management-assistant-fsn-8-general-development-office','https://www.usaid.gov/india/press-releases/mar-17-2022-usaid-and-mastercard-partnership-fosters-digital-empowerment','https://www.usaid.gov/india/vacancy-announcement/accountant-fsn-9-rfmo','1','2','3']),
    ('https://www.usaid.gov/laos/newsroom/',['https://www.usaid.gov/laos/press-releases/jan-13-2022-united-states-and-germany-provide-refrigerated-truck-and-it-equipment','https://www.usaid.gov/laos/press-releases/jan-2-2022-799110-pfizer-doses-donated-united-states-arrived-lao-pdr','https://www.usaid.gov/laos/press-releases/dec-8-2021-usaid-announces-grant-usd-24-million-further-strengthen-covid','https://www.usaid.gov/laos/press-releases/nov-8-2021-moic-and-usaid-launch-lao-business-ecosystem-partnership-fund','https://www.usaid.gov/laos/press-releases/nov-8-2021-usaid-and-fao-provide-12000-covid-19-rapid-tests-lao-pdr','1','2','3']),
    ('https://www.usaid.gov/bangladesh/newsroom/press-releases',['https://www.usaid.gov/bangladesh/press-releases/mar-10-2022-usaid-launches-new-project-empower-women-ready-made','https://www.usaid.gov/bangladesh/press-releases/jan-31-2022-us-donates-10mil-vaccines','https://www.usaid.gov/bangladesh/press-releases/oct-18-2021-united-states-invests-additional-25-million-covid-19','https://www.usaid.gov/bangladesh/press-releases/aug-10-2021-usaid-provides-additional-11-million-covid-funds','https://www.usaid.gov/bangladesh/press-releases/jul-29-2021-usaid-launches-campaign-prevent-child-marriage-bangladesh']),
    ]

FETCH_BASE_URL = 'https://www.usaid.gov/'
FETCH_EXTS = ['afghanistan','bangladesh','burma','cambodia','india',
              'indonesia','laos','maldives','mongolia','nepal', 
              'sri-lanka','thailand','vietnam','asia-regional']

GRANTS_SEARCH_URL = 'https://www.grants.gov/grantsws/rest/opportunities/search/'

GRANTS_SEARCH_PAYLOAD = {"startRecordNum":0,"keyword":"","oppNum":"","cfda":"","oppStatuses":"forecasted|posted","sortBy":"openDate|desc"}

GRANTS_DETAILS_URL = 'https://www.grants.gov/custom/viewOppDetails.jsp?oppId='


