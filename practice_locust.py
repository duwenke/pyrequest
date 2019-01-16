# -*- coding:utf-8 -*-
'''
@author: 
@file: practice_locust.py
@time: 2018/11/12 15:29
@desc:
'''
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("/test/redis")
    # @task(2)
    # def baidu2(self):
    #     self.client.get("/#/exchange?symbol=ZXT-KTC")



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # host = "https://bibo.gold/#/"
    min_wait = 3000
    max_wait = 6000