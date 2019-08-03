import re
import time
import requests
from bs4 import BeautifulSoup


def ch():
    ch = ["Get all specified element with an specific attribut from the website","Get all links from the website by an attribut and the value","Get the website source code in an .html file","Get data from element code list","Filter data list1 from data list2"]
    i=1
    while i <= len(ch):
        value = ch[i-1]
        key = i
        i += 1
    response = input('\033[1;32m\nWhat would you like to do ?:\033[1;m ')
    return response

def init():
    """Initialisation Function who return link of the website"""
    link = input('\033[1;32m\n[+] Enter the link of website that you want to scrap:\033[1;m ')
    return str(link)

def get_all_link_from_html_code_by_cls(html, attr = '', value = ''):
    """ Function to return all links who has the same class """
    a = html.find_all("a", {attr: value}, {"href": re.compile("https://")})
    links = [] 
    for link in a:
        links.append(link.get("href"))
    return links


def get_htmlcode(link, params=None):
    """ Function who return the source code of the website """
    request = requests.get(link,params=params)
    page = request.content
    html = BeautifulSoup(page, "lxml")
    return html


def get_htmlcode_of_elements_by_attr(html, element='', attr='', value=''):
    """ Function to return data from some elements who has same attributs.
	It can also filter the data that you do not want to extract by pass it... """
    html_code = html.find_all(element, {attr: value})
    return html_code


def find_element_by_attrs(html, attributs, element=''):
    """ Function who take an element and a dict of some attributs and their values
	to return all element who has them """
    for key in attributs.keys():
        value = attributs[key]
        key = key
        found = html.find_all(element, {key: value})
        return found


def get_data_from_element_list(elements):
    """ Function who take a list of elements, get the data and return them"""
    data = []
    for l in elements:
        dat = l.getText().strip()
        data.append(dat)
    return data


def filter_data_on_list1_elmt_from_list2_elmt(list1, list2):
    filt = []
    for n in list1:
        for i in list2:
            if n in i:
                filtered = i.split(n)
                filtered = str(filtered[0])
                filt.append(filtered)
    return filt
