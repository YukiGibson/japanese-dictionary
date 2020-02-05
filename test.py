import api
import pprint
# getting file content

new_request = api.ApiRequests("悪い").get_content()["data"]
new_key = ""

for value in range(2):
    # Kanji
    pprint.pprint(new_request[value]["japanese"][0]["word"])
    # Furigana
    pprint.pprint(new_request[value]["japanese"][0]["reading"])

    pprint.pprint(new_request[value]["senses"][0]["english_definitions"])

