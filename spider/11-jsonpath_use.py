# jsonpath的使用

import json
import jsonpath

from base.netutils import NetUtils


def main():
    url = 'https://rate.tmall.com/list_detail_rate.htm' \
          '?itemId=567024626908&spuId=893336129&sellerId=1776456424&order=3&currentPage=2'

    headers = {
        'authority': 'rate.tmall.com',
        'method': 'GET',
        'path': '/list_detail_rate.htm?itemId=567024626908&spuId=893336129&sellerId=1776456424&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvxvvXvOyvUpCkvvvvvjiPRLqZljtEnLsZ0j3mPmPWAj1UP2ShgjtRPsLU6jE2RghCvCB4cNa9Ka147Dd9sRNGNl%2Bh75qNh46Cvvyv2UoENc6vgx0rvpvEvv2ckNzYvUyBdphvmpvhw9DRL9CrN46CvvyvvPpEclGv7pJjvpvhvvpvv8wCvvpvvUmmvphvC9vhvvCvpUyCvvOUvvVva6JivpvUvvmvr2KApXRtvpvIvvvvvhCvvvvvvUnvphvWu9vv96CvpC29vvm2phCvhhvvvUnvphvppvyCvhQhFkQvCsPWQb2XrqpyCW2%2BFO7t%2BeCB6RFEDLuTWDAvD7zvdigDNrCl%2BE7re369D7zvaB4AVA1lYExreut%2Bm7zvaNoAdcwudExrs8g72QhvCvvvMMGtvpvhvvvvvvwCvva47rMNzP6iRphvCvvvvvmrvpvEvvLCv1hBvhs3dphvmpvh8Ox0a9mpRu6CvvyvC8TEzYGvKPJrvpvEvvoekRzrvvecdphvmpvvz9e%2BdvvaxIhCvv147ICQYr147DdC7nGtvpvhvvvvv86Cvvyv2v%2FUd46vmrWtvpvhvvvvvv%3D%3D&needFold=0&_ksTS=1552555825097_4983&callback=jsonp4984',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'cna=ZRaJE91VC1wCAbSvsxStFi/p; lid=tb412400_11; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; enc=Oy9b7I8S8Vkfutb%2FGBt78gkpsjd99l67PjYGQNaeamMakfhLDiy1gMpMm5wrECR1sA4VlC3GUwiIgI2ts3WacA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; t=9a7352cff38b23b05d86668fa0366a4c; tracknick=tb412400_11; _tb_token_=e1e33803005be; cookie2=148587c0c33358521555fabc55b02dd3; l=bBxuG0CedQdwwPtLBOfNquI8LQ_t4QAf1sPzw4OgnICPsx1V9AWhWZ1NFwLyC3GVa6UyJ3yE-_q0B-L3ByzHl; isg=BJmZpacSIYL4-_qfm9l1TfnNqIWzjoxIVHvFPLtMTUGswrpUAneyqbmQxMYR-iUQ',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
    }

    content = NetUtils.get(url, headers)
    content = json.loads(content[content.index('{'):-1])
    comments = content['rateDetail']['rateList']
    print(comments)

    for comment in comments:
        print(jsonpath.jsonpath(comment, '$..userInfo'))


if __name__ == '__main__':
    main()
