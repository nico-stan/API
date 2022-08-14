# Project IV My API
## API - SQL query for US Presidential Speeches

By: Nicolas Stambolsky
Date: August, 15th 2022

![Screenshot](https://github.com/nico-stan/Project-IV/blob/main/images/waving_eagle.gif)
________________________________________________

## Main Endpoint page for the API query:
    http://127.0.0.1:5001/

## 1 - Endpoint route for generating a Random Number:
As a gift, I created a special feature that generates a number between 0 and 1000.
This special feature is just to test the access to the endpoint route.
    http://127.0.0.1:5001/random-number 
    
## 2 - Endpoint route for a dictionary of all presidential speeches:
Query all US presidential speeches ever spoken until september 2019, ordered chronologically.
    http://127.0.0.1:5001/speeches
    
## 3 - Endpoint route for a dictionary of all the Presidents:
Query all US presidents until september 2019, ordered alphabetically.
    http://127.0.0.1:5001/presidents
    
## 4 - Endpoint route for a dictionary of all the Parties:
Query all US Parties until september 2019, ordered alphabetically.
    http://127.0.0.1:5001/parties
    
## 5 - Endpoint route for a Polarity Score of a given President.
Combines all speeches ever spoken by a given President and shows its polarity score.
    http://127.0.0.1:5001/sentiment/president/<president>
  
## 6 - Endpoint route for a Polarity Score of a given Party.
Combines all speeches ever spoken by a given Party and shows its polarity score.
    http://127.0.0.1:5001/sentiment/party/<party>
    
## 7 - Endpoint route for translating:
...
    http://127.0.0.1:5001/one/<name>

## 8 - Endpoint route for posting:
Inserts a new line in the database.
    http://127.0.0.1:5001/newline
