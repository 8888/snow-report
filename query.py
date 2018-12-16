import re
import requests

class Query():
    def get_raw_content(self, url):
        try:
            r = requests.get(url)
            return r.text
        except:
            return 'Error! Response: {}'.format(r.status_code)
    
    def parse(self, content):
        result = re.findall(r'<p class="open value">(.*?)</p>', content)
        regex = re.compile(r"(<span>)|(</span>)")
        sanitized = list(map(lambda value: re.sub(regex, '', value), result))
        return sanitized
    
    def _run(self, url):
        content = self.get_raw_content(url)
        return self.parse(content)

    def run(self, urls):
        return list(map(lambda url: self._run(url), urls))

if __name__ == '__main__':
    URLS = [
        'https://www.onthesnow.com/vermont/killington-resort/skireport.html',
        'https://www.onthesnow.com/new-york/hunter-mountain/skireport.html',
        'https://www.onthesnow.com/pennsylvania/camelback-mountain-resort/skireport.html'
    ]
    QUERY = Query()
    print(QUERY.run(URLS))
