import wfuzz
import requests
from bs4 import BeautifulSoup

LoginUrl = r"http://192.168.56.101:8080/wp-login.php"
AdminUrl = r"http://192.168.56.101:8080/wp-admin/"

data = {'log': 'dnr6419', 'pwd': '123456','wp-submit':'Log In','redirect_to':'http://192.168.56.101:8080/wp-admin','testcookie':'1'}

# 쿠키 해결
res = requests.post(LoginUrl, data=data)
cookie = {}
with requests.Session() as s:
    res = s.post(LoginUrl,data=data)
    if "is incorrect" in res.text:
        print("[+] Username or Password Error")
        exit()
    else:
        cookie = s.cookies.get_dict()



# 플러그인 URI 해결
PluginUrl = r"http://192.168.56.101:8080/wp-admin/post-new.php?post_type=acf-field-group"
res = requests.get(PluginUrl,cookies=cookie)
# 파라미터 해결
# input을 이용하여 파라미터를 자동으로 출력하려 했으나 
# WordPress 특성상 _wpnonce 값을 알 수 없으므로 반자동으로 진행하려고 한다. 

# soup = BeautifulSoup(res.text,'html.parser')
# result = soup.find_all('input')
# arr = []
# for i in result:
#     if i.get('name'):
#         arr.append(i.get('name'))
# for param in list(set(arr)):
#     print(param)
# # http://192.168.1.32:8080/wp-admin/edit.php?post_type=acf-field-group


# for r in wfuzz.get_payload(range(100)).fuzz(hl=[97], url="http://192.168.1.59/?cat=FUZZ"):
#      print(r)
