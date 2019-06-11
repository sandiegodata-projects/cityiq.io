# City IQ pedestrian Data for San Diego

This dataset is pedestrian directions and counts for walkwaks in the San Diego
CityIQ system. The package includes pedestrian counts for most walkway
locations in the San Diego CityIQ system, but not all of them. The date range
for the data is 1 August 2018 to the last full month before the package was
built. For Version 1, then end date is 1 June 2019.


## Building the Source Package 

Before generating this package, you must have scraped all of the events to be
included in the package. After creating a ``.city-iq.yaml`` configuration file,
run:

    $ ciq_events -s ped # Scrape the events
    $ ciq_aggregate ped # Convert JSON to CSV
    
The first process ``ciq_events`` may run for several days and consume up to
300G of disk space. The second process, ``ciq_aggregate`` may run for a few
hours and consume a few more gigabytes of disk space.
