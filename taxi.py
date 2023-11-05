import requests
import json

def get_token():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36',
        'Cookie': 'ys=newsca.native_cache#ybzcc.ru#svt.1#def_bro.1#ead.2FECB7CF; is_gdpr=0; yashr=9851379761698002267; _ym_uid=16360272791022374256; is_gdpr_b=CNC3LBDG1QEoAg==; gdpr=0; L=RFtyQ09cWldmdgIGekRvQ3tFXUFpB1tlBjwLCyAqQU0=.1698177924.15505.367571.8f232d87e541481dcf88d18ef8470e56; yandex_login=gogame37; yandexuid=1813243551691081760; yuidss=1813243551691081760; i=1orreKjoN5jdBXgo34JKwwUEHQs0ADX5xBZGEinD9PD1rHUrFy5xLKKmAzBQZcyuuTklfgBmMu4CIjRMMECBJBITYik=; ymex=1700773173.oyu.5825466761698002267#2013362268.yrts.1698002268; my=YwA=; font_loaded=YSv1; Session_id=3:1699037304.5.0.1698177924343:yUx4Tw:29.1.2:1|594829349.0.2.3:1698177924|3:10278153.354872.Al6Q132s6Qc2lBVdskP3F4niS0E; sessar=1.1183.CiC19sINi8851KImTgbp66F6mWegjKIehgXMOA7NvwK9dA.7tukoHxiqWCn94WE2gcjcAehlGbKlQ3v1eAvJsGT6Dg; sessionid2=3:1699037304.5.0.1698177924343:yUx4Tw:29.1.2:1|594829349.0.2.3:1698177924|3:10278153.354872.fakesign0000000000000000000; _ym_isad=2; cycada=C33WXaO7Fpgg1/3T84XddXATqGGN34mVtl76xweF8RA=; bh=EjoiQ2hyb21pdW0iO3Y9IjExNiIsIk5vdClBO0JyYW5kIjt2PSIyNCIsIllhQnJvd3NlciI7dj0iMjMiGgUieDg2IiIMIjIzLjkuMy45MzEiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJUIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjIyOCIsIk5vdClBO0JyYW5kIjt2PSIyNC4wLjAuMCIsIllhQnJvd3NlciI7dj0iMjMuOS4zLjkzMSIi; sae=0:E43C1CC4-440B-4AED-BDB1-BB2F5EB87756:p:23.9.3.931:w:d:RU:20211104; _yasc=r6IFVT3xUIKtpY1q4MvsQglAarVftuMsB2TcR2ZzJSKXsv43BBuUdYAdWIRSTAeMxJnsoHaOakX0WXMyQbgr2fg6cHk=; _ym_d=1699212391; yp=1699296761.uc.ru#1699296761.duc.de#1729717173.cld.2261448#1729717173.brd.0699000014#1700680668.hdrc.1#1714113294.szm.1:1920x1080:1920x956#2014569363.pcs.1#1700523734.ygu.1#4294967295.skin.s#2013537924.udn.cDrQlNCw0L3RjyDQotC40YLQvtCy#1705960863.v_sum_b_onb.1:1698184863096#1701023705.csc.1#1706281408.v_smr_onb.t%3D2:1698505407812#1699219961.gpauto.55_949795:37_098354:100000:3:1699212761'
    }
    response = requests.post("https://ya-authproxy.taxi.yandex.ru/csrf_token", headers=headers).json()
    return response['sk']
def get_route_info(route):
    url = "https://ya-authproxy.taxi.yandex.ru/3.0/routestats"
    payload = {"route":[route],
        "format_currency":True,
        "supports_paid_options": True
    }
    headers = {
    'X-Csrf-Token': get_token(),
    'X-YaTaxi-UserId': '1ad5afd2d09745559c2bd24b4ae4ff47',
    'X-Taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36 turboapp_taxi',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36',
    'Cookie': 'ys=newsca.native_cache#ybzcc.ru#svt.1#def_bro.1#ead.2FECB7CF; is_gdpr=0; yashr=9851379761698002267; _ym_uid=16360272791022374256; is_gdpr_b=CNC3LBDG1QEoAg==; gdpr=0; L=RFtyQ09cWldmdgIGekRvQ3tFXUFpB1tlBjwLCyAqQU0=.1698177924.15505.367571.8f232d87e541481dcf88d18ef8470e56; yandex_login=gogame37; yandexuid=1813243551691081760; yuidss=1813243551691081760; i=1orreKjoN5jdBXgo34JKwwUEHQs0ADX5xBZGEinD9PD1rHUrFy5xLKKmAzBQZcyuuTklfgBmMu4CIjRMMECBJBITYik=; ymex=1700773173.oyu.5825466761698002267#2013362268.yrts.1698002268; my=YwA=; font_loaded=YSv1; Session_id=3:1699037304.5.0.1698177924343:yUx4Tw:29.1.2:1|594829349.0.2.3:1698177924|3:10278153.354872.Al6Q132s6Qc2lBVdskP3F4niS0E; sessar=1.1183.CiC19sINi8851KImTgbp66F6mWegjKIehgXMOA7NvwK9dA.7tukoHxiqWCn94WE2gcjcAehlGbKlQ3v1eAvJsGT6Dg; sessionid2=3:1699037304.5.0.1698177924343:yUx4Tw:29.1.2:1|594829349.0.2.3:1698177924|3:10278153.354872.fakesign0000000000000000000; _ym_isad=2; cycada=C33WXaO7Fpgg1/3T84XddXATqGGN34mVtl76xweF8RA=; bh=EjoiQ2hyb21pdW0iO3Y9IjExNiIsIk5vdClBO0JyYW5kIjt2PSIyNCIsIllhQnJvd3NlciI7dj0iMjMiGgUieDg2IiIMIjIzLjkuMy45MzEiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJUIkNocm9taXVtIjt2PSIxMTYuMC41ODQ1LjIyOCIsIk5vdClBO0JyYW5kIjt2PSIyNC4wLjAuMCIsIllhQnJvd3NlciI7dj0iMjMuOS4zLjkzMSIi; sae=0:E43C1CC4-440B-4AED-BDB1-BB2F5EB87756:p:23.9.3.931:w:d:RU:20211104; _yasc=r6IFVT3xUIKtpY1q4MvsQglAarVftuMsB2TcR2ZzJSKXsv43BBuUdYAdWIRSTAeMxJnsoHaOakX0WXMyQbgr2fg6cHk=; _ym_d=1699212391; yp=1699296761.uc.ru#1699296761.duc.de#1729717173.cld.2261448#1729717173.brd.0699000014#1700680668.hdrc.1#1714113294.szm.1:1920x1080:1920x956#2014569363.pcs.1#1700523734.ygu.1#4294967295.skin.s#2013537924.udn.cDrQlNCw0L3RjyDQotC40YLQvtCy#1705960863.v_sum_b_onb.1:1698184863096#1701023705.csc.1#1706281408.v_smr_onb.t%3D2:1698505407812#1699219961.gpauto.55_949795:37_098354:100000:3:1699212761'
    }
    response = requests.post(url, headers=headers, json=payload).json()
    econom = response["service_levels"][0]
    price, demand, estimated_time = int(econom['max_price_as_decimal'][:-3]), econom['paid_options']['alert_properties']['label'], econom['estimated_waiting']['message']
    print(route,price,demand,estimated_time)
    return price, demand, estimated_time
# print(get_route_info([37.094755,55.946703]))
# print(response["service_levels"][0]['paid_options']["alert_properties"]['label'])