from lib.oimdb import Axios


class OimDb:
    @staticmethod
    def search(title):
        result = Axios.get(params={'s': title})
        return result['Search'] if result['Response'] != 'False' else []


    @staticmethod
    def get_film(film_id):
        result = Axios.get(params={'i': film_id})
        return result if result['Response'] != 'False' else []