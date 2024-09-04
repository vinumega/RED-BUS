                 ** DATA SCRAPING WITH SELENIUM DYNAMIC FILTERING USING STREAMLIT AND SELENIUM**

**INTRODUCTION:**
The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

**DOMAIN:**
TRANSPORTATION

**SKILL:**
Python scripting
Selenium
Data Collection
Data Management using SQL
Streamlit

**TECHNOLOGY USED**
Python 3.9.I
MySQL 8.0
Streamlit
Selenium

**FEATURES OF APPLICATION**

1.Retrive the Bus Information

2.Selenium is a powerful tool for automating web browsers, which is especially useful for web scraping tasks.

3.If you want to retrieve bus details from RedBus, you can use Selenium to automate the process of searching for buses and extracting the relevant information. 

4.This involves interacting with web elements like input 

a)fields and buttons 
b)waiting for the page to load
c)extracting the desired details from the search results.

**STORE DATA IN DATABASE:**
The collected bus details data was transformed into pandas dataframes. Before that, a new database and tables were created using the MySQL connector. With the help of MySQL, the data was inserted into the respective tables. The database could be accessed and managed in the MySQL environment.

**web app -**

streamlit:

With the help of Streamlit, you can create an interactive application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices

**PACKAGES AND LIBRARIES:****

*pandas as pd

*mysql.connector

*import time

*streamlit as slt

*import datetime

*from streamlit_option_menu import option_menu

*from selenium import webdriver


**DATA SCRAPING:**
     At first step using the htmal tag of the respective state link the "x.path " is identified and given to the selenium code.The path link reads the respective route names and the links of the 10 states kerala,telanga,andhra,bangalore,harayana,delhi,rajastan,goa,assam,west bengal.
     then from the elements on tghe link the coressponding Bus Id,Bus route,Bus name,PRICE,rating,Sleeper, AC sleeper,Rating.above execution of the code the list of state routes ands state names list his driven into the path given in the code.The final full list of staes routes price and bus types is yuploaded to the streamlit for the  describing the data inn the web page provided by us


**STREAMLIT:**
   The above tool provides the webpafe dispaly  the data given accordingb the given conditions.
   
   In this project redbus the display includes the filtering of the states and the pricing rating  type of bus .The final result of the red bus project is done
         
