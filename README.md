# mpc-filereader
The Minor Planet Center (MPC) maintains a database of orbital parameters for over a million bodies updated daily in the MPCORB.DAT database file available here: (https://minorplanetcenter.net/data). 
However, due to the size of the dataset, it's necessary to provide this data in an unusual format (described here: https://minorplanetcenter.net//iau/info/MPOrbitFormat.html) - with certain parameters being defined in a compressed "packed form". This format is nonstandard and cannot be easily read with traditional '.csv' file readers.  

This script unpacks the epoch and reads an "MPCORB.DAT" file into pandas dataframes - convienet for future manipulation.


## To do:

Expand script to other MPC format files.
