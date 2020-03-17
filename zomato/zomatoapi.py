import requests


class Zomato:

    def __init__(self, apikey):
        self.apikey = apikey
        self.base_url = "https://developers.zomato.com/api/v2.1/"

    def search(self, city, lat, lon):
        try:
            float(lat)
            float(lon)
        except ValueError:
            raise ValueError('Invalid Lat or Long value!')

        headers = {'Accept': 'application/json', 'user-key': self.apikey}
        request = self.base_url + "search?q=" + str(city).lower().replace(' ', '%20') \
                                     + "&lat=" + str(lat) \
                                     + "&lon=" + str(lon)\
                                     + "&count=5000" \
                                     + "&radius=3000" \
                                     + "&sort=real_distance" \
                                     + "&order=asc"
        print(f"request URL: {request}")
        try:
            response = requests.get(request, headers=headers).json()
        except Exception:
            response = "null"
            pass
        return response