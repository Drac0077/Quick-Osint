#!/usr/bin/env python3
# -*- coding: utf-8 -*-

art = '''

 ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗      ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝     ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║   ██║██║   ██║██║██║     █████╔╝█████╗██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║▄▄ ██║██║   ██║██║██║     ██╔═██╗╚════╝██║   ██║╚════██║██║██║╚██╗██║   ██║   
╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗     ╚██████╔╝███████║██║██║ ╚████║   ██║   
 ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝                                                                      
                                                                                                                                                                                                                                                                                                                                                       
                            DEVELOPED BY @DRAC0077. VERSION:1.0

This tool generates a quick osint web-search on an individuals based on their name and their mail.
'''
print(art)

import requests
from bs4 import BeautifulSoup
import random

# Function to perform Google search
def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('.kCrYT a')
    return [result.get('href') for result in results]

# Function to perform Google search with a specific site
def site_search(site):
    query = f"site:{site}"
    return google_search(query)

# Function to suggest Google dorks
def suggest_google_dorks(target_name):
    dorks = [
        f'intitle:"{target+name}"',
        f'site:"{target+name}"',
        f'intext:"{target+name}"'
    ]
    return dorks

# Asking user for input
target_name = input("Enter the Target's name: ")
email = input("Enter the Target's email address: ")

# Perform Google search with target's name
name_query = f'"{target_name}"'
name_results = google_search(name_query)

if name_results:
    print("Search Results based on Target's name:")
    for result in name_results:
        print(result)
else:
    print("No search results found for the Target's name.")

# Performing Google search
google_results = google_search(target_name)
print("General Search Results:")
for result in google_results:
    print(result)
print()

# Asking for a specific website using Google dorks
specific_website = input("Enter a specific website (e.g., 'twitter+com+[target's-name'): ")
specific_results = site_search(specific_website)

if specific_results:
    print("Specific Website Results:")
    for result in specific_results:
        print(result)
else:
    print("No specific website results found.")

# Asking for more search results
more_results = input("Do you want to fetch more search results? (y/n): ")
if more_results.lower() == "y":
    num_results = int(input("How many more results do you want to fetch? "))
    additional_results = google_search(target_name)
    additional_results = random.sample(additional_results, num_results)
    print(f"Additional Search Results ({num_results} results):")
    for result in additional_results:
        print(result)
    print()

# Suggesting Google dorks
dorks = suggest_google_dorks(target_name)
print("Suggested Google Dorks:")
for dork in dorks:
    print(dork)

print("Thank you for using Quick-Osint, Have a Fabulous day!")
