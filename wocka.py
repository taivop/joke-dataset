from lxml import html
import requests
import json
import logging

logging.basicConfig(level=logging.ERROR)

def extract_joke(id):
    """Download and parse a single joke."""

    url_base = "http://www.wocka.com/{}.html"
    response = requests.get(url_base.format(id))

    tree = html.fromstring(response.content)
    content = tree.xpath('//div[@id="content"]')[0]
    h2s = tree.xpath('//div[@id="content"]/h2')
    category_rows = content.xpath('./div[@class="right"]//tr/td/b[text()="Category"]/../..')

    crap = tree.xpath('//div[@id="content"]/child::node()[not(self::text()) and not(self::br)]') # all html nodes in content, but not plaintext

    for node in crap:
        content.remove(node)

    body_text = content.text_content().strip()

    if body_text == "This joke does not exist":
        return None, "does not exist", None
    if body_text == "This is a dirty joke, so it has been hidden.  To read this joke, you will need to create an account and signin.":
        return None, "is dirty", None

    category = category_rows[0].xpath('./td/a/text()')[0]

    title = h2s[0]
    joke_title = title.text_content()
    joke_body = body_text

    return joke_title, joke_body, category


if __name__ == "__main__":

    jokes = []

    save_frequency = 100 # save after every 100 IDs
    max_id = 19000
    for id in range(1, max_id+1): #19000
        try:
            title, body, category = extract_joke(id)

            if title is None:
                print("ID {} {}.".format(id, body))
                continue

            joke = {"id": id, "category": category, "title": title, "body": body}
            jokes.append(joke)
            print("ID {} success: [{}] {}".format(id, category, title))
        except Exception as ex:
            print("ID {} failed: ".format(id))
            logging.error(ex)

        if id % save_frequency == 0 or id == max_id:
            with open("wocka.json", "w") as f:
                json.dump(jokes, f, indent=4, sort_keys=True)