# A dataset of about 200k English plaintext jokes.


### Files
Currently the dataset contains jokes from three sources, each in a different file.

```
----------------------------------------------
reddit_jokes.json |  195K jokes | 7.40M tokens
stupidstuff.json  | 3.77K jokes |  396K tokens
wocka.json        | 10.0K jokes | 1.11M tokens
----------------------------------------------
TOTAL             |  208K jokes | 8.91M tokens
----------------------------------------------
```

### Format
Each file is a JSON document, containing a flat list of joke objects. Each joke object always has the `body` field with additional fields varying based on the dataset, described below.

#### **reddit_jokes.json**
Scraped from [/r/jokes](https://www.reddit.com/r/jokes).

Additional fields:

* id
* score
* title

```json
{
        "body": "I said, \"I'm not sure; it's hard to keep track.\"",
        "id": "5tyytx",
        "score": 3,
        "title": "My boss said to me, \"you're the worst train driver ever. How many have you derailed this year?\""
    }
```


### License
