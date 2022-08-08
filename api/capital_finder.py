from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)

        if "name" in query_dict:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            response = requests.get(url + query_dict["word"])
            data = response.json()
            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)

            message = str(definitions)
        else:
            message = "gimme a word"

        self.wfile.write(message.encode())
        return
