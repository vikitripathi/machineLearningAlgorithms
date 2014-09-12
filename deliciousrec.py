# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 02:32:28 2014

@author: img-05
"""
from pydelicious import get_popular,get_userposts,get_urlposts
import time

def initializeUserDict(tag,count=5):
  user_dict={}
  # get the top count' popular posts
  for p1 in get_popular(tag=tag)[0:count]:
    # find all users who posted this , what does this mean???
    print p1 # to know about the structure of p1
    for p2 in get_urlposts(p1['href']):
      #print p2  
      user=p2['user']
      print user
      user_dict[user]={}
  return user_dict

def fillItems(user_dict):
  all_items={}
  # Find links posted by all users
  for user in user_dict:
    print user  
    for i in range(3):
      try:
        posts=get_userposts(user)
        break
      except:
        print "Failed user "+user+", retrying"
        time.sleep(4)
    for post in posts:
      url=post['href']
      print url
      user_dict[user][url]=1.0
      all_items[url]=1
  
  # Fill in missing items with 0
  for ratings in user_dict.values():
    for item in all_items:
      if item not in ratings:
        ratings[item]=0.0
