import os
import csv
import sys
from bs4 import BeautifulSoup

filepath = (os.getcwd() + "/fb_birthdays.html")
if not os.path.isfile(filepath):
    sys.exit("\nPlease rename your HTML file: `fb_birthdays.html` and ensure the terminal session is in the same folder as the HTML file\n")

parsed = BeautifulSoup(open(filepath), "html.parser")

output_lod = []
for birthday_row in parsed.find_all("li", {"class": "_43q7"}):   # Querying into li for each individual

    birthday_data = birthday_row.find("a", {"class": "link"})
    birthday_info = birthday_data.get("data-tooltip-content")    # Get string with our wanted substrings in it

    output_dict = {
        "Name": birthday_info.split(" (",1)[0],                   # Get Name substring from Info string
        "Date": birthday_info.split(" (",1)[1].replace(")", ""),  # Get Date substring from Info string
        "Link": birthday_data.get("href")                         # Get FB Profile Link
    }

    output_lod.append(output_dict)

with open("Processed Birthdays.csv", "w") as output_file:
    dict_writer = csv.DictWriter(output_file, output_lod[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(output_lod)

print("Data successfully processed. Output file is called: Processed Birthdays.csv")
