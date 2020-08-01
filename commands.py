import requests
import json
import configparser as cfg
from time import sleep
class command():


    def __init__(self, config):
        self.apikey = self.read_token_from_config_file(config)
        self.base = "https://pikuapi.herokuapp.com/cnv/{}?".format(self.apikey)


    def getReply(self, msg):
        self.messege=msg
        url=self.base + "getReply="+self.messege
        try:
            r = requests.get(url)
            s=json.loads(r.content)
            return s
        except:
            print('Refiused')
            sleep(5)
            print('ok now')
    

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'apikey')