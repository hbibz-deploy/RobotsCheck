#!/usr/bin/python3

import requests, sys, datetime
from colorama import Fore as Cl
from colorama import Style

seperator = '*******************************************'

def menu(option):
    print(Cl.GREEN)
    print('__________      ___.           __          ')
    print('\______   \ ____\_ |__   _____/  |_        ')
    print(' |       _//  _ \| __ \ /  _ \   __\/  ___/')
    print(' |    |   (  <_> ) \_\ (  <_> )  |  \___ \ ')
    print(' |____|_  /\____/|___  /\____/|__| /____  >')
    print('        \/           \/       H4X0Rx*   \/ ')
    if len(sys.argv)<=2:
        print('-> Usage : ')
        print("-\t%s -u URL\n\t\tSpecify URL to scan" % sys.argv[0])
        print("+\t%s -h\n\t\tShow help" % sys.argv[0])
        quit()

    elif option == '-u' and len(sys.argv) > 2:
        print(Cl.BLUE)
        print("-> Scan started at %s" % str(datetime.datetime.now())[11:19])
    print(Style.RESET_ALL)

def sendRequest(url):
    urlToRequest = requests.get(url + "/robots.txt")
    if str(urlToRequest.status_code)[0] == '2':
        print("->\t%d  ON robots.txt file!" % urlToRequest.status_code)
        elementsInRobots = urlToRequest.text.split('\n')
        elementsInRobots = [x for x in elementsInRobots if "#" not in x and "User-agent" not in x and x != '']
        elementsInRobots = ["/"+_.split("/")[1] for _ in elementsInRobots]

    else:
        print("->\t%d  !" % urlToRequest.status_code)
        print("EXITING ...")

    return set(elementsInRobots)


def checkStatus(url, listOfElements):
    list200 = []
    for _ in listOfElements:
        fullUrl = url+_
        urlToRequest = requests.get(fullUrl)
        status = urlToRequest.status_code
        print("[/GET HTTP : {} ] -> {}".format(status, _))
        if check4(str(status),fullUrl,_):
            list200.append(_)
        if check2(str(status)):
            list200.append(_)
    print(seperator)
    print("[-] Done at %s\n[-] %d Results found!" % (str(datetime.datetime.now())[11:19],len(list200)))
    print(seperator)
def check2(string):
    if "2" in string:
        return True

def check4(status, fullUrl, elementOfList):
    if str(status)[0] == "4":
        print("\tTrying... -> {}".format(fullUrl + "/"))
        print(Cl.RED + "\t[/GET HTTP : {} ] -> {}".format(status,elementOfList+ "/"))
       	print(Style.RESET_ALL)
        if check2(str(status)):
            return True


def main():
    menu(sys.argv[1])
    checkStatus(sys.argv[2],sendRequest(sys.argv[2]))

if __name__ =='__main__':

    main()



#sendRequest('https://facebook.com')