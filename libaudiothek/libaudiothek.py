# from sgqlc.endpoint.http import HTTPEndpoint

# url = 'https://api.ardaudiothek.de'

# query = 'query { ... }'
# variables = {'term': 'kalk und welk'}

# endpoint = HTTPEndpoint(url)
# data = endpoint(query, variables)

from datetime import datetime
from enum import Enum
import pprint
from pydoc import describe
from sqlite3 import Date
from sre_parse import CATEGORIES
from sgqlc.operation import Operation
from audiothek_schema import Item, Organization, PublicationService, audiothek_schema as schema
from sgqlc.endpoint.http import HTTPEndpoint

op = Operation(schema.query_type)

url = 'https://api.ardaudiothek.de'
endpoint = HTTPEndpoint(url)


class AudiothekEntryType(Enum):
    ITEM = 0
    PROGRAM = 1
    CATEGORY = 2
    COLLECTION = 3


class AudiothekEntryMedia:
    def __init__(self, url: str) -> None:
        self.url = url
    url = str


class AudiothekEntry:
    def __init__(self, id: int, title: str, type: AudiothekEntryType, program_id: int, publish_date: datetime = datetime.fromtimestamp(0), publisher: str = "", organization: str = "", media: list[AudiothekEntryMedia] = []) -> None:
        self.id = id
        self.title = title
        self.type = type
        self.publish_date = publish_date
        self.publisher = publisher
        self.organization = organization
        self.media = media

    def __str__(self):
        return f'Title: {self.title}, Type: {self.type}, ID: {self.id}, Publication date: {self.publish_date}'

    id = int
    title = str
    type = AudiothekEntryType
    publish_date = datetime
    publisher = str
    organization = str
    media = [AudiothekEntryMedia]
    description = str
    synopsis = str
    program_id = int


def search(term: str) -> list[AudiothekEntry]:
    search = op.search(query=term)

    search.items().nodes.__fields__(
        'id', 'title', 'publish_date', 'description', 'synopsis', 'url')
    search.items().nodes().audios()
    search.items().nodes().program_set.__fields__(
        'row_id', 'title', 'synopsis', 'description', 'sharing_url')
    search.items().nodes().program_set().publication_service()
    search.program_sets().nodes().__fields__(
        'id', 'title', 'description', 'synopsis', 'sharing_url', 'last_item_added')
    search.program_sets().nodes().publication_service()

    data = endpoint(op)
    obj = (op + data)

    res = []

    for node in obj.search.items.nodes:
        entry = AudiothekEntry(
            id=node.id,
            title=node.title,
            type=AudiothekEntryType.ITEM,
            program_id=node.program_set.publication_service.row_id,
            publish_date=datetime.fromisoformat(node.publish_date),
            publisher=node.program_set.publication_service.title,
            organization=node.program_set.publication_service.organization_name,

        )

        for audio in node.audios:
            entry.media.append(
                AudiothekEntryMedia(audio.url)
            )
        res.append(entry)

    for node in obj.search.program_sets.nodes:
        entry = AudiothekEntry(
            id=node.id,
            title=node.title,
            type=AudiothekEntryType.PROGRAM,
            program_id=node.id,
            publish_date=datetime.fromisoformat(node.last_item_added),
            publisher=node.publication_service.title,
            organization=node.publication_service.organization_name,
        )

    return res


pprint.pprint(search("Kalk und Welk"))
