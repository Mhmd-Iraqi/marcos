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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
