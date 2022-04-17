#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 支持Python3
import json
import sys
import requests
notify_channel_funcs = {
    "wecom": "wecom"
}
proxies = {"http": "http://10.9.24.190:30581",
           "https": "http://10.9.24.190:30581", }
class Sender(object):
    @classmethod
    def send_wecom(cls, payload):
        users = payload.get('event').get("notify_users_obj")
        tokens = {}
        for u in users:
            contacts = u.get("contacts")
            if contacts.get("wecom_robot_token", ""):
                tokens[contacts.get("wecom_robot_token", "")] = 1
            else:
                print("wecom_robot_token doesn't config!")
        for t in tokens:
            url = "https://qyapi.weixin.qq.com/"
            "cgi-bin/webhook/send?key={}".format(t)
            body = json.dumps({
                "msgtype": "markdown",
                "markdown": {
                    "content": payload.get('tpls').get("wecom.tpl",
                                                       "wecom.tpl not found")
                }
            })
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=body,
                                        proxies=proxies)
            print(response.text)
def main():
    payload = json.load(sys.stdin)
    with open(".payload", 'w') as f:
        f.write(json.dumps(payload, indent=4))
    for ch in payload.get('event').get('notify_channels'):
        send_func_name = "send_{}".format(notify_channel_funcs.get(ch.strip()))
        if not hasattr(Sender, send_func_name):
            print("function: {} not found", send_func_name)
            continue
        send_func = getattr(Sender, send_func_name)
        send_func(payload)
def hello():
    print("hello nightingale")
def testing():
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", sys.stdin, headers=headers, proxies=proxies)
    print(response.text)
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif sys.argv[1] == "hello":
        hello()
    elif sys.argv[1] == "test":
        testing()
    else:
        print("I am confused")