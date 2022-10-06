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
    """
    A enum class used to represent the type of an AudiothekEntry.

    ...

    ITEM 
        Represents a single item
    PROGRAM 
        Represents a program containing multiple items
    CATEGORY
        Represents a category of multiple programs
    Collection 
        Represents a collection of multiple programs

    """
    ITEM = 0
    PROGRAM = 1
    CATEGORY = 2
    COLLECTION = 3


class AudiothekEntryMedia:
    """
    A class used to represent a media file associated with an item.

    ...

    Attributes
    ----------
    url : str
        An url that points to the media file
    """

    def __init__(self, url: str) -> None:
        """
        Parameters
        ----------
        url : str
            The url of the media file
        """
        self.url = url
    url = str


class AudiothekEntry:
    """
    A class used to represent an entry found in the Audiothek

    ...

    Attributes
    ----------
    id : int
        The ID of the item as it is returned by Audiothek
    title : str
        The title of the item
    type : AudiothekEntryType
        The type of the entry
    program_id : int
        The ID of the program associated with the item as it is returned by Audiothek
    publish_date : datetime
        The date when an element was published
    publisher : str
        The station that published the media
    organization : str
        The organization (Sendeanstalt) that published the media
    media : list[AudiothekEntryMedia]
        A list of media elements linked to the element
    """

    def __init__(self, id: int, title: str, type: AudiothekEntryType, program_id: int, publish_date: datetime = datetime.fromtimestamp(0), publisher: str = "", organization: str = "", media: list[AudiothekEntryMedia] = []) -> None:
        """
        Parameters 
        ----------
        id : int
            The ID of the item as it is returned by Audiothek
        title : str
            The title of the item
        type : AudiothekEntryType
            The type of the entry
        program_id : int
            The ID of the program associated with the item as it is returned by Audiothek
        publish_date : datetime
            The date when an element was published
        publisher : str
            The station that published the media
        organization : str
            The organization (Sendeanstalt) that published the media
        media : list[AudiothekEntryMedia]
            A list of media elements linked to the element
        """

        self.id = id
        self.title = title
        self.type = type
        self.program_id = program_id
        self.publish_date = publish_date
        self.publisher = publisher
        self.organization = organization
        self.media = media

    def __str__(self):
        return f'{self.type} - Title: {self.title}, Type: {self.type}, ID: {self.id}, Publication date: {self.publish_date}'

    def __repr__(self):
        return f'{self.type} - Title: {self.title}, Type: {self.type}, ID: {self.id}, Publication date: {self.publish_date}'

    id = int
    title = str
    type = AudiothekEntryType
    program_id = int
    publish_date = datetime
    publisher = str
    organization = str
    media = [AudiothekEntryMedia]
    description = str
    synopsis = str


class Audiothek:
    """
    A class used to request data from the ARD Audiothek API

    Methods
    -------
    search(term)
        Searches the Audiothek for the given string and returns the results.

    """

    def __process_items(self, items: any) -> list[AudiothekEntry]:
        entries = []
        for node in items:
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
            entries.append(entry)
        return entries

    def __process_program_sets(self, items: any) -> list[AudiothekEntry]:
        entries = []
        for node in items:
            entry = AudiothekEntry(
                id=node.id,
                title=node.title,
                type=AudiothekEntryType.PROGRAM,
                program_id=node.id,
                publish_date=datetime.fromisoformat(node.last_item_added),
                publisher=node.publication_service.title,
                organization=node.publication_service.organization_name,
            )
            entries.append(entry)
        return entries

    def search(self, term: str) -> list[AudiothekEntry]:
        """
        Searches the Audiothek for the given string and returns the results.

        Parameter
        ---------
        term : str
            The string to search for in the Audiothek

        Returns
        -------
        list[AudiothekEntry]
            A list of AudiothekEntry returned by the API
        """

        search = op.search(query=term)

        # retrieve the fields needed for the items
        search.items().nodes.__fields__(
            'id', 'title', 'publish_date', 'description', 'synopsis', 'url')
        search.items().nodes().audios()

        # retrieve the fields needed for the program sets
        search.items().nodes().program_set.__fields__(
            'row_id', 'title', 'synopsis', 'description', 'sharing_url')
        search.items().nodes().program_set().publication_service()
        search.program_sets().nodes().__fields__(
            'id', 'title', 'description', 'synopsis', 'sharing_url', 'last_item_added')
        search.program_sets().nodes().publication_service()

        data = endpoint(op)
        obj = (op + data)

        res = []

        items = self.__process_items(obj.search.items.nodes)
        program_sets = self.__process_program_sets(
            obj.search.program_sets.nodes)
        res.append(items)
        res.append(program_sets)

        return res
