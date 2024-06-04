from config import QUERY_TEXT

class PostmanRequestModel:
    def __init__(self, query_text=QUERY_TEXT):
        self.service = "search"
        self.method = "POST"
        self.path = "/search-all"
        self.body = {
            "queryText": query_text,
            "from": 0,
            "size": 10,
            "mergeEntities": True,
            "nested": True,
            "clientTraceId": "941c73ae-107f-4965-87ae-95c00e8d9d42",
            "requestOrigin": "dropdown",
            "domain": "public",
            "queryIndices": ["collaboration.workspace", "adp.api", "runtime.collection", "flow.flow"]
        }
