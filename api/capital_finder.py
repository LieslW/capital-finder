from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Necessary variables for parsing through string; also contains dicitonary
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)

        if 'name' in query_dict:
            # if the country exists, follow through code below

            url = 'https://restcountries.com/v3.1/name/'
            query = query_dict['name']
            query_url = url + query

            response = requests.get(query_url)
            data = response.json()

            parsed_city = data[0]['capital']
            city = str(parsed_city[0])
            result_str = f"The capital of {query.upper()} is {city.upper()}"

            # This is in both statements so whatever content returned is consistent
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(result_str.encode())
        else:
            # if the country doesn't exist/user error, return message below
            error_message = "Please search for a valid capital city to receive a valid country."

            # self.send_response(200)
            # self.send_header('Content-type', 'text/plain')
            # self.end_headers()

            self.wfile.write(error_message.encode())
        return

# non-country is getting pushed into query_dict and therefore, gets passed into the "it statement". So it ends in a 502 and doesn't get to the else statement.
