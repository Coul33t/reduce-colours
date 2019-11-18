from bs4 import BeautifulSoup as BS
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import json

# This file isn't meant to be run every time, I just did it once and that's it.
# The result is located in the "colours.json" file.

class RGB2DMC:
    def __init__(self, rgb_value, hex_value, dmc_name, floss_number):
        self.rgb_value = rgb_value
        self.hex_value = hex_value
        self.dmc_name = dmc_name
        self.floss_number = floss_number



firefox_options = Options()
firefox_options.add_argument('--headless')

driver = Firefox(options=firefox_options)

driver.get('https://threadcolors.com/')
html = driver.page_source
soup = BS(html, 'html.parser')

table_lines = soup.find_all('tr')

colours = []
colour_dict = {'Floss': None, 'DMC Name': None, 'RGB': None, 'Hex': None}
keys_order = []
rgb_keys = ['R', 'G', 'B']

for i, row in enumerate(table_lines):
    if i == 0:
        for column in row.find_all('th'):
            to_string = ''.join(column.contents).replace(u'\xa0', u'')
            keys_order.append(to_string)
            if to_string != '' and to_string not in rgb_keys:
                colour_dict[to_string] = []

    else:
        new_colour = colour_dict.copy()
        values = [x.get_text() for x in row.find_all('td')]
        rgb_values = [0, 0, 0]
        for j, val in enumerate(values):
            if j != 0:
                if keys_order[j] in rgb_keys:
                    if keys_order[j] == 'R':
                        rgb_values[0] = int(val)
                    elif keys_order[j] == 'G':
                        rgb_values[1] = int(val)
                    elif keys_order[j] == 'B':
                        rgb_values[2] = int(val)
                else:
                    new_colour[keys_order[j]] = val
        new_colour['RGB'] = rgb_values
        colours.append(new_colour)


with open('colours.json', 'w') as json_output:
    json.dump(colours, json_output)
