# JSON styling guidelines
This document documents the specific guidelines for generating a `subreddits.json` file, used by the program Termiddit.

## Filename
The filename can be changed dynamically, but must match the filename in `fetch.py`. The default filename is `subreddits.json`.

Generally, it is good practice to name your file `subreddits.json`, unless you're planning on using multiple different lists. You can request with a custom list by using the `-s` argument.

## Internal formatting
- ### `name` (required)
    The `name` section has a datatype of a string. This section defines the list's name, as outputted in the last line (`Fetch * posts from list "[name]"`)

- ### `subreddits` (required)
    This section is a list, and contains the list of subreddits to fetch from. 
     
    By default, the list provided from the GitHub repository consist of four subreddits, however, you can add it to any amount. However, the application will only display 25 results maximum, no matter how many subreddits.

    Subreddits such as `r/all` and `r/popular` do work as well. However, they are not marked in the "Posted on" section, and instead are marked by the posts' original subreddit(s).

## Other notes
Crossposts, as far as my knowledge goes, do not work.