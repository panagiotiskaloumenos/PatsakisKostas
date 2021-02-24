def main():
    import requests, json
    url = "https://api.opap.gr/"
    gameid  = "1100"
    dstart = firstDayOfMonth()

    surl = url + "draws/v3.0/" + gameid + "/draw-date/" + dstart
    par = {"limit": "1"}

    resp = requests.get(surl, params=par)
    j = resp.text
    jdata = json.loads(j)
    rval = []

    for item in jdata['content']:
        t = int(item["drawId"]), list(item["winningNumbers"]["list"])
        rval.append(t)



def firstDayOfMonth():

	import datetime

	today = datetime.date.today()
	first = datetime.date(today.year, today.month, 1)
	return first

main()