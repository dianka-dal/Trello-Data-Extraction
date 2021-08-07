from trello.trelloclient import TrelloClient
import csv

TRELLO_API_KEY = ''
TRELLO_TOKEN = ''
API_SECRET = ''
client = TrelloClient(TRELLO_API_KEY, API_SECRET, TRELLO_TOKEN)

all_boards = client.list_boards()

with open("boards_and_cards.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    for board in all_boards:
        writer.writerow([board])
        lists = board.list_lists()
        for l in lists:
            writer.writerow([l])
            cards = l.list_cards()
            for c in cards:
                writer.writerow([c])
        writer.writerow('')

