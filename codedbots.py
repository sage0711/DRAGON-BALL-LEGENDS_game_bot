# -*- coding: utf-8 -*-
import requests
import base64
import json
import time

class codedbots(object):
    def __init__(self):
        self.s = requests.Session()
        self.mainurl = base64.b64decode('aHR0cHM6Ly9sZWdlbmRzLmNvZGVkYm90cy5jb20=').decode()
    
    def getuuid(self, data):
        r = self.s.post(self.mainurl + '/getuuid', data={'uuid': data})
        return r.content

    def getecd(self, data, _platformId, _romType):
        r = self.s.post(self.mainurl + '/ecd', data={'ecd': base64.b64encode(data), '_platformId': _platformId, '_romType': _romType})
        if r.status_code == 200:
            return json.loads(r.content)
        else: 
            print('[%s] request failed [%s]' % (r.status_code, r.content.decode()))
            time.sleep(60)
            exit(1)

    def encrypt(self, data):
        r = self.s.post(self.mainurl + '/encrypt', data={'data': json.dumps(data, separators=(',', ':'))})
        if r.status_code == 200:
            return base64.b64decode(r.content)
        else:
            print('[%s] request failed [%s]' % (r.status_code, r.content.decode()))
            time.sleep(60)
            exit(1)

    def decrypt(self, data):
        r = self.s.post(self.mainurl + '/decrypt', data={'data': base64.b64encode(data).decode()})
        if r.status_code == 200:
            return json.loads(r.content)
        else:
            print('[%s] request failed [%s]' % (r.status_code, r.content.decode()))
            time.sleep(60)
            exit(1)
