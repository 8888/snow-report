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

    def _run(self, mountain):
        content = self.get_raw_content(mountain['url'])
        report = {
            'name': mountain['name'],
            'report': self.parse(content)
        }
        return report

    def run(self, mountains):
        return list(map(lambda mountain: self._run(mountain), mountains))
