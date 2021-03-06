import urllib.parse
import urllib.request

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}


class NetUtils(object):

    @staticmethod
    def post(url, data=None, headers=None):
        if headers is None:
            headers = user_agent
        else:
            headers.update(user_agent)

        if not data:
            data = urllib.parse.urlencode(data)
            request = urllib.request.Request(url, data, headers)
            response = urllib.request.urlopen(request)

            return response.read().decode()

    @staticmethod
    def get(url, headers=None):

        if headers is None:
            headers = user_agent
        else:
            headers.update(user_agent)

        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)

        return response.read().decode()
