import requests


class ApiRequests:
    def __init__(self, keyword=""):
        self.request = "https://jisho.org/api/v1/search/words?keyword={0}".format(keyword)
        self.keyword = keyword

    def new_request(self, keyword=""):
        self.request = "https://jisho.org/api/v1/search/words?keyword={0}".format(keyword)
        self.keyword = keyword

    def get(self):
        response = requests.get(self.request)
        return response.json()

    def has_content(self):
        content = self.get()
        result = content['data']
        if result:
            return True
        else:
            return False

    def get_content(self):
        if self.has_content():
            return self.get()
        return None
