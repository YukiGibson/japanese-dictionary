import api
import pprint
# getting file content

new_request = api.ApiRequests("hello").get_content()["data"]
new_key = ""
for item in new_request:
    pprint.pprint(item["slug"])

