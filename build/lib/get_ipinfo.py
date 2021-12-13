import urllib.request
import json

def ip_details(iip):
        ipcheck=0
        try:
            url="https://ipinfo.io/" + iip
            req=urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                data=response.read()
                data=json.loads(data)
        except:
            ipcheck=1
            return ("Network-Problem/Not-Valid-Ip")
        if(ipcheck==0):
            try:
                my_dict = {"IP Address": data['ip'], "City:": data['city']
                , "State:": data['region']
                , "Country:": data['country']
                , "GPS:": data['loc']
                , "ZIP:": data['postal']
                , "ISP:": data['org']
                    }
                return (my_dict)
            except:
                my_dict2 = {"IP Address": "N/A", "City:": "N/A"
                , "State:": "N/A"
                , "Country:": "N/A"
                , "GPS:": "N/A"
                , "ZIP:": "N/A"
                , "ISP:": "N/A"
                    }
                return (my_dict2)
