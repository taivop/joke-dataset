# A dataset of English plaintext jokes

There are about 208 000 jokes in this database scraped from three sources.

I make no claim on ownership of these files, nor do I necessarily endorse the jokes in them. This dataset is provided for research purposes (see License section below).


## Files
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

## Format
Each file is a JSON document, containing a flat list of joke objects. Each joke object always has the `body` field with additional fields varying based on the dataset, described below.

Obviously they are not all funny; to find the best ones, sort on the relevant additional fields.

Note that the title is in part of the joke many cases (especially for Reddit submissions).

### reddit_jokes.json
Scraped from [/r/jokes](https://www.reddit.com/r/jokes). Contains all submissions to the subreddit as of 13.02.2017.

These jokes may have additional comments in them ([example](https://www.reddit.com/r/Jokes/comments/5k9tgu/this_is_the_dirty_joke_my_85yo_grandad_told_to/)).

Additional fields:

* `id` -- submission ID in the subreddit.
* `score` -- post score displayed on Reddit.
* `title` -- title of the submission.

```json
{
        "title": "My boss said to me, \"you're the worst train driver ever. How many have you derailed this year?\"",
        "body": "I said, \"I'm not sure; it's hard to keep track.\"",
        "id": "5tyytx",
        "score": 3
    }
```

### stupidstuff.json
Scraped from [stupidstuff.org](stupidstuff.org/jokes/).

Additional fields:

* `id` -- page ID on stupidstuff.org.
* `category` -- see available categories [here](http://stupidstuff.org/jokes/category.htm).
* `rating` -- mean user rating on a scale of 1 to 5.

```json
{
        "category": "Blonde Jokes",
        "body": "A blonde is walking down the street with her blouse open, exposing one of her breasts. A nearby policeman approaches her and remarks, \"Ma'am, are you aware that I could cite you for indecent exposure?\" \"Why, officer?\" asks the blonde. \"Because your blouse is open and your breast is exposed.\" \"Oh my goodness,\" exclaims the blonde, \"I must have left my baby on the bus!\"",
        "id": 14,
        "rating": 3.5
    }
```


### wocka.json
Scraped from [wocka.com](http://wocka.com/).

Additional fields:

* `id` -- page ID on wocka.com.
* `category` -- see available categories [here](http://www.wocka.com/).
* `title` -- title of the joke.

```json
{
        "title": "Infants vs Adults",
        "body": "Do infants enjoy infancy as much as adults enjoy adultery?",
        "category": "One Liners",
        "id": 17
    }
```


## License
I provide this dataset for research purposes and make no ownership claim on any part of it. The question of copyright in the case of jokes is unclear and I recommend not using the dataset commercially.

For removal of copyrighted content, please contact me on GitHub.

## Citing
If you use this dataset in academic work, please cite as follows:

```bibtex
@misc{pungas,
        title={A dataset of English plaintext jokes.},
        url={https://github.com/taivop/joke-dataset},
        author={Pungas, Taivo},
        year={2017},
        publisher = {GitHub},
        journal = {GitHub repository}
}
```
