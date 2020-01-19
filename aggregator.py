#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:53:42 2019
@author: henry-mac
"""
import math

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

test_player1 = ['Charles Oakley', '50', '3.8', '2.2', '33.8', '34.6', '86.2', '0.4', '0.2', '0.2', '0.1', '0.1', '1.5']
test_player2 = ['Charles Oakley', '48', '2.8', '0.6', '39.1', '0.0', '76.5', '1.1', '0.1', '0.1', '0.0', '0.0', '1.3']
##['Player Name', 'GP', 'Min', 'PTS', 'FG%', '3P%', 'FT%', 'REB', 'AST', 'TOV', 'STL', 'BLK', '+/-']
def aggregate (player1, player2):
    GP1 = int(player1[1])
    GP2 = int(player2[1])
    li = [player1[0], str(GP1 + GP2)]
    for i in range(2, 13):
        adj = str(truncate(((float(player1[i]) * GP1) + (float(player2[i]) * GP2))/(GP1 + GP2), 2))
        li.append(adj)
    return li

###x is a player name, list is a list of player data
def contains (x, li):
    for i in li:
        if x == i[0]:
            return True
    return False;
               
def combine (list1, list2):
    ##for each element in list1, find matching one in list2, aggregate stats accordingly into new_list
    ##then for each element in list2, check if that player is in new_list, if not add it
    new_list = []
    for player1 in list1:
        print(player1[0])
        if not contains(player1[0], list2):
            new_list.append(player1)
    for player2 in list2:
        if not contains(player2[0], list1):
            new_list.append(player2)
    for player1 in list1:
        for player2 in list2:
            if player1[0] == player2[0]:
                new_list.append(aggregate(player1, player2))
    return new_list

to_combine = [last_30_2017, last_30_2016, last_30_2015, last_30_2014, last_30_2013, last_30_2012, last_30_2011\
        , last_30_2010, last_30_2009, last_30_2008, last_30_2007, last_30_2006, last_30_2005, last_30_2004, last_30_2003\
        , last_30_2002, last_30_2001, last_30_2000, last_30_1999, last_30_1998, last_30_1997, last_30_1996]

last_30_all = last_30_2018
for li in to_combine:
    last_30_all = combine(last_30_all, li)
    
##check for repeating players in last_5_all
##combine with 2019
##repeat whole process for last_2 and last_30

        
