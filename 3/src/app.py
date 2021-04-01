from datetime import datetime
import json


class App:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __get_response_data(self):
        current_url = self.environ['HTTP_HOST'] + self.environ['RAW_URI']
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return {
            'time': current_time,
            'url': current_url
        }

    def __iter__(self):
        response = json.dumps(self.__get_response_data()).encode('utf-8')

        headers = [
            ('Content-Type', 'application/json'),
            ('Content-Length', str(len(response)))
        ]
        self.start_response('200 OK', headers)

        yield response
