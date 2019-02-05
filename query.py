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
        return [re.sub(regex, '', value) for value in result]

    def remove_miles(self, content):
        '''
        filter out miles values
        they exist for some mountains, but not all
        and when they exist, they are usually incorrectly reporting 0 miles open
        '''
        return [stat for stat in content if stat.find('mi') == -1]

    def map(self, runs, lifts, acres):
        return {'runs': runs, 'lifts': lifts, 'acres': acres}

    def _run(self, mountain):
        content = self.get_raw_content(mountain['url'])
        parsed_content = self.parse(content)
        cleaned_content = self.remove_miles(parsed_content)
        mapped_content = self.map(*cleaned_content)
        report = {
            'name': mountain['name'],
            'report': mapped_content
        }
        return report

    def run(self, mountains):
        return [self._run(mountain) for mountain in mountains]
