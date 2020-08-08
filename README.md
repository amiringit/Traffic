
# CMSC Traffic
## Amir Khoshbooie

In this project we have used the package called traffic to illustrate the impact of COVID-19 pandemic on aviation from Feb 2020 to May 2020.

---

Run `make` to build the report.

software: https://github.com/xoolive/traffic

Paper: oolive, Xavier. “Xoolive/Traffic.” GitHub, github.com/xoolive/traffic.


      reference: @article{olive2019traffic,
          author={Xavier {Olive}},
          journal={Journal of Open Source Software},
          title={traffic, a toolbox for processing and analysing air traffic data},
          year={2019},
          volume={4},
          pages={1518},
          doi={10.21105/joss.01518},
          issn={2475-9066},
      }

Data source:

https://opensky-network.org/datasets/covid-19/

## Dependencies

- matplotlib
- pandas
- numpy
- cartopy

## Installation

```
pip install --upgrade traffic
```

If you are using Google Colab you will need to first install cartopy using:

```
!apt-get -qq install python-cartopy python3-cartopy
```

