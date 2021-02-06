import random, string, requests, time, re, threading 
from colorama import init, Fore, Back, Style 
#webhook
def webhook(usr):
    import json 
    user = usr
    r = requests.session()
    url = "https://discord.com/api/webhooks/806841199989358603/ksK1AlT6_kdiOyMvTNUPVknFtYnqkmd7F2k60KCgtngUItf7ZQ49ZSvA0FHAZgJ6C2xh"#your web hook url
    data = {}
    data["username"] = "5G7 Bot !"
    data["embeds"] = []
    embed = {}
    embed["description"] = f"Username @{user}\n | Might be Available or Banned |" 
    embed["title"] = " 5G7  Catch !"
    data["embeds"].append(embed)
    result = r.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"}).text
#list
file = 'user.txt'
use = 'user.txt'
file = open(use, "r")
#check
def chk():
    while True:
                    r = requests.session()
                    proxy = open('proxy.txt', 'r').read().splitlines()
                    randomproxy = str(random.choice(proxy))
                    r.proxies = {'http': "http://"+randomproxy, 'https': 'https://'+randomproxy}
                    username = file.readline().split('\n')[0]
                    useragent = open('user-agent.txt', 'r').read().splitlines()#i use random user-agent to avoid get block its not work 100% But it fulfills the purpose 
                    randomagent = str(random.choice(useragent))#choose random
                    url = f'https://m.tiktok.com/node/share/user/@{username}'  
                    r = requests.get(url, headers={'user-agent': '{}'.format(randomagent)})
                    try:#Becuse i use regex ---------- i must use try cuse regex if not find the text it well stopped and close the app
                        responsecode = re.search(r'"statusCode":(.*?),', str(r.text)).group(1)#I like Regex ;)
                        if ('{"statusCode":10202,"statusMsg":"","userInfo":{}}') in r.text:
                            print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {username}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
                            f = open("availables.txt", "a", encoding='utf-8')
                            f.write(f"{username} | Might be Available or Banned |\n")
                            webhook(username)#Send User IN Discord
                        elif responsecode == "10222":
                           print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+ Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                        elif responsecode == "0":
                             print(Fore.CYAN+"[-] "+Fore.RED + "Maybe You Get blocked OR UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+ Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                        elif responsecode == "10221":
                            print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                        elif responsecode == "10223":
                            print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+Style.BRIGHT +" [-]"+ Style.RESET_ALL)
               
                    except:
                            #('statusCode: 0')<-(this to search for a word that You are the one who determines) in <- (this mean where you want to search) r.text <- (we want to search in response Who has come From Tik Tok)
                          if ('statusCode: 0') in r.text: #0 status its Indicates tHAT You Get Blocked Or User Isn't UnAvailable
                                      print(Fore.CYAN+"[-] "+Fore.RED + "if this repeat alot Maybe You Get blocked OR User UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {username}'+Fore.WHITE+" <=|"+Fore.CYAN+ Style.BRIGHT +" [-]"+ Style.RESET_ALL)
                          else:
                            print(r.text)
thrd = int(input("Thread 1 Best More than 150 Danger:"))
for _ in range(thrd):
    threading.Thread(target=chk).start()#If I want to explain to you what is threading Just Dm Cuse Its Long Stoy :( @8r18