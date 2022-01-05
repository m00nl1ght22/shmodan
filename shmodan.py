import shodan
import sys
key = "key"

query = raw_input("zapros: ")
filename = raw_input("filename: ")
spisok = open(filename,"w")

try:
        api = shodan.Shodan(key)
        result = api.search(query)
        for service in result['matches']:
                print service['ip_str']
                spisok.write(service['ip_str'])
                spisok.write("\n")
except Exception as e:
        print 'err: %s' % e

