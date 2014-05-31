import requests

r = requests.get("http://tcg.fishboned.net/ra/tcg.php?recycledart")
f = open("recycle.html", "w")
if r.status_code == 200:
	f.write(r.text)
