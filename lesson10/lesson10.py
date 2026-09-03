# http verb: post, put, get, delete

import requests
import json

header={'Content-Type': 'application/json'}

result=requests.post('https://apiestimatesearch.momoshop.com.tw/searchWordRec/searchRecommendKeywordList',json={"pageID":"1","userSearchKeyword":["戰鬥陀螺 x"]},headers=header)


response_json = json.loads(result.text)



recommendKeywords = response_json.get("recommendKeyword")

for keyword in recommendKeywords:
    print(keyword.get("name"))

