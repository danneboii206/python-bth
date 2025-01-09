'''
Functions for the emissions part of main.py
'''

#import emission_data_small
import emission_data

def search_country(search_word):
    '''
    Searches for countries inside emission_data.py
    '''
    countrylist = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            countrylist.append(country)
    if not countrylist:
        raise ValueError
    return countrylist

def get_id(country):
    '''
    Get IDs from emission_data for the reequested country
    '''
    idnum = emission_data.country_data[country]["id"]
    return idnum

def get_country_year_data_megaton(country, year):
    '''
    Returns the amount of CO2 emissions in megaton
    '''
    idnum = get_id(country)
    year = int(year)
    if year == 1990:
        emissions = emission_data.emission_1990[idnum] * 1000000
    elif year == 2005:
        emissions = emission_data.emission_2005[idnum] * 1000000
    elif year == 2017:
        emissions = emission_data.emission_2017[idnum] * 1000000
    else:
        raise ValueError
    return emissions


def get_country_change_for_years(country, year1, year2):
    '''
    Gets the changes in % of how much CO2 emissions has been impacted
    '''
    em_year1 = get_country_year_data_megaton(country, year1)
    em_year2 = get_country_year_data_megaton(country, year2)
    em_change = round(int(em_year2) / int(em_year1), 4)
    if em_change < 1:
        em_change = round(((1 - em_change) * 100), 4)
        str_res = (f"-{em_change}")
        float_str_res = float(str_res)
    else:
        em_change = round(((em_change - 1) * 100), 4)
        str_res = (f"{em_change}")
        float_str_res = float(str_res)
    return float_str_res

def get_population(country, year):
    '''
    Get population info from emission_data
    '''
    poplist = emission_data.country_data[country]["population"]
    try:
        pop_1990 = poplist[0]
    except IndexError:
        pop_1990 = None
    try:
        pop_2005 = poplist[1]
    except IndexError:
        pop_2005 = None
    try:
        pop_2017 = poplist[2]
    except IndexError:
        pop_2017 = None
    if year == 1990:
        pop = pop_1990
    elif year == 2005:
        pop = pop_2005
    else:
        pop = pop_2017
    return pop

def get_country_data(country_name):
    '''
    Gets country data from different functions and appends into a list
    '''
    em_1990 = get_country_year_data_megaton(country_name, "1990")
    em_2005 = get_country_year_data_megaton(country_name, "2005")
    em_2017 = get_country_year_data_megaton(country_name, "2017")
    pop_1990 = get_population(country_name, 1990)
    pop_2005 = get_population(country_name, 2005)
    pop_2017 = get_population(country_name, 2017)
    em_change_1990_2005 = get_country_change_for_years(country_name, "1990", "2005")
    em_change_2005_2017 = get_country_change_for_years(country_name, "2005", "2017")
    country_data = {
        'name': country_name,
        1990: {'emission': em_1990, 'population': pop_1990},
        2005: {'emission': em_2005, 'population': pop_2005},
        2017: {'emission': em_2017, 'population': pop_2017},
        'emission_change': (em_change_1990_2005, em_change_2005_2017)
    }
    return country_data

def print_country_data(data):
    '''
    Prints the result in get_country_data
    '''
    print(data["name"])
    pop_1990 = data[1990]["population"]
    print(f"Emission - 1990: {data[1990]['emission']} 2005: {data[2005]['emission']} 2017: {data[2017]['emission']}")
    print(f"Emission change - 1990-2005: {data['emission_change'][0]}% 2005-2017: {data['emission_change'][1]}%")
    if pop_1990 is not None:
        print(f"Population - 1990: {data[1990]['population']} 2005:"
            f" {data[2005]['population']} 2017: {data[2017]['population']}")
    else:
        print("Missing population data!")
