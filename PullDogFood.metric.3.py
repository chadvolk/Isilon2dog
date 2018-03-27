import json
import requests
import warnings

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


u=f'gel\zChad.Uzvolk'
p='Passw0rd'

api_url_base = f'https://10.102.2.254:8080/platform/3/storagepool/nodepools'


#headers = {'Content-Type': 'application/json' , 'username': u ,'password':p }
headers = {'Content-Type': 'application/json'  }

def get_result_info():
    api_url = format(api_url_base)


    warnings.filterwarnings("ignore")
    response = requests.get(api_url, auth=(u, p), verify=False,  headers=headers)

    return json.loads(response.content.decode('utf-8'))


result_info = get_result_info()
print ('''ISILON API JSON RESPONSE:''')

print(result_info)
print (type(result_info))


# Parse each node in nodepools to get usage stats
free_bytes_list = []
#available_bytes_list = []
for node in result_info['nodepools'] :
    #print(type(i))
    print (node['usage'])
    #avaialable_bytes = float(i['usage']['avail_bytes'])
    free_bytes = float(node['usage']['free_bytes'])
    free_bytes_list.append(free_bytes)
    #available_bytes_list.append(avaialable_bytes)

print("Total Usable Bytes in PiB: {0:.2f}".format((sum(free_bytes_list)) /(1024**5))+" PiB")
print("Total Usable Bytes in TB: {0:.2f}".format((sum(free_bytes_list)) /(1024**4))+" TB")


