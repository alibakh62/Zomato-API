# Zomato-API
For getting restaurants data from Zomato's API. 

To query the API, you'll need these four:

- city name
- state (2-letter)
- latitude
- longitude

## Query a long list of locations
To query the API for many locations, store them in a .csv file. Make sure your file has the following columns (keep the names the same): `city`, `state`, `latitude`, `longitude`. 

Once, you have the input file, run the `run.py` in the command line. You need pass in the following arguments:

- `--key`: your Zomato API key
- `--input`: path to your .csv input file
- `--output`: path where to store the results
- `--states` (optional): in case you want to query for only a list of selected states

Your command should look like this:

```bash
python run.py --key <API_KEY> --input <INPUT_FILE_PATH> --output <OUTPUT_FOLDER_PATH> --states TX CA FL
```

## Single query
In case, you only want to query once, you can use the `zomatoapi.py` module itself. Just read the module in your code, and give it the `city`, `latitude`, and `longitude`. Check out the pseudo code below:

```python
from zomatoapi import Zomato

apikey = "YOUR API KEY"

z = Zomato(apikey)

city = 'Dallas`
lat = 32.76793
lon = -96.83631

response = z.search(city, lat, lon)
```
