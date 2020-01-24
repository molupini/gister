import requests
from os import environ
import fire
import json
import time

# Authentication only required for private gist, add param into 
# url = https://api.github.com/
# path = ...
# token = environ.get('AUTH_TOKEN')
# auth = {'Authorization': environ.AUTH_TOKEN}
# requests.get(url, headers=auth)

class Fetch(object):

    def hello(self, username='molupini'):
        try:
            # debugging
            print({'info': 'hello world func'})
        except Exception as er:
            return 1

    def public(self):
        try:
            # debugging
            # print({'info': 'public func'})
            response = requests.get('https://api.github.com/gists/public') 
            # If Bad Request 
            if response.status_code != 200:
                raise Exception({'error': f'response {response.status_code}'})
            js = response.json()
            return json.dumps(js, separators=(',',':'), indent=2)
        except Exception as er:
            print(er)
            return 1

    def user(self, username='molupini'):
        try:
            # debugging
            # print({'info': 'user func'})
            url = f'https://api.github.com/users/{username}/gists'

            response = requests.get(url) 
            # If Bad Request 
            if response.status_code != 200:
                raise Exception({'error': f'response {response.status_code}'})
            js = response.json()
            return js
        except Exception as er:
            print(er)
            return 1
    
    def selectId(self, obj):
        try:
            # debugging
            # print({'info': 'selectId func'})
            array = []
            for o in obj:
                array.append(o['id'])
            return array
        except Exception as er:
            print(er)
            return 1

    def read(self, username):
        try:
            # debugging
            # print({'info': 'read func'})
            with open(f'./{username}.json', 'r') as dat:
                return dat.read()
        except FileNotFoundError as er:
            # debugging
            # print(er)
            with open(f'./{username}.json', 'w+') as dat:
                # dat.write('')
                return dat.read()
    
    def write(self, username, obj):
        try:
            # debugging
            # print({'info': 'write func'})
            with open(f'./{username}.json', 'w+') as dat:
                dat.write(','.join(obj))
                dat.close()
        except Exception as er:
            print(er)



class Gist(object):

    def run(self, username='BretFisher', follow='true', rate='120'):

        while(True):
            # CALL FETCH CLASS
            fetch = Fetch()
            result = []

            # READ FILE, CREATE IF EXCEPTION
            read = fetch.read(username)
            # debugging
            # print('read =')
            # print(read)

            if read == '':
                read = []
            else:
                read = read.split(',')

            # GET GIST, BREAK LOOP IF NIL 
            user = fetch.user(username)
            if len(user) == 0:
                # debugging
                print({'warn': 'gist nil'})
                break
            
            # RETURN ONLY ID'S
            array = fetch.selectId(user)
            # IF READ NIL THEN POPULATE FILE 
            if len(read) == 0:
                for a in array:
                    print({'result': f'{username} gist.id found {a}'})
                fetch.write(username, array)
            else:
                # ELSE BETWEEN TWO SETS ELEMENTS FROM THE FIRST THAT ARE NOT PRESTENT IN THE 2ND
                dif = set(array).difference(set(read))
                # debugging 
                # print('dif =')
                # print(dif)
                result = list(dif)
            
            # IF RESULT GREATER THEN NIL POPULATE FILE 
            if len(result) > 0:
                for r in result:
                    print({'result': f'{username} gist.id found {r}'})
                fetch.write(username, array)

            # FOLLOW
            if follow != 'true':
                break
            # ENSURE RATE IS LIMITED
            time.sleep(120)


if __name__ == '__main__':
    # CALL GIST CLASS  
    fire.Fire(Gist)

