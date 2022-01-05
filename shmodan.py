import shodan
import sys
key = "key"

print '\033[31m'
print '   __ '
print '  (_ |_  _  _  _| _  _ '
print '  __)| )|||(_)(_|(_|| )'
print '\033[39m'

query = raw_input("request: ")
filename = raw_input("filename: ")
iplist = open(filename, "w")

try:
        api = shodan.Shodan(key)
        result = api.search(query)
        for service in result['matches']:
                print service['ip_str']
                iplist.write(service['ip_str'])
                iplist.write("\n")
except Exception as e:
        print 'err: %s' % e
