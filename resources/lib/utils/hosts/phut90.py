import re, json
from utils.mozie_request import Request
import utils.xbmc_helper as helper
from urllib import urlencode


def get_link(url, media):
    response = Request().get(url)
    sources = re.search(r'sources:\s?(.*?),\n', response)
    sources = helper.convert_js_2_json(sources.group(1).encode('utf-8'))
    if sources:
        try:
            sources = sorted(sources, key=lambda elem: int(elem['label'][0:-1]), reverse=True)
        except:
            pass

        url = ""
        if len(sources) > 0:
            for source in sources:
                url = source.get('file')
                break

        if re.search('pegasus-pop.com', url):
            header = {
                'Origin': 'https://live.90m.tv',
                'User-Agent': "Chrome/59.0.3071.115 Safari/537.36",
                'Referrer': 'https://live.90m.tv'
            }
            return url + "|%s" % urlencode(header)

    return url