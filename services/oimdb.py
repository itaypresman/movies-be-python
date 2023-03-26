from lib.oimdb import Axios


class OimDb:
    @staticmethod
    def search(title):
        return Axios.get(params={'s': title})
