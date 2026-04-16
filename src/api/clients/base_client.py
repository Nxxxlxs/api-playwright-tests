class BaseClient:
    def __init__(self, api_context):
        self.api = api_context

    def get(self, url):
        return self.api.get(url)

    def post(self, url, data=None):
        return self.api.post(url, data=data)