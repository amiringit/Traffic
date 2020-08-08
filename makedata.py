#the download function was taken from: https://techoverflow.net/2017/02/26/requests-download-file-if-it-doesnt-exist/
import requests
import os.path

def download_file(filename, url):
    """
    Download an URL to a file
    """
    with open(filename, 'wb') as fout:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        # Write response data to file
        for block in response.iter_content(4096):
            fout.write(block)
            
def download_if_not_exists(filename, url):
    """
    Download a URL to a file if the file
    does not exist already.    Returns
    -------
    True if the file was downloaded,
    False if it already existed
    """
    if not os.path.exists(filename):
        download_file(filename, url)
        return True
    return False

import pandas as pd
import wget
#download data

download_if_not_exists("flightlist_20200201_20200229.csv.gz", "https://opensky-network.org/datasets/covid-19/flightlist_20200101_20200131.csv.gz")
download_if_not_exists("flightlist_20200301_20200331.csv.gz", "https://opensky-network.org/datasets/covid-19/flightlist_20200301_20200331.csv.gz")
download_if_not_exists("flightlist_20200401_20200430.csv.gz", "https://opensky-network.org/datasets/covid-19/flightlist_20200401_20200430.csv.gz")
download_if_not_exists("flightlist_20200501_20200531.csv.gz", "https://opensky-network.org/datasets/covid-19/flightlist_20200501_20200531.csv.gz")

#used to be like following, but then it would download data for every run, even if their were already downloaded.
#import wget
#wget.download("https://opensky-network.org/datasets/covid-19/flightlist_20200201_20200229.csv.gz")
#wget.download("https://opensky-network.org/datasets/covid-19/flightlist_20200301_20200331.csv.gz")
#wget.download("https://opensky-network.org/datasets/covid-19/flightlist_20200401_20200430.csv.gz")
#wget.download("https://opensky-network.org/datasets/covid-19/flightlist_20200501_20200531.csv.gz")

#read data as csv

data_feb = pd.read_csv("flightlist_20200201_20200229.csv.gz", compression='gzip')
data_mar = pd.read_csv("flightlist_20200301_20200331.csv.gz", compression='gzip')
data_apr = pd.read_csv("flightlist_20200401_20200430.csv.gz", compression='gzip')
data_may = pd.read_csv("flightlist_20200501_20200531.csv.gz", compression='gzip')

#append data for 4 months and make new dataframe
flightslist = pd.concat([data_feb, data_mar, data_apr, data_may])
#reread "day" column as datetime
flightslist["day"] = pd.to_datetime(flightslist["day"], utc=True)
flightslist
