from base.netutils import NetUtils


def login():
    url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19) '
    data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'qrcode_flag': 'false',
        'useticket': '1',
        'pagerefer': 'https://www.baidu.com/link?url=u0pafhNNnkXmoxj4A-y0SdV-8Ld738Nl'
                     'wXlRZw4i_Ha&wd=&eqid=9b0d7d940000f901000000045c8b5dce',
        'pcid': 'gz-50ec89487eb430734bc144aafe2021597ac2',
        'door': 'crpfk',
        'vsnf': '1',
        'su': 'MTUzNzg0MTI0MDA=',
        'service': 'miniblog',
        'servertime': '1552637479',
        'nonce': '6IGSH4',
        'pwencode': 'rsa2',
        'rsakv': '1330428213',
        'sp': '224aef4960526adb4167f5b9981bb530fad42c2f65edeab15987e794339dd495de378'
              'd460e547b4bbdc81849f246a2a867e8f3b229e35405ef044a275d13c4065cea953e9d1'
              '673c3def4fd94e9138f5369e908d4be0c261553e7fbbd134abd01c3726bc0abbbeb32fc5'
              'ca70ad9d451cf6f356283ebb6c1ce09ea8095dd417698',
        'sr': '1920*1080',
        'encoding': 'UTF-8'
    }

    print(NetUtils.post(url, data=data))


if __name__ == '__main__':
    login()
