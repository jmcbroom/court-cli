import requests, urllib, bs4, re, fire, time

ROOT = 'http://jis.36thdistrictcourt.org/ROAWEBINQ/ROACase.aspx?'

# URL parameters for different types of cases:
# ... landlord-tenant
LT = {
    'CRTNO': '3600',
    'PFIX': 'C',
    'PTY':'A01'
}
# ...civil & criminal
CC = {
    'CRTNO': '3600',
    'PFIX': 'D',
    'PTY':'D01'
}

class Case(object):
    def __init__(self, cnum = '135046942', ctype = 'CC'):
        """
        Create a new Case instance; get a register of actions from
        36th District court
        """

        self.case_num = cnum
        self.case_type = ctype
        if ctype == 'LT':
            params = LT
            params['CASE'] = self.case_num
        elif ctype == 'CC':
            params = CC
            params['CASE'] = self.case_num
        params['CASE'] = self.case_num
        self.case_url = ROOT + urllib.parse.urlencode(params)
        r = requests.get(self.case_url)
        parsed = bs4.BeautifulSoup(r.text, 'lxml')
        self.roa_text = []
        for tag in parsed.find_all(id=re.compile('dlROA_ct.')):
            self.roa_text.append(tag.string.replace("\xa0", " "))

    def display(self):
        """Print register of actions to the console"""
        for i, a in enumerate(self.roa_text):
            print("{} < ({})".format(a, i))

    def download(self):
        """Download register of actions as a .txt file"""
        with open('{}_{}.txt'.format(self.case_num, int(time.time())), 'w') as thefile:
            for line in self.roa_text:
                thefile.write("{}\n".format(line))

    def clean(self):
        """Remove some unnecessary text from the register of actions."""
        # remove the top bar
        del self.roa_text[0]
        # just get the case information from the first line
        self.roa_text[0] = self.roa_text[0][53:-2]

        # remove the court information
        del self.roa_text[1:8]

        for i, a in enumerate(self.roa_text):
            if a.find('ACTIONS, JUDGMENTS, CASE NOTES') > -1:
                del self.roa_text[i-1:i+1]

    def parse_as_blocks(self):
        """Parse entire ROA text into blocks which can be identified"""
        pass

if __name__ == '__main__':
    fire.Fire(Case)
