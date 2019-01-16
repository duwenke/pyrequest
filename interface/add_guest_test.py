# -*- coding:utf-8 -*-
'''
@author: 
@file: add_guest_test.py
@time: 2018/10/11 13:49
@desc:
'''
import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

class AddGuestTest(unittest.TestCase):
    '''添加嘉宾'''
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/add_guest/'

    def test_add_guest_all_null(self):
        '''所有参数为空'''
        par = {'eid':'',
               'realname':'',
               'phone':'',
               'email':''
               }
        r = requests.post(self.base_url,par)
        self.result = r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'参数错误')
    def test_add_guest_eid_null(self):
        '''事件id为空'''
        par = {'eid':100,
               'realname':'test',
               'phone':'18012345670',
               'email':'test@qq.com'
               }
        r = requests.post(self.base_url, par)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], '事件id不存在')
    def test_add_guest_status_close(self):
        '''eid = 3 状态未开启'''
        par = {'eid':3,
               'realname': 'test',
               'phone': '18012345671',
               'email': 'test@qq.com'
               }
        r = requests.post(self.base_url, par)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], '事件状态不可用')
    def test_add_guest_limit_full(self):
        '''发布会人数已满'''
        par = {'eid':2,
               'realname': 'test',
               'phone': '18012345672',
               'email': 'test@qq.com'
               }
        r = requests.post(self.base_url, par)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], '发布会人数已满')
    def test_add_guest_starttime_start(self):
        '''发布会开始时间已过'''
        par = {'eid':4,
               'realname':'test',
               'phone': '18012345673',
               'email': 'test@qq.com'
               }
        r = requests.post(self.base_url, par)
        print(r)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'event has started')
    def test_add_guest_phone_existed(self):
        '''手机号已存在'''
        par = {'eid':1,
               'realname':'test',
               'phone': '13511001100',
               'email': 'test@qq.com'
               }
        r = requests.post(self.base_url, par)
        print(r)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], '手机号已存在')
    def test_add_guest_success(self):
        '''添加成功'''
        par = {'eid':1,
               'realname':'test',
               'phone': '13511001109',
               'email': 'test@qq.com'
               }
        r = requests.post(self.base_url, par)
        print(r)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add guest success')
    def tearDown(self):
        print(self.result)
if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()


