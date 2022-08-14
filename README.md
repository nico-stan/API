# Project IV My API
## API - SQL query for US Presidential Speeches

By: Nicolas Stambolsky
Date: August, 15th 2022

![Screenshot](https://github.com/nico-stan/Project-IV/blob/main/images/waving_eagle.gif)
________________________________________________

# How does it work?

First: make sure you have a `.env` file with your databases info.

# @POST
Endpoint
- /new/sentence

We'll insert a new sentence into the database


# @GET
Endpoint
- /sentence/<name>

We'll extract all the sentences from a user in the database

```
url_sentences = "http://localhost:5000/sentence/"
name = "Albus Dumbledore"
```
