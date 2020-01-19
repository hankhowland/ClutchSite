#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:13:40 2019

@author: henry-mac
"""

#How it would work:
#Have separate data frames with the stats for absolute and relative for each time frame
#When click selectors change which data frame you are selecting out of
#When search players and hit add, it searches the player names for that string and adds the row to the data table that is being displayed if it matches
#Checks for low minutes played, puts asterisk after player name if too low

######Data Collection######
#want to make files with just the stats I want where the first list in the list of lists is the headers
#need to iterate through all seasons and aggregate them together when appropriate
#need to figure out git and start committing the file to there
from selenium import webdriver
import itertools
from bs4 import BeautifulSoup as soup 
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/henry-mac/Downloads/chromedriver')

######function that takes in a link to an nba.com page and extracts/cleans the data in it
##and adds headers at the beginning of the list
##stats are ['Player Name', 'GP', 'Min', 'PTS', 'FG%', '3P%', 'FT%', 'REB', 'AST', 'TOV', 'STL', 'BLK', '+/-']
def get_data (link, menu_xpath) :
    
#open page
    driver.get(link)

##find page options dropdown menu and click on all to make table include all the values
    droplist= Select(driver.find_element_by_xpath(menu_xpath))
    droplist.select_by_value('string:All')

##extract the data from a page
    s = soup(driver.page_source, 'html.parser').find('table', {'class':'table'})
    headers, [_, *data] = [i.text for i in s.find_all('th')], [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]
    final_data = [i for i in data if len(i) > 1] 
##final data is a list of lists that are of length 30
    player_example = ['1', '\nChris Paul\n', '\nOKC\n', '34', '21', '11', '10', '3.7', '3.3', 
                  '\n            1.0\n', '\n            2.0\n', '50.0', '\n            0.3\n', '\n            0.7\n', '40.0', '1.0',
                  '1.0', '95.5', '\n            0.0\n', '\n            0.4\n', '\n            0.4\n',
                  '\n            0.4\n', '\n            0.1\n', '\n            0.3\n', 
                  '\n            0.0\n', '\n            0.5\n', '\n            5.3\n          ', '1', '0', '1.5']

##making function to clean the list of lists
    def clean_stat (stat) :
        k = stat.strip()
        return k.strip('\n');
    
    def clean_player (player) :
        indices = [0,2,3,5,6,9,10,12,13,15,16,18,19,25,26,27,28]
        for i in sorted(indices, reverse=True):
            del player[i]
        return list(map(clean_stat, player));
    
    clean_example = clean_player(player_example)
    
    def clean_data (data):
        return list(map(clean_player, data));
    
    final_data_cl = clean_data(final_data)
    
    return final_data_cl;

##season label is the year the season started in
##traditional data from last 5 minutes of games within 5 pts
##link format: "https://stats.nba.com/players/clutch-traditional/?sort=GP&dir
##=-1&Season=1997-98&SeasonType=Regular%20Season"
#last_5_19 = get_data("https://stats.nba.com/players/clutch-traditional/?sort=GP&dir=-1", "/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
def last_5_link (year):
    return "https://stats.nba.com/players/clutch-traditional/?sort=GP&dir=-1&Season="\
    + str(year) + "&SeasonType=Regular%20Season"

def last_2_link (year):
    return "https://stats.nba.com/players/clutch-traditional/?sort=GP&dir=-1&Season="\
    + str(year) + "&SeasonType=Regular%20Season&ClutchTime=Last%202%20Minutes&PointDiff=4"
    
def last_30_link (year):
    return "https://stats.nba.com/players/clutch-traditional/?sort=GP&dir=-1&Season="\
    + str(year) + "&SeasonType=Regular%20Season&ClutchTime=Last%2030%20Seconds&PointDiff=3"

def playoffsLink (year):
    return "https://stats.nba.com/players/traditional/?Season="\
    + str(year) + "&SeasonType=Playoffs&sort=PTS&dir=-1"

last_30_2018 = get_data(playoffsLink('2018-19'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2017 = get_data(playoffsLink('2017-18'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2016 = get_data(playoffsLink('2016-17'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2015 = get_data(playoffsLink('2015-16'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2014 = get_data(playoffsLink('2014-15'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2013 = get_data(playoffsLink('2013-14'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2012 = get_data(playoffsLink('2012-13'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2011 = get_data(playoffsLink('2011-12'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2010 = get_data(playoffsLink('2010-11'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2009 = get_data(playoffsLink('2009-10'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2008 = get_data(playoffsLink('2008-09'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2007 = get_data(playoffsLink('2007-08'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2006 = get_data(playoffsLink('2006-07'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2005 = get_data(playoffsLink('2005-06'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2004 = get_data(playoffsLink('2004-05'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2003 = get_data(playoffsLink('2003-04'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2002 = get_data(playoffsLink('2002-03'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2001 = get_data(playoffsLink('2001-02'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_2000 = get_data(playoffsLink('2000-01'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_1999 = get_data(playoffsLink('1999-00'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_1998 = get_data(playoffsLink('1998-99'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_1997 = get_data(playoffsLink('1997-98'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")
last_30_1996 = get_data(playoffsLink('1996-97'),"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select")

##traditional data from last 2 minutes of games within 5 pts

##traditional data from last 30 seconds of games within 3 pts

#####plan to aggregate:
#get data from each season
#for each player, if big data fram contains player already, skip, if not,
#go through all seasons and aggregate all stats for that player, then add that to the big data frame

