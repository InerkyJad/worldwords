import time
import os, json, requests, sys


def read(f):
    with open(f, 'r', encoding="utf-8") as f:
        return json.load(f)


def get_files(path):
    arr = os.listdir(path)
    return [path + p for p in arr]


'''******************************************************************************************************************'''

_all = {}
for f in get_files('./native/'):
    lang = f.split('/')[-1][0:2]
    _all[lang] = json.load(open(f, 'r', encoding="utf-8"))

full_len = len(_all['en'])
for i in range(len(_all['en'])):
    json_data = {
        "_af": _all["af"][i],
        "_ar": _all["ar"][i],
        "_be": _all["be"][i],
        "_bg": _all["bg"][i],
        "_bn": _all["bn"][i],
        "_cn": _all["cn"][i],
        "_da": _all["da"][i],
        "_de": _all["de"][i],
        "_el": _all["el"][i],
        "_en": _all["en"][i],
        "_es": _all["es"][i],
        "_fi": _all["fi"][i],
        "_fr": _all["fr"][i],
        "_ga": _all["ga"][i],
        "_hi": _all["hi"][i],
        "_hr": _all["hr"][i],
        "_id": _all["id"][i],
        "_is": _all["is"][i],
        "_it": _all["it"][i],
        "_iw": _all["iw"][i],
        "_ja": _all["ja"][i],
        "_ka": _all["ka"][i],
        "_ko": _all["ko"][i],
        "_lb": _all["lb"][i],
        "_lv": _all["lv"][i],
        "_mt": _all["mt"][i],
        "_nl": _all["nl"][i],
        "_no": _all["no"][i],
        "_pl": _all["pl"][i],
        "_pt": _all["pt"][i],
        "_ro": _all["ro"][i],
        "_ru": _all["ru"][i],
        "_sk": _all["sk"][i],
        "_sl": _all["sl"][i],
        "_sr": _all["sr"][i],
        "_sv": _all["sv"][i],
        "_th": _all["th"][i],
        "_tl": _all["tl"][i],
        "_uk": _all["uk"][i],
        "_ur": _all["ur"][i],
        "_uz": _all["uz"][i],
        "_vi": _all["vi"][i]
    }

    requests.post('http://127.0.0.1:8000/', data=json.dumps(json_data, ensure_ascii=False).encode("utf-8"), headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    })

    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %d%%" % ('=' * int((i / full_len) * 50), int((i / full_len) * 100)))
    sys.stdout.write(' %d/%d' % (i, full_len))
    sys.stdout.flush()

    time.sleep(0.002)