from bs4 import BeautifulSoup
import requests
import sys

specified_name = sys.argv[1].title()

source = requests.get("https://stardewvalleywiki.com/{0}".format(specified_name)).text
soup = BeautifulSoup(source, 'lxml')


love_list = []
like_list = []
neutral_list = []
dislike_list = []
hate_list = []

def get_loves():
    row_num = 0
    for row in soup.find(string="Universal Loves").find_parent("table").find_all("tr"):
        # The first two rows are not necessary (table header and universals)
        if row_num > 1:
            # [1] will grab the name column
            for specific_love in row.select("a")[1]:
                love_list.append(specific_love.lower())
        row_num = row_num + 1

def get_likes():
    row_num = 0
    for row in soup.find(string="Universal Likes").find_parent("table").find_all("tr"):
        if row_num > 1:
            for specific_like in row.select("a")[1]:
                like_list.append(specific_like.lower())
        row_num = row_num + 1

def get_neutrals():
    row_num = 0
    for row in soup.find(string="Universal Neutrals").find_parent("table").find_all("tr"):
        if row_num > 1:
            for specific_neutral in row.select("a")[1]:
                neutral_list.append(specific_neutral.lower())
        row_num = row_num + 1

def get_dislikes():
    row_num = 0
    for row in soup.find(string="Universal Dislikes").find_parent("table").find_all("tr"):
        if row_num > 1:
            for specific_dislike in row.select("a")[1]:
                dislike_list.append(specific_dislike.lower())
        row_num = row_num + 1

def get_hates():
    row_num = 0
    for row in soup.find(string="Universal Hates").find_parent("table").find_all("tr"):
        if row_num > 1:
            for specific_hate in row.select("a")[1]:
                hate_list.append(specific_hate.lower())
        row_num = row_num + 1

get_loves()
get_likes()
get_dislikes()
get_hates()

def get_specified_item():
    # this is needed for two word items e.g Iridium Bar
    if len(sys.argv) == 4:
        return sys.argv[2].lower() + " " + sys.argv[3].lower()
    else:
        return sys.argv[2].lower()

specified_item = get_specified_item()

if specified_item in love_list:
    print("{0} loves {1}".format(specified_name, specified_item.title()))
elif specified_item in like_list:
    print("{0} likes {1}".format(specified_name, specified_item.title()))
elif specified_item in neutral_list:
    print("{0} is neutral about {1}".format(specified_name, specified_item.title()))
elif specified_item in dislike_list:
    print("{0} dislikes {1}".format(specified_name, specified_item.title()))
elif specified_item in hate_list:
    print("{0} hates {1}".format(specified_name, specified_item.title()))
else:
    print("No Results Found")
