import requests
from lib.config import Config


class Axios:
    @staticmethod
    def get(path='/', params=None):
        if params is None:
            params = {}

        url = Config.OIMDB_URL + path
        data = {'apikey': Config.OIMDB_TOKEN, 'plot': 'full'}
        response = requests.get(url, params={**data, **params}).json()

        return response['Search'] if response['Response'] != 'False' else []
