from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Necessary variables for parsing through string; also contains dicitonary
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        if 'name' in query_dict:
            # if the country exists, follow through code below

            url = 'https://restcountries.com/v3.1/capital/'
            query = dict['name']
            query_url = url + query

            response = requests.get(query_url)
            data = response.json()

            parsed_country = data[0]['name']
            country = str(parsed_country['common'])
            result_str = f"{query} is the capital of {country}"

            # This is in both statements so whatever content returned is consistent
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(result_str.encode())
        else:
            # if the country doesn't exist/user error, return message below
            error_message = "Please search for a valid country to receive a valid capital city."

        self.wfile.write(error_message.encode())
        return
