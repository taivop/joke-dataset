from lxml import html
import requests
import json
import logging
import re

re_category_rating = re.compile(r"\s*Category: (.*[A-z])\s*Rating: (.*\d)\s*")

logging.basicConfig(level=logging.ERROR)

def extract_joke(id):
    """Download and parse a single joke."""

    url_base = "http://stupidstuff.org/jokes/joke.htm?jokeid={}"
    response = requests.get(url_base.format(id))

    tree = html.fromstring(response.content)
    content = tree.xpath('//table[@bgcolor="#ffffff" and @width="470"]//table[@class="scroll"]//td')[0]
    category_rating_cells = content.xpath('//table[@bgcolor="#ffffff"]//table[@class="bkline"]//td/b[text()="Category: "]/..')
    #print(category_rating_cell)

    crap = content.xpath('./child::node()[not(self::text()) and not(self::br)]') # all html nodes in content, but not plaintext

    for node in crap:
        content.remove(node)

    body_text = content.text_content().strip()
    joke_body = body_text

    cell_text = category_rating_cells[0].text_content()

    match = re_category_rating.search(cell_text)
    category = match.group(1)
    rating = float(match.group(2))

    return joke_body, category, rating


if __name__ == "__main__":

    jokes = []

    save_frequency = 100 # save after every 100 IDs
    max_id = 3773
    for id in range(1, max_id+1): #19000
        try:
            body, category, rating = extract_joke(id)

            joke = {"id": id, "category": category, "body": body, "rating": rating}
            jokes.append(joke)
            print("ID {} success: [{}]".format(id, category))
        except Exception as ex:
            print("ID {} failed: ".format(id))
            logging.error(ex)
            raise ex

        if id % save_frequency == 0 or id == max_id:
            with open("stupidstuff.json", "w") as f:
                json.dump(jokes, f, indent=4, sort_keys=True)