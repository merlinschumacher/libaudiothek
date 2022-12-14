"""libaudiothek &mdash; A Python library to access the audiothek.de API
This library provides a Python interface to the ARD Audiothek API.
"""

from datetime import datetime
from enum import Enum

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from .audiothek_schema import audiothek_schema as schema

# The base URL of the audiothek API.
URL = 'https://api.ardaudiothek.de'


class AudiothekEntryType(Enum):
    """A enum class used to represent the type of an AudiothekEntry."""
    ITEM = 0
    """Represents a single item"""
    PROGRAM = 1
    """Represents a program containing multiple items"""
    CATEGORY = 2
    """Represents a category of multiple programs"""
    COLLECTION = 3
    """Represents a collection of multiple programs"""


class AudiothekEntryMedia:
    """
    A class used to represent a media file associated with an item.

    Args:
        media_url (str): An url that points to the media file
    """

    def __init__(self, media_url: str) -> None:
        """
        Parameters
        ----------
        url (str): The url of the media file
        """
        self.url: str = media_url

    url = str


class AudiothekEntry:
    """A class used to represent an entry found in the Audiothek
    Args:
        entry_id (int): The ID of the item as it is returned by Audiothek
        title (str): The title of the item
        entry_type (AudiothekEntryType): The type of the entry
        program_id (int): The ID of the program associated with the item
        publish_date (datetime): The date when an element was published
        publisher (str): The station that published the media
        organization (str): The organization (Sendeanstalt) that published the media
        media (list[AudiothekEntryMedia]): A list of media elements linked to the element

    """

    def __init__(self, entry_id: int,
                 title: str,
                 entry_type: AudiothekEntryType,
                 program_id: int,
                 publish_date: datetime = datetime.fromtimestamp(0),
                 publisher: str = "",
                 organization: str = "",
                 media: list[AudiothekEntryMedia] = None) -> None:
        """ Initializes an AudiothekEntry
        Args:
            entry_id (int): The ID of the item as it is returned by Audiothek
            title (str): The title of the item
            entry_type (AudiothekEntryType): The type of the entry
            program_id (int): The ID of the program associated with the item
            publish_date (datetime): The date when an element was published
            publisher (str): The station that published the media
            organization (str): The organization (Sendeanstalt) that published the media
            media (list[AudiothekEntryMedia]): A list of media elements linked to the element
        """

        self.entry_id: int = entry_id
        self.title: str = title
        self.entry_type: AudiothekEntryType = entry_type
        self.program_id: int = program_id
        self.publish_date: datetime = publish_date
        self.publisher: str = publisher
        self.organization: str = organization
        self.media: list[AudiothekEntryMedia] = media or []

    def __str__(self):
        return f'{self.entry_type} - Title: {self.title}, Type: {self.entry_type}, ID: {self.entry_id}, Publication date: {self.publish_date}'

    def __repr__(self):
        return f'{self.entry_type} - Title: {self.title}, Type: {self.entry_type}, ID: {self.entry_id}, Publication date: {self.publish_date}'

    entry_id = int
    title = str
    entry_type = AudiothekEntryType
    program_id = int
    publish_date = datetime
    publisher = str
    organization = str
    media = [AudiothekEntryMedia]
    description = str
    synopsis = str


class AudiothekSearchResult:
    """The result of a search of the Audiothek API
        Args:
            items (list[AudiothekEntry]): A list of items found by the search
            program_sets (list[AudiothekEntry]): A list of programs found by the search
            result_count (int): The total number of results found by the search
    """

    def __init__(self, items: list[AudiothekEntry], program_sets: list[AudiothekEntry]) -> None:
        """Initializes an AudiothekSearchResult
        Args:
            items (list[AudiothekEntry]): A list of items found by the search
            program_sets (list[AudiothekEntry]): A list of programs found by the search
        """
        self.items: list[AudiothekEntry] = items
        self.program_sets: list[AudiothekEntry] = program_sets
        self.result_count: int = len(items) + len(program_sets)

    items = [AudiothekEntry]
    program_sets = [AudiothekEntry]
    result_count = int



class Audiothek:
    """A class used to request data from the ARD Audiothek API"""

    def __init__(self) -> None:
        self.endpoint: HTTPEndpoint = HTTPEndpoint(URL)
        self.op: Operation = Operation(schema.query_type)

    def __process_items(self, items: any) -> list[AudiothekEntry]:
        entries = []
        for node in items:
            entry: AudiothekEntry = AudiothekEntry(
                entry_id=node.id,
                title=node.title,
                entry_type=AudiothekEntryType.ITEM,
                program_id=node.program_set.publication_service.row_id,
                publish_date=node.publish_date,
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
            entry: AudiothekEntry = AudiothekEntry(
                entry_id=node.id,
                title=node.title,
                entry_type=AudiothekEntryType.PROGRAM,
                program_id=node.id,
                publish_date=node.last_item_added,
                publisher=node.publication_service.title,
                organization=node.publication_service.organization_name,
            )
            entries.append(entry)
        return entries

    def search(self, term: str) -> AudiothekSearchResult:
        """Searches the Audiothek for the given string and returns the results.

        Args:
        term (str): The string to search for in the Audiothek

        Returns:
            list[AudiothekEntry]
                A list of AudiothekEntry returned by the API
        
        Examples:
            Searching for "WDR" will return an AudiothekSearchResult with multiple AudiothekEntry objects
            >>> audiothek = Audiothek()
            >>> res = audiothek.search("WDR")
            >>> print(res.result_count)
            >>> print(res.items[0])
        """

        search = self.op.search(query=term)

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

        data = self.endpoint(self.op)
        obj = (self.op + data)

        items: list[AudiothekEntry] = self.__process_items(
            obj.search.items.nodes)
        program_sets: list[AudiothekEntry] = self.__process_program_sets(
            obj.search.program_sets.nodes)
        res: AudiothekSearchResult = AudiothekSearchResult(items, program_sets)

        return res
