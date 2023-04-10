import webbrowser
from sys import argv

if argv.__len__() < 2:
    print("You need to pass in search prompt")
    exit()

sites = ["stackoverflow.com", "w3schools.com", "geeksforgeeks.org"]

url = "https://google.com"
search_part = "/search?q="
site_filter = "site:" + str.join("+OR+", sites)
prompt = str.join("+", argv[1:])

webbrowser.open(url+search_part+prompt+"+"+site_filter)
