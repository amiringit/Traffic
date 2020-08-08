#make new dataframe containing the number of departed aircraft per day 
from traffic.data import airports
import pandas as pd
from makedata import *

airports_subset = [
    # Europe
    ["EDDF", "UUEE"],
    # Asia
    ["RJBB", "YSSY"],
    # America
    ["KATL", "CYYZ"],
]

data = pd.concat(
    (
        flightslist.query(f'origin == "{airport}"')
        # count the number of departing aircraft per day
        .groupby("day")
        .agg(dict(callsign="count"))
        # label the current chunk with the name of the airport
        .rename(columns=dict(callsign=airport))
        # iterate on all airports in the list hereabove
        for airport in sum(airports_subset, [])
    ),
    axis=1,
)
data

