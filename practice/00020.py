####################################################
# 20. : Harvester IV Extraction
####################################################
import requests
from bs4 import BeautifulSoup
slug = "\n\n\n"

page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")


# Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
# Use a list comprehension to call the get_text method on each BeautifulSoup object
# CSS selectors
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods, slug)

short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs, slug)
print(temps, slug)
print(descs, slug)
