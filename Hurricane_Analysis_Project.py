# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#Conversion dict
conversion_dict= {"M": 1000000,
             "B": 1000000000}

#Update damages function; converts string data in list to float values. Unrecorded values are retained.
def damages_to_float(damages_list):
    new_damages_list = []
    for i in range(len(damages_list)):
        damage_data = damages_list[i]
        if "M" in damage_data:
            new_damages_list.append(float(damage_data[:-1]) * conversion_dict["M"])
            
        elif "B" in damage_data:
            new_damages_list.append(float(damage_data[:-1]) * conversion_dict["B"])
            
        else:
            new_damages_list.append(damage_data)
    return new_damages_list

new_damages = damages_to_float(damages)
#print(new_damages)


#Function that compounds respective hurricane data into dictonary with key for each hurricane. 
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"Name": names[i],
                           "Month": months[i],
                           "Year": years[i],
                           "Max Sustained Wind": max_sustained_winds[i],
                           "Areas Affected": areas_affected[i],
                           "Damage": new_damages[i],
                           "Deaths": deaths[i]}
    return hurricanes


hurricanes = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricanes)


#Function that creates dictionary of year keys containing lists of data for hurricanes that occurred that year.
def hurricane_by_year(old_dict):
    new_year_dict = {}
    for key in old_dict:
        current_year = old_dict[key]['Year']
        current_element = old_dict[key]
        if current_year not in new_year_dict:
            new_year_dict[current_year] = []
            new_year_dict[current_year].append(current_element)
        else:
            new_year_dict[current_year].append(current_element)
    return new_year_dict

'''
hurricanes_by_year = hurricane_by_year(hurricanes)
print(hurricanes_by_year)
'''

#Function that counts how often an area is affected by hurricanes, returning each area and count as key, value pairs in a dictionary.
def area_hit_count(hurricane_dict):
    area_hit_dict = {}
    for key in hurricane_dict:
        area_list = hurricane_dict[key]['Areas Affected']
        for area in area_list:
            if area not in area_hit_dict:
                area_hit_dict[area] = 1
            else:
                area_hit_dict[area] += 1
    return area_hit_dict

'''
area_hit_freq = area_hit_count(hurricanes)
print(area_hit_freq)
'''
#Function that identifies the area most hit by hurricanes, and how many times.
def most_hit_area(dict):
    current_count = 0
    for key in dict:
        if dict[key] > current_count:
            current_count = dict[key]
            current_key = key
    return current_key, current_count

'''
most_hit, hit_count = most_hit_area(area_hit_freq)
print(f"The area most affected by hurricanes is {most_hit}, hit {hit_count} times.")
'''

#Function that identifies the hurricane with highest death count.
def highest_death_freq(dict):
    death_count = 0
    for key in dict:
        current_death = dict[key]['Deaths']
        if current_death > death_count:
            death_count = current_death
            current_hurricane = key
    return current_hurricane, death_count

'''
most_deaths, death_count = highest_death_freq(hurricanes)
print(f"The hurricane that caused the most deaths was hurricane {most_deaths} with {death_count} deaths.")
'''

#Function that rates hurricanes on a mortality scale.
def mortality_rating(hurricanes_dict):
    mortality_scale = {0: 0,
                      1: 100,
                      2: 500,
                      3: 1000,
                      4: 10000}
    hurricane_mortality = {0:[], 1:[],2:[], 3:[], 4:[], 5:[]}
    for key in hurricanes_dict:
        current_death = hurricanes_dict[key]['Deaths']
        if current_death <= 0:
            hurricane_mortality[0].append(key)
        elif mortality_scale[0] < current_death <= mortality_scale[1]:
            hurricane_mortality[1].append(key)
        elif mortality_scale[1] < current_death <= mortality_scale[2]:
            hurricane_mortality[2].append(key)
        elif mortality_scale[2] < current_death <= mortality_scale[3]:
            hurricane_mortality[3].append(key)
        elif mortality_scale[3] < current_death <= mortality_scale[4]:
            hurricane_mortality[4].append(key)
        else:
            hurricane_mortality[5].append(key)
    return hurricane_mortality

'''
mortality = mortality_rating(hurricanes)
print(mortality)
'''

#Function that finds the hurricane that caused the most damage, and how costly it was.
def most_damaging(hurricanes):
    highest_damage = 0
    for key in hurricanes:
        current_damage_value = hurricanes[key]['Damage']
        if current_damage_value == 'Damages not recorded':
            pass
        elif current_damage_value > highest_damage:
            highest_damage = current_damage_value
            most_damaging_hurricane = key
    return highest_damage, most_damaging_hurricane

'''
highest_damage_cost, hurricane_most_damaging = most_damaging(hurricanes)
print(f"The most damaging hurricane was {hurricane_most_damaging} with a damage cost of ${highest_damage_cost}.")
'''


#Function that rates hurricanes according to how much damage they cause.
def hurricane_damage_rating(hurricanes_dict):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    hurricane_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for key in hurricanes:
        current_cane = key
        current_damage_value = hurricanes[key]['Damage']
        if current_damage_value == 'Damages not recorded':
            hurricane_ratings[0].append(hurricanes[current_cane])
        elif current_damage_value <= damage_scale[1]:
            hurricane_ratings[1].append(hurricanes[current_cane])
        elif damage_scale[1] < current_damage_value <= damage_scale[2]:
            hurricane_ratings[2].append(hurricanes[current_cane])
        elif damage_scale[2] < current_damage_value <= damage_scale[3]:
            hurricane_ratings[3].append(hurricanes[current_cane])
        elif damage_scale[3] < current_damage_value <= damage_scale[4]:
            hurricane_ratings[4].append(hurricanes[current_cane])
        else:
            hurricane_ratings[5].append(hurricanes[current_cane])        
    return hurricane_ratings

'''
hurricane_damage_ratings = hurricane_damage_rating(hurricanes)
print(hurricane_damage_ratings[5])
'''
