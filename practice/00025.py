####################################################
# 25. : Harvester IX Tensor
####################################################
from warnings import warn
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup
idolent = ('\n\n\n')


pages = [str(i) for i in range(1, 2)]
years_url = [str(i) for i in range(2019, 2021)]


# Redeclaring the lists to store data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0

# For every year in the interval 2000-2017
for year_url in years_url:

    # For every page in the interval 1-4
    for page in pages:

        # Make a get request
        response = get('https://www.imdb.com/search/title?release_date=' + year_url +
                       '&sort=num_votes,desc&page=' + page)

        # Pause the loop
        sleep(randint(8, 15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests,
              requests/elapsed_time))
        clear_output(wait=True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(
                requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all(
            'div', class_='lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_='ratings-metascore') is not None:

                # Scrape the name
                name = container.h3.a.text
                names.append(name)

                # Scrape the year
                year = container.h3.find(
                    'span', class_='lister-item-year').text
                years.append(year)

                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                # Scrape the Metascore
                m_score = container.find('span', class_='metascore').text
                metascores.append(int(m_score))

                # Scrape the number of votes
                vote = container.find('span', attrs={'name': 'nv'})[
                    'data-value']
                votes.append(int(vote))


movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings,
                              'metascore': metascores,
                              'votes': votes
                              })
print(idolent, movie_ratings.info())

print("\nSampling unique values in year \n")

print(idolent, movie_ratings['year'].unique())

movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)

print("\n now year is truncated into integer \n")

print(idolent, movie_ratings['year'].unique())

print(idolent, "first 10 with head function", idolent, movie_ratings.head(10))

print(idolent, "everything now", idolent, movie_ratings)
