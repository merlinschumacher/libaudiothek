import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


audiothek_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
audiothek_schema -= sgqlc.types.relay.Node
audiothek_schema -= sgqlc.types.relay.PageInfo


########################################################################
# Scalars and Enumerations
########################################################################
class AspectRatio(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('ASPECT_16x9', 'SQUARE')


class BigInt(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class BookmarkListSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'ENTRIES_BOOKMARKEDAT_ASC', 'ENTRIES_BOOKMARKEDAT_DESC', 'ENTRIES_CREATEDAT_ASC', 'ENTRIES_CREATEDAT_DESC',
                   'ENTRIES_ITEM_ID_ASC', 'ENTRIES_ITEM_ID_DESC', 'ENTRIES_MODIFIEDAT_ASC', 'ENTRIES_MODIFIEDAT_DESC', 'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC')


class BookmarkSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('BOOKMARKEDAT_ASC', 'BOOKMARKEDAT_DESC', 'CREATEDAT_ASC',
                   'CREATEDAT_DESC', 'ITEM_ID_ASC', 'ITEM_ID_DESC', 'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC')


Boolean = sgqlc.types.Boolean


class CacheControlScope(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('PRIVATE', 'PUBLIC')


class CategoriesToProgramSetsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CATEGORY_SOPHORA_ID_ASC', 'CATEGORY_SOPHORA_ID_DESC', 'NATURAL',
                   'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROGRAM_SET_CORE_ID_ASC', 'PROGRAM_SET_CORE_ID_DESC')


class ConceptsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CONCEPT_SOURCE_ASC', 'CONCEPT_SOURCE_DESC', 'DATA_ASC', 'DATA_DESC', 'ITEM_ID_ASC', 'ITEM_ID_DESC',
                   'LAST_UPDATED_AT_ASC', 'LAST_UPDATED_AT_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ConfigsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('KEY_ASC', 'KEY_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC',
                   'UPDATED_AT_ASC', 'UPDATED_AT_DESC', 'UPDATED_BY_ASC', 'UPDATED_BY_DESC', 'VALUE_ASC', 'VALUE_DESC')


class Cursor(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


DateTime = sgqlc.types.datetime.DateTime


class Datetime(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class DurationVariant(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('ISO8601', 'SECONDS')


class EditorialCategoriesOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('ID_ASC', 'ID_DESC', 'IMAGE_ASC', 'IMAGE_DESC', 'NATURAL', 'ORDER_ASC', 'ORDER_DESC',
                   'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SOPHORA_ID_ASC', 'SOPHORA_ID_DESC', 'TITLE_ASC', 'TITLE_DESC')


class EditorialCollectionsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('BROADCAST_DURATION_ASC', 'BROADCAST_DURATION_DESC', 'COREMEDIA_ID_ASC', 'COREMEDIA_ID_DESC', 'IMAGE_ASC', 'IMAGE_DESC', 'NATURAL', 'NUMBER_OF_ELEMENTS_ASC',
                   'NUMBER_OF_ELEMENTS_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SOPHORA_ID_ASC', 'SOPHORA_ID_DESC', 'SYNOPSIS_ASC', 'SYNOPSIS_DESC', 'TITLE_ASC', 'TITLE_DESC')


class EndUserSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'LOCALID_ASC', 'LOCALID_DESC', 'LOGINID_ASC',
                   'LOGINID_DESC', 'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC', 'SYNCSUCCESSFUL_ASC', 'SYNCSUCCESSFUL_DESC')


Float = sgqlc.types.Float


class GroupingsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CORE_DOCUMENT_ASC', 'CORE_DOCUMENT_DESC', 'CORE_ID_ASC', 'CORE_ID_DESC', 'COUNT_ASC', 'COUNT_DESC', 'ID_ASC', 'ID_DESC', 'ITEM_LABEL_ASC', 'ITEM_LABEL_DESC', 'LAST_MODIFIED_ASC', 'LAST_MODIFIED_DESC',
                   'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROGRAMSET_ID_ASC', 'PROGRAMSET_ID_DESC', 'SEASON_NUMBER_ASC', 'SEASON_NUMBER_DESC', 'SHOW_ID_ASC', 'SHOW_ID_DESC', 'TITLE_ASC', 'TITLE_DESC', 'TYPE_ASC', 'TYPE_DESC')


class Grouptype(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('MULTIPART', 'SEASON', 'SERIES')


class HTML(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class HistoryEntrySortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'ITEM_ID_ASC', 'ITEM_ID_DESC', 'LASTLISTENEDAT_ASC',
                   'LASTLISTENEDAT_DESC', 'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC', 'PROGRESS_ASC', 'PROGRESS_DESC')


ID = sgqlc.types.ID


class ImagesCollectionsBinariesViewsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('ASPECT_RATIO_ASC', 'ASPECT_RATIO_DESC', 'FILE_LOCATION_ASC', 'FILE_LOCATION_DESC', 'HEIGHT_ASC', 'HEIGHT_DESC', 'IMAGE_BINARY_ID_ASC', 'IMAGE_BINARY_ID_DESC', 'IMAGE_COLLECTION_ID_ASC',
                   'IMAGE_COLLECTION_ID_DESC', 'IMAGE_ID_ASC', 'IMAGE_ID_DESC', 'MEDIA_TYPE_ASC', 'MEDIA_TYPE_DESC', 'NATURAL', 'PRODUCER_NAME_ASC', 'PRODUCER_NAME_DESC', 'TITLE_ASC', 'TITLE_DESC', 'WIDTH_ASC', 'WIDTH_DESC')


Int = sgqlc.types.Int


class ItemRecVariant(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('DETAIL_1', 'DETAIL_2', 'NOT_FOUND')


class ItemSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('ID_ASC', 'ID_DESC')


class ItemType(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('EPISODE', 'EVENT_LIVESTREAM', 'EXTRA', 'SECTION')


class ItemsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('AUDIO_BINARY_ID_ASC', 'AUDIO_BINARY_ID_DESC', 'BACKEND_DOCUMENT_ASC', 'BACKEND_DOCUMENT_DESC', 'BACKEND_DOCUMENT_HASH_ASC', 'BACKEND_DOCUMENT_HASH_DESC', 'CODEX_LAST_PUBLISHED_ASC', 'CODEX_LAST_PUBLISHED_DESC', 'CODEX_PENDING_ASC', 'CODEX_PENDING_DESC', 'CORE_DOCUMENT_ASC', 'CORE_DOCUMENT_DESC', 'CORE_ID_ASC', 'CORE_ID_DESC', 'DEPUBLISHED_AT_ASC', 'DEPUBLISHED_AT_DESC', 'EDITORIAL_CATEGORY_ID_ASC', 'EDITORIAL_CATEGORY_ID_DESC', 'EPISODE_NUMBER_ASC', 'EPISODE_NUMBER_DESC', 'EXTERNAL_IDS_ASC', 'EXTERNAL_IDS_DESC', 'EXTERNAL_ID_ASC', 'EXTERNAL_ID_DESC', 'FEED_DOCUMENT_ASC', 'FEED_DOCUMENT_DESC', 'FEED_DOCUMENT_MODIFIED_AT_ASC',
                   'FEED_DOCUMENT_MODIFIED_AT_DESC', 'FIRST_PUBLISH_DATE_ASC', 'FIRST_PUBLISH_DATE_DESC', 'GROUP_ID_ASC', 'GROUP_ID_DESC', 'ID_ASC', 'ID_DESC', 'IMAGE_ASC', 'IMAGE_COLLECTION_ID_ASC', 'IMAGE_COLLECTION_ID_DESC', 'IMAGE_DESC', 'IS_PUBLISHED_ASC', 'IS_PUBLISHED_DESC', 'ITEM_TYPE_ASC', 'ITEM_TYPE_DESC', 'MAX_GROUP_NUMBER_ASC', 'MAX_GROUP_NUMBER_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROGRAM_SET_ID_ASC', 'PROGRAM_SET_ID_DESC', 'PUBLISH_DATE_ASC', 'PUBLISH_DATE_DESC', 'SHOW_ID_ASC', 'SHOW_ID_DESC', 'STATUS_ASC', 'STATUS_DESC', 'TITLE_ASC', 'TITLE_DESC', 'TITLE_WITHOUT_NUMBER_ASC', 'TITLE_WITHOUT_NUMBER_DESC')


class JSON(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class MigrationsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('EXECUTED_AT_ASC', 'EXECUTED_AT_DESC', 'HASH_ASC', 'HASH_DESC', 'ID_ASC',
                   'ID_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class OrganizationsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CORE_DOCUMENT_ASC', 'CORE_DOCUMENT_DESC', 'CORE_ID_ASC', 'CORE_ID_DESC', 'ID_ASC', 'ID_DESC', 'NAME_ASC',
                   'NAME_DESC', 'NATURAL', 'ORDER_ASC', 'ORDER_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'TITLE_ASC', 'TITLE_DESC')


class PermanentLivestreamsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('AUDIOS_ASC', 'AUDIOS_DESC', 'AUDIO_BINARY_ID_ASC', 'AUDIO_BINARY_ID_DESC', 'CORE_DOCUMENT_ASC', 'CORE_DOCUMENT_DESC', 'CORE_ID_ASC', 'CORE_ID_DESC', 'EXTERNAL_IDS_ASC', 'EXTERNAL_IDS_DESC', 'ID_ASC', 'ID_DESC', 'IMAGE_ASC', 'IMAGE_COLLECTION_ID_ASC', 'IMAGE_COLLECTION_ID_DESC',
                   'IMAGE_DESC', 'NATURAL', 'ORDER_ASC', 'ORDER_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PUBLICATION_SERVICE_ID_ASC', 'PUBLICATION_SERVICE_ID_DESC', 'PUBLISHER_CORE_ID_ASC', 'PUBLISHER_CORE_ID_DESC', 'STREAM_ASC', 'STREAM_DESC', 'TITLE_ASC', 'TITLE_DESC', 'TRACKING_ASC', 'TRACKING_DESC')


class PlaylistSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'ENTRIES_ID_ASC', 'ENTRIES_ID_DESC', 'MODIFIEDAT_ASC',
                   'MODIFIEDAT_DESC', 'PRIVATE_ASC', 'PRIVATE_DESC', 'SORTINDEX_ASC', 'SORTINDEX_DESC', 'TITLE_ASC', 'TITLE_DESC')


class ProgramSetSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('ID_ASC', 'ID_DESC')


class ProgramSetSubscriptionSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'LASTVISITEDAT_ASC', 'LASTVISITEDAT_DESC', 'MODIFIEDAT_ASC',
                   'MODIFIEDAT_DESC', 'SUBSCRIBEDAT_ASC', 'SUBSCRIBEDAT_DESC', 'SUBSCRIBEDPROGRAMSET_ID_ASC', 'SUBSCRIBEDPROGRAMSET_ID_DESC')


class ProgramSetsOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CORE_DOCUMENT_ASC', 'CORE_DOCUMENT_DESC', 'CORE_ID_ASC', 'CORE_ID_DESC', 'EDITORIAL_CATEGORY_ID_ASC', 'EDITORIAL_CATEGORY_ID_DESC', 'ID_ASC', 'ID_DESC', 'IMAGE_ASC', 'IMAGE_COLLECTION_ID_ASC', 'IMAGE_COLLECTION_ID_DESC', 'IMAGE_DESC', 'LAST_ITEM_ADDED_ASC', 'LAST_ITEM_ADDED_DESC',
                   'LAST_ITEM_MODIFIED_ASC', 'LAST_ITEM_MODIFIED_DESC', 'NATURAL', 'NUMBER_OF_ELEMENTS_ASC', 'NUMBER_OF_ELEMENTS_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PUBLICATION_SERVICE_ID_ASC', 'PUBLICATION_SERVICE_ID_DESC', 'SYNOPSIS_ASC', 'SYNOPSIS_DESC', 'TITLE_ASC', 'TITLE_DESC')


class PropertySortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'KEY_ASC', 'KEY_DESC',
                   'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC', 'VALUE_ASC', 'VALUE_DESC')


class PublicationServicesOrderBy(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('BRANDING_COLOR_ASC', 'BRANDING_COLOR_DESC', 'CORE_DOCUMENT_ASC', 'CORE_DOCUMENT_DESC', 'CORE_ID_ASC', 'CORE_ID_DESC', 'DVB_SERVICE_ID_ASC', 'DVB_SERVICE_ID_DESC', 'EXTERNAL_IDS_ASC', 'EXTERNAL_IDS_DESC', 'GENRE_ASC', 'GENRE_DESC', 'HOMEPAGE_URL_ASC', 'HOMEPAGE_URL_DESC', 'ID_ASC', 'ID_DESC', 'IMAGE_ASC',
                   'IMAGE_DESC', 'NATURAL', 'NUMBER_OF_ELEMENTS_ASC', 'NUMBER_OF_ELEMENTS_DESC', 'ORDER_ASC', 'ORDER_DESC', 'ORGANIZATION_NAME_ASC', 'ORGANIZATION_NAME_DESC', 'PARENT_SERVICE_ID_ASC', 'PARENT_SERVICE_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SYNOPSIS_ASC', 'SYNOPSIS_DESC', 'TITLE_ASC', 'TITLE_DESC')


class PublishableThingSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'MODIFIEDAT_ASC',
                   'MODIFIEDAT_DESC', 'NOINDEX_ASC', 'NOINDEX_DESC')


class QueueSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'ENTRIES_ID_ASC',
                   'ENTRIES_ID_DESC', 'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC')


class SearchType(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('All', 'EditorialCategories',
                   'EditorialCollections', 'Items', 'ProgramSets')


class ShowType(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('FINITE_SERIES', 'INFINITE_SERIES',
                   'SEASON_SERIES', 'SINGLE')


class SourceSystem(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('Core', 'Hybrid', 'Postgres')


class Status(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('DELETED', 'DEPUBLISHED', 'INCOMPLETE', 'OBSOLETE',
                   'PUBLISHED', 'SCHEDULED', 'SPECIAL', 'SUPERSEDED')


String = sgqlc.types.String


class SubscriptionListSortOrder(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('CREATEDAT_ASC', 'CREATEDAT_DESC', 'MODIFIEDAT_ASC', 'MODIFIEDAT_DESC', 'PROGRAMSETS_CREATEDAT_ASC', 'PROGRAMSETS_CREATEDAT_DESC', 'PROGRAMSETS_LASTVISITEDAT_ASC', 'PROGRAMSETS_LASTVISITEDAT_DESC',
                   'PROGRAMSETS_MODIFIEDAT_ASC', 'PROGRAMSETS_MODIFIEDAT_DESC', 'PROGRAMSETS_SUBSCRIBEDAT_ASC', 'PROGRAMSETS_SUBSCRIBEDAT_DESC', 'PROGRAMSETS_SUBSCRIBEDPROGRAMSET_ID_ASC', 'PROGRAMSETS_SUBSCRIBEDPROGRAMSET_ID_DESC')


class TeaserTypeATG(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('EditorialCategory', 'EditorialCollection',
                   'EventLivestream', 'Item', 'ProgramSet', 'SophoraTeaser')


class URI(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class URL(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class UrlVariant(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('API', 'SHARING', 'WEB')


class WidgetDisplayVariant(sgqlc.types.Enum):
    __schema__ = audiothek_schema
    __choices__ = ('COLLAPSIBLE_GRID', 'DEFAULT', 'GRID', 'SLIDER')


class _Any(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


class _FieldSet(sgqlc.types.Scalar):
    __schema__ = audiothek_schema


########################################################################
# Input Objects
########################################################################
class BigIntFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(BigInt, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(BigInt, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(BigInt, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        BigInt, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(BigInt)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(BigInt)), graphql_name='notIn')
    less_than = sgqlc.types.Field(BigInt, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        BigInt, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(BigInt, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        BigInt, graphql_name='greaterThanOrEqualTo')


class BigIntFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_', 'gt', 'gte', 'lt', 'lte')
    eq = sgqlc.types.Field(BigInt, graphql_name='eq')
    ne = sgqlc.types.Field(BigInt, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(BigInt), graphql_name='in')
    gt = sgqlc.types.Field(BigInt, graphql_name='gt')
    gte = sgqlc.types.Field(BigInt, graphql_name='gte')
    lt = sgqlc.types.Field(BigInt, graphql_name='lt')
    lte = sgqlc.types.Field(BigInt, graphql_name='lte')


class BookmarkConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('bookmarked_at', 'created_at', 'modified_at', 'empty')
    bookmarked_at = sgqlc.types.Field(
        'DateFilterB', graphql_name='bookmarkedAt')
    created_at = sgqlc.types.Field('DateFilterB', graphql_name='createdAt')
    modified_at = sgqlc.types.Field('DateFilterB', graphql_name='modifiedAt')
    empty = sgqlc.types.Field('BooleanFilterB', graphql_name='empty')


class BookmarkCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('type', 'bookmarked_at', 'item')
    type = sgqlc.types.Field(String, graphql_name='type')
    bookmarked_at = sgqlc.types.Field(DateTime, graphql_name='bookmarkedAt')
    item = sgqlc.types.Field(sgqlc.types.non_null(
        'ItemCreateInput'), graphql_name='item')


class BookmarkFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('bookmarked_at', 'created_at', 'modified_at')
    bookmarked_at = sgqlc.types.Field(
        'DateFilterB', graphql_name='bookmarkedAt')
    created_at = sgqlc.types.Field('DateFilterB', graphql_name='createdAt')
    modified_at = sgqlc.types.Field('DateFilterB', graphql_name='modifiedAt')


class BookmarkListConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field('BooleanFilterB', graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class BookmarkListCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type', 'entries')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    entries = sgqlc.types.Field(sgqlc.types.non_null(
        sgqlc.types.list_of(BookmarkCreateInput)), graphql_name='entries')


class BookmarkListEntryListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'entry', 'bookmark_list')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    entry = sgqlc.types.Field(sgqlc.types.non_null(
        BookmarkCreateInput), graphql_name='entry')
    bookmark_list = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='bookmarkList')


class BookmarkListFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'entries', 'modified_at', 'user')
    created_at = sgqlc.types.Field('DateFilterB', graphql_name='createdAt')
    entries = sgqlc.types.Field(
        BookmarkConnectionFilterB, graphql_name='entries')
    modified_at = sgqlc.types.Field('DateFilterB', graphql_name='modifiedAt')
    user = sgqlc.types.Field('EndUserRelationFilterB', graphql_name='user')


class BookmarkListRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field('IDFilterB', graphql_name='id')
    exists = sgqlc.types.Field('BooleanFilterB', graphql_name='exists')


class BookmarkListRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'bookmark_list')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    bookmark_list = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='bookmarkList')


class BookmarkListUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'entries')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    entries = sgqlc.types.Field(sgqlc.types.list_of(
        BookmarkCreateInput), graphql_name='entries')


class BookmarkRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('bookmarked_at', 'created_at', 'modified_at')
    bookmarked_at = sgqlc.types.Field(
        'DateFilterB', graphql_name='bookmarkedAt')
    created_at = sgqlc.types.Field('DateFilterB', graphql_name='createdAt')
    modified_at = sgqlc.types.Field('DateFilterB', graphql_name='modifiedAt')


class BookmarkRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'bookmark')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    bookmark = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='bookmark')


class BookmarkUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'bookmarked_at', 'item')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    bookmarked_at = sgqlc.types.Field(DateTime, graphql_name='bookmarkedAt')
    item = sgqlc.types.Field('ItemCreateInput', graphql_name='item')


class BooleanFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(Boolean, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(Boolean, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(Boolean, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        Boolean, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Boolean)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Boolean)), graphql_name='notIn')
    less_than = sgqlc.types.Field(Boolean, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        Boolean, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Boolean, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        Boolean, graphql_name='greaterThanOrEqualTo')


class BooleanFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne')
    eq = sgqlc.types.Field(Boolean, graphql_name='eq')
    ne = sgqlc.types.Field(Boolean, graphql_name='ne')


class CategoriesToProgramSetCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('program_set_core_id', 'category_sophora_id')
    program_set_core_id = sgqlc.types.Field(
        String, graphql_name='programSetCoreId')
    category_sophora_id = sgqlc.types.Field(
        String, graphql_name='categorySophoraId')


class CategoriesToProgramSetFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('program_set_core_id',
                       'category_sophora_id', 'and_', 'or_', 'not_')
    program_set_core_id = sgqlc.types.Field(
        'StringFilter', graphql_name='programSetCoreId')
    category_sophora_id = sgqlc.types.Field(
        'StringFilter', graphql_name='categorySophoraId')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(
        'CategoriesToProgramSetFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(
        'CategoriesToProgramSetFilter')), graphql_name='or')
    not_ = sgqlc.types.Field(
        'CategoriesToProgramSetFilter', graphql_name='not')


class ConceptCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('item_id', 'concept_source', 'data', 'last_updated_at')
    item_id = sgqlc.types.Field(Int, graphql_name='itemId')
    concept_source = sgqlc.types.Field(String, graphql_name='conceptSource')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    last_updated_at = sgqlc.types.Field(Datetime, graphql_name='lastUpdatedAt')


class ConceptFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('item_id', 'concept_source', 'data',
                       'last_updated_at', 'and_', 'or_', 'not_')
    item_id = sgqlc.types.Field('IntFilter', graphql_name='itemId')
    concept_source = sgqlc.types.Field(
        'StringFilter', graphql_name='conceptSource')
    data = sgqlc.types.Field('JSONFilter', graphql_name='data')
    last_updated_at = sgqlc.types.Field(
        'DatetimeFilter', graphql_name='lastUpdatedAt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ConceptFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ConceptFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('ConceptFilter', graphql_name='not')


class ConfigCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('key', 'value', 'updated_at', 'updated_by')
    key = sgqlc.types.Field(String, graphql_name='key')
    value = sgqlc.types.Field(JSON, graphql_name='value')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    updated_by = sgqlc.types.Field(String, graphql_name='updatedBy')


class ConfigFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('key', 'value', 'updated_at',
                       'updated_by', 'and_', 'or_', 'not_')
    key = sgqlc.types.Field('StringFilter', graphql_name='key')
    value = sgqlc.types.Field('JSONFilter', graphql_name='value')
    updated_at = sgqlc.types.Field('DatetimeFilter', graphql_name='updatedAt')
    updated_by = sgqlc.types.Field('StringFilter', graphql_name='updatedBy')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ConfigFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ConfigFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('ConfigFilter', graphql_name='not')


class DateFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_', 'gt', 'gte', 'lt', 'lte')
    eq = sgqlc.types.Field(DateTime, graphql_name='eq')
    ne = sgqlc.types.Field(DateTime, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='in')
    gt = sgqlc.types.Field(DateTime, graphql_name='gt')
    gte = sgqlc.types.Field(DateTime, graphql_name='gte')
    lt = sgqlc.types.Field(DateTime, graphql_name='lt')
    lte = sgqlc.types.Field(DateTime, graphql_name='lte')


class DatetimeFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(Datetime, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(Datetime, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(Datetime, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        Datetime, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Datetime)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Datetime)), graphql_name='notIn')
    less_than = sgqlc.types.Field(Datetime, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        Datetime, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Datetime, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        Datetime, graphql_name='greaterThanOrEqualTo')


class DeleteHistoryEntryByItemInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'item')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    item = sgqlc.types.Field(sgqlc.types.non_null(
        'ItemCreateInput'), graphql_name='item')


class DeleteInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DepublishExpiredItemsInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')


class EditorialCategoryCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'title', 'image', 'sophora_id', 'order')
    id = sgqlc.types.Field(String, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field('ImageTypeInput', graphql_name='image')
    sophora_id = sgqlc.types.Field(String, graphql_name='sophoraId')
    order = sgqlc.types.Field(Int, graphql_name='order')


class EditorialCategoryFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'title', 'sophora_id', 'order',
                       'image', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field('StringFilter', graphql_name='id')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    sophora_id = sgqlc.types.Field('StringFilter', graphql_name='sophoraId')
    order = sgqlc.types.Field('IntFilter', graphql_name='order')
    image = sgqlc.types.Field('ImageTypeFilter', graphql_name='image')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCategoryFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCategoryFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('EditorialCategoryFilter', graphql_name='not')


class EditorialCollectionCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('sophora_id', 'title', 'image', 'broadcast_duration',
                       'number_of_elements', 'synopsis', 'coremedia_id')
    sophora_id = sgqlc.types.Field(String, graphql_name='sophoraId')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field('ImageTypeInput', graphql_name='image')
    broadcast_duration = sgqlc.types.Field(
        Int, graphql_name='broadcastDuration')
    number_of_elements = sgqlc.types.Field(
        Int, graphql_name='numberOfElements')
    synopsis = sgqlc.types.Field(String, graphql_name='synopsis')
    coremedia_id = sgqlc.types.Field(String, graphql_name='coremediaId')


class EditorialCollectionFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('sophora_id', 'title', 'broadcast_duration', 'number_of_elements',
                       'synopsis', 'coremedia_id', 'image', 'and_', 'or_', 'not_')
    sophora_id = sgqlc.types.Field('StringFilter', graphql_name='sophoraId')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    broadcast_duration = sgqlc.types.Field(
        'IntFilter', graphql_name='broadcastDuration')
    number_of_elements = sgqlc.types.Field(
        'IntFilter', graphql_name='numberOfElements')
    synopsis = sgqlc.types.Field('StringFilter', graphql_name='synopsis')
    coremedia_id = sgqlc.types.Field(
        'StringFilter', graphql_name='coremediaId')
    image = sgqlc.types.Field('ImageTypeFilter', graphql_name='image')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCollectionFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCollectionFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('EditorialCollectionFilter', graphql_name='not')


class EndUserConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class EndUserCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type',
                       'local_id', 'login_id', 'sync_successful')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    local_id = sgqlc.types.Field(String, graphql_name='localId')
    login_id = sgqlc.types.Field(String, graphql_name='loginId')
    sync_successful = sgqlc.types.Field(Boolean, graphql_name='syncSuccessful')


class EndUserFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'local_id', 'login_id',
                       'modified_at', 'sync_successful')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    local_id = sgqlc.types.Field('StringFilterB', graphql_name='localId')
    login_id = sgqlc.types.Field('StringFilterB', graphql_name='loginId')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    sync_successful = sgqlc.types.Field(
        BooleanFilterB, graphql_name='syncSuccessful')


class EndUserRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field('IDFilterB', graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class EndUserRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'end_user')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    end_user = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='endUser')


class EndUserSyncInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('user', 'bookmarks', 'playlists', 'queued_items',
                       'program_set_subscriptions', 'history_entries')
    user = sgqlc.types.Field(sgqlc.types.non_null(
        EndUserCreateInput), graphql_name='user')
    bookmarks = sgqlc.types.Field(sgqlc.types.list_of(
        BookmarkCreateInput), graphql_name='bookmarks')
    playlists = sgqlc.types.Field(sgqlc.types.list_of(
        'PlaylistCreateInput'), graphql_name='playlists')
    queued_items = sgqlc.types.Field(sgqlc.types.list_of(
        'ItemCreateInput'), graphql_name='queuedItems')
    program_set_subscriptions = sgqlc.types.Field(sgqlc.types.list_of(
        'ProgramSetSubscriptionCreateInput'), graphql_name='programSetSubscriptions')
    history_entries = sgqlc.types.Field(sgqlc.types.list_of(
        'HistoryEntryCreateInput'), graphql_name='historyEntries')


class EndUserUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id',
                       'local_id', 'login_id', 'sync_successful')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    local_id = sgqlc.types.Field(String, graphql_name='localId')
    login_id = sgqlc.types.Field(String, graphql_name='loginId')
    sync_successful = sgqlc.types.Field(Boolean, graphql_name='syncSuccessful')


class FloatFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_', 'gt', 'gte', 'lt', 'lte')
    eq = sgqlc.types.Field(Float, graphql_name='eq')
    ne = sgqlc.types.Field(Float, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='in')
    gt = sgqlc.types.Field(Float, graphql_name='gt')
    gte = sgqlc.types.Field(Float, graphql_name='gte')
    lt = sgqlc.types.Field(Float, graphql_name='lt')
    lte = sgqlc.types.Field(Float, graphql_name='lte')


class GroupingCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'programset_id', 'title', 'item_label', 'type', 'count',
                       'season_number', 'last_modified', 'core_id', 'core_document', 'show_id')
    id = sgqlc.types.Field(String, graphql_name='id')
    programset_id = sgqlc.types.Field(Int, graphql_name='programsetId')
    title = sgqlc.types.Field(String, graphql_name='title')
    item_label = sgqlc.types.Field(String, graphql_name='itemLabel')
    type = sgqlc.types.Field(Grouptype, graphql_name='type')
    count = sgqlc.types.Field(Int, graphql_name='count')
    season_number = sgqlc.types.Field(Int, graphql_name='seasonNumber')
    last_modified = sgqlc.types.Field(Datetime, graphql_name='lastModified')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    show_id = sgqlc.types.Field(String, graphql_name='showId')


class GroupingFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'programset_id', 'title', 'item_label', 'type', 'count', 'season_number',
                       'last_modified', 'core_id', 'core_document', 'show_id', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field('StringFilter', graphql_name='id')
    programset_id = sgqlc.types.Field('IntFilter', graphql_name='programsetId')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    item_label = sgqlc.types.Field('StringFilter', graphql_name='itemLabel')
    type = sgqlc.types.Field('GrouptypeFilter', graphql_name='type')
    count = sgqlc.types.Field('IntFilter', graphql_name='count')
    season_number = sgqlc.types.Field('IntFilter', graphql_name='seasonNumber')
    last_modified = sgqlc.types.Field(
        DatetimeFilter, graphql_name='lastModified')
    core_id = sgqlc.types.Field('StringFilter', graphql_name='coreId')
    core_document = sgqlc.types.Field(
        'JSONFilter', graphql_name='coreDocument')
    show_id = sgqlc.types.Field('StringFilter', graphql_name='showId')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('GroupingFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('GroupingFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('GroupingFilter', graphql_name='not')


class GrouptypeFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(Grouptype, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(Grouptype, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(Grouptype, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        Grouptype, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Grouptype)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Grouptype)), graphql_name='notIn')
    less_than = sgqlc.types.Field(Grouptype, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        Grouptype, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Grouptype, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        Grouptype, graphql_name='greaterThanOrEqualTo')


class HistoryEntryConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class HistoryEntryCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type', 'item',
                       'last_listened_at', 'progress')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    item = sgqlc.types.Field(sgqlc.types.non_null(
        'ItemCreateInput'), graphql_name='item')
    last_listened_at = sgqlc.types.Field(
        DateTime, graphql_name='lastListenedAt')
    progress = sgqlc.types.Field(Float, graphql_name='progress')


class HistoryEntryFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'last_listened_at',
                       'modified_at', 'progress', 'user')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    last_listened_at = sgqlc.types.Field(
        DateFilterB, graphql_name='lastListenedAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    progress = sgqlc.types.Field(FloatFilterB, graphql_name='progress')
    user = sgqlc.types.Field(EndUserRelationFilterB, graphql_name='user')


class HistoryEntryRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field('IDFilterB', graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class HistoryEntryRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'history_entry')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    history_entry = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='historyEntry')


class HistoryEntryUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'item',
                       'last_listened_at', 'progress')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    item = sgqlc.types.Field('ItemCreateInput', graphql_name='item')
    last_listened_at = sgqlc.types.Field(
        DateTime, graphql_name='lastListenedAt')
    progress = sgqlc.types.Field(Float, graphql_name='progress')


class IDFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_')
    eq = sgqlc.types.Field(ID, graphql_name='eq')
    ne = sgqlc.types.Field(ID, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')


class ImageTypeFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('url', 'url1_x1', 'description',
                       'attribution', 'and_', 'or_', 'not_')
    url = sgqlc.types.Field('StringFilter', graphql_name='url')
    url1_x1 = sgqlc.types.Field('StringFilter', graphql_name='url1X1')
    description = sgqlc.types.Field('StringFilter', graphql_name='description')
    attribution = sgqlc.types.Field('StringFilter', graphql_name='attribution')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ImageTypeFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ImageTypeFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('ImageTypeFilter', graphql_name='not')


class ImageTypeInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('url', 'url1_x1', 'description', 'attribution')
    url = sgqlc.types.Field(String, graphql_name='url')
    url1_x1 = sgqlc.types.Field(String, graphql_name='url1X1')
    description = sgqlc.types.Field(String, graphql_name='description')
    attribution = sgqlc.types.Field(String, graphql_name='attribution')


class ImagesCollectionsBinariesViewCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('image_collection_id', 'image_id', 'title', 'producer_name',
                       'image_binary_id', 'aspect_ratio', 'height', 'width', 'media_type', 'file_location')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    image_id = sgqlc.types.Field(String, graphql_name='imageId')
    title = sgqlc.types.Field(String, graphql_name='title')
    producer_name = sgqlc.types.Field(String, graphql_name='producerName')
    image_binary_id = sgqlc.types.Field(String, graphql_name='imageBinaryId')
    aspect_ratio = sgqlc.types.Field(String, graphql_name='aspectRatio')
    height = sgqlc.types.Field(Int, graphql_name='height')
    width = sgqlc.types.Field(Int, graphql_name='width')
    media_type = sgqlc.types.Field(String, graphql_name='mediaType')
    file_location = sgqlc.types.Field(String, graphql_name='fileLocation')


class ImagesCollectionsBinariesViewFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('image_collection_id', 'image_id', 'title', 'producer_name', 'image_binary_id',
                       'aspect_ratio', 'height', 'width', 'media_type', 'file_location', 'and_', 'or_', 'not_')
    image_collection_id = sgqlc.types.Field(
        'StringFilter', graphql_name='imageCollectionId')
    image_id = sgqlc.types.Field('StringFilter', graphql_name='imageId')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    producer_name = sgqlc.types.Field(
        'StringFilter', graphql_name='producerName')
    image_binary_id = sgqlc.types.Field(
        'StringFilter', graphql_name='imageBinaryId')
    aspect_ratio = sgqlc.types.Field(
        'StringFilter', graphql_name='aspectRatio')
    height = sgqlc.types.Field('IntFilter', graphql_name='height')
    width = sgqlc.types.Field('IntFilter', graphql_name='width')
    media_type = sgqlc.types.Field('StringFilter', graphql_name='mediaType')
    file_location = sgqlc.types.Field(
        'StringFilter', graphql_name='fileLocation')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(
        'ImagesCollectionsBinariesViewFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(
        'ImagesCollectionsBinariesViewFilter')), graphql_name='or')
    not_ = sgqlc.types.Field(
        'ImagesCollectionsBinariesViewFilter', graphql_name='not')


class IntFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(Int, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(Int, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(Int, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(Int, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Int)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Int)), graphql_name='notIn')
    less_than = sgqlc.types.Field(Int, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        Int, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Int, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        Int, graphql_name='greaterThanOrEqualTo')


class IntFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_', 'gt', 'gte', 'lt', 'lte')
    eq = sgqlc.types.Field(Int, graphql_name='eq')
    ne = sgqlc.types.Field(Int, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='in')
    gt = sgqlc.types.Field(Int, graphql_name='gt')
    gte = sgqlc.types.Field(Int, graphql_name='gte')
    lt = sgqlc.types.Field(Int, graphql_name='lt')
    lte = sgqlc.types.Field(Int, graphql_name='lte')


class ItemCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'backend_document_hash', 'backend_document', 'publish_date', 'codex_pending', 'feed_document', 'feed_document_modified_at', 'is_published', 'depublished_at', 'program_set_id', 'title', 'title_without_number', 'group_id',
                       'episode_number', 'max_group_number', 'codex_last_published', 'external_ids', 'image', 'editorial_category_id', 'core_id', 'item_type', 'core_document', 'external_id', 'image_collection_id', 'show_id', 'first_publish_date', 'audio_binary_id', 'status')
    id = sgqlc.types.Field(Int, graphql_name='id')
    backend_document_hash = sgqlc.types.Field(
        String, graphql_name='backendDocumentHash')
    backend_document = sgqlc.types.Field(JSON, graphql_name='backendDocument')
    publish_date = sgqlc.types.Field(Datetime, graphql_name='publishDate')
    codex_pending = sgqlc.types.Field(Boolean, graphql_name='codexPending')
    feed_document = sgqlc.types.Field(JSON, graphql_name='feedDocument')
    feed_document_modified_at = sgqlc.types.Field(
        BigInt, graphql_name='feedDocumentModifiedAt')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    depublished_at = sgqlc.types.Field(BigInt, graphql_name='depublishedAt')
    program_set_id = sgqlc.types.Field(Int, graphql_name='programSetId')
    title = sgqlc.types.Field(String, graphql_name='title')
    title_without_number = sgqlc.types.Field(
        String, graphql_name='titleWithoutNumber')
    group_id = sgqlc.types.Field(String, graphql_name='groupId')
    episode_number = sgqlc.types.Field(Int, graphql_name='episodeNumber')
    max_group_number = sgqlc.types.Field(Int, graphql_name='maxGroupNumber')
    codex_last_published = sgqlc.types.Field(
        BigInt, graphql_name='codexLastPublished')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    image = sgqlc.types.Field(ImageTypeInput, graphql_name='image')
    editorial_category_id = sgqlc.types.Field(
        String, graphql_name='editorialCategoryId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    item_type = sgqlc.types.Field(ItemType, graphql_name='itemType')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    show_id = sgqlc.types.Field(String, graphql_name='showId')
    first_publish_date = sgqlc.types.Field(
        Datetime, graphql_name='firstPublishDate')
    audio_binary_id = sgqlc.types.Field(String, graphql_name='audioBinaryId')
    status = sgqlc.types.Field(Status, graphql_name='status')


class ItemConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'empty')
    id = sgqlc.types.Field(IntFilterB, graphql_name='id')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')


class ItemCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('type', 'id')
    type = sgqlc.types.Field(String, graphql_name='type')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ItemFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'backend_document_hash', 'backend_document', 'publish_date', 'codex_pending', 'feed_document', 'feed_document_modified_at', 'is_published', 'depublished_at', 'program_set_id', 'title', 'title_without_number', 'group_id', 'episode_number',
                       'max_group_number', 'codex_last_published', 'external_ids', 'editorial_category_id', 'core_id', 'item_type', 'core_document', 'external_id', 'image_collection_id', 'show_id', 'first_publish_date', 'audio_binary_id', 'status', 'image', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field(IntFilter, graphql_name='id')
    backend_document_hash = sgqlc.types.Field(
        'StringFilter', graphql_name='backendDocumentHash')
    backend_document = sgqlc.types.Field(
        'JSONFilter', graphql_name='backendDocument')
    publish_date = sgqlc.types.Field(
        DatetimeFilter, graphql_name='publishDate')
    codex_pending = sgqlc.types.Field(
        BooleanFilter, graphql_name='codexPending')
    feed_document = sgqlc.types.Field(
        'JSONFilter', graphql_name='feedDocument')
    feed_document_modified_at = sgqlc.types.Field(
        BigIntFilter, graphql_name='feedDocumentModifiedAt')
    is_published = sgqlc.types.Field(BooleanFilter, graphql_name='isPublished')
    depublished_at = sgqlc.types.Field(
        BigIntFilter, graphql_name='depublishedAt')
    program_set_id = sgqlc.types.Field(IntFilter, graphql_name='programSetId')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    title_without_number = sgqlc.types.Field(
        'StringFilter', graphql_name='titleWithoutNumber')
    group_id = sgqlc.types.Field('StringFilter', graphql_name='groupId')
    episode_number = sgqlc.types.Field(IntFilter, graphql_name='episodeNumber')
    max_group_number = sgqlc.types.Field(
        IntFilter, graphql_name='maxGroupNumber')
    codex_last_published = sgqlc.types.Field(
        BigIntFilter, graphql_name='codexLastPublished')
    external_ids = sgqlc.types.Field(
        'StringListFilter', graphql_name='externalIds')
    editorial_category_id = sgqlc.types.Field(
        'StringFilter', graphql_name='editorialCategoryId')
    core_id = sgqlc.types.Field('StringFilter', graphql_name='coreId')
    item_type = sgqlc.types.Field('ItemTypeFilter', graphql_name='itemType')
    core_document = sgqlc.types.Field(
        'JSONFilter', graphql_name='coreDocument')
    external_id = sgqlc.types.Field('StringFilter', graphql_name='externalId')
    image_collection_id = sgqlc.types.Field(
        'StringFilter', graphql_name='imageCollectionId')
    show_id = sgqlc.types.Field('StringFilter', graphql_name='showId')
    first_publish_date = sgqlc.types.Field(
        DatetimeFilter, graphql_name='firstPublishDate')
    audio_binary_id = sgqlc.types.Field(
        'StringFilter', graphql_name='audioBinaryId')
    status = sgqlc.types.Field('StatusFilter', graphql_name='status')
    image = sgqlc.types.Field(ImageTypeFilter, graphql_name='image')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ItemFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ItemFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('ItemFilter', graphql_name='not')


class ItemFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(IntFilterB, graphql_name='id')


class ItemRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(IntFilterB, graphql_name='id')


class ItemTypeFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(ItemType, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(ItemType, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(ItemType, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        ItemType, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(ItemType)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(ItemType)), graphql_name='notIn')
    less_than = sgqlc.types.Field(ItemType, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        ItemType, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(ItemType, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        ItemType, graphql_name='greaterThanOrEqualTo')


class JSONFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from', 'in_', 'not_in', 'less_than', 'less_than_or_equal_to',
                       'greater_than', 'greater_than_or_equal_to', 'contains', 'contains_key', 'contains_all_keys', 'contains_any_keys', 'contained_by')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(JSON, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(JSON, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(JSON, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(JSON, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(JSON)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(JSON)), graphql_name='notIn')
    less_than = sgqlc.types.Field(JSON, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        JSON, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(JSON, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        JSON, graphql_name='greaterThanOrEqualTo')
    contains = sgqlc.types.Field(JSON, graphql_name='contains')
    contains_key = sgqlc.types.Field(String, graphql_name='containsKey')
    contains_all_keys = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(String)), graphql_name='containsAllKeys')
    contains_any_keys = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(String)), graphql_name='containsAnyKeys')
    contained_by = sgqlc.types.Field(JSON, graphql_name='containedBy')


class MigrationCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'name', 'hash', 'executed_at')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    executed_at = sgqlc.types.Field(Datetime, graphql_name='executedAt')


class MigrationFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'name', 'hash', 'executed_at',
                       'and_', 'or_', 'not_')
    id = sgqlc.types.Field(IntFilter, graphql_name='id')
    name = sgqlc.types.Field('StringFilter', graphql_name='name')
    hash = sgqlc.types.Field('StringFilter', graphql_name='hash')
    executed_at = sgqlc.types.Field(DatetimeFilter, graphql_name='executedAt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('MigrationFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('MigrationFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('MigrationFilter', graphql_name='not')


class OrganizationCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'name', 'core_id',
                       'core_document', 'order', 'title')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    order = sgqlc.types.Field(Int, graphql_name='order')
    title = sgqlc.types.Field(String, graphql_name='title')


class OrganizationFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'name', 'core_id', 'core_document',
                       'order', 'title', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field(IntFilter, graphql_name='id')
    name = sgqlc.types.Field('StringFilter', graphql_name='name')
    core_id = sgqlc.types.Field('StringFilter', graphql_name='coreId')
    core_document = sgqlc.types.Field(JSONFilter, graphql_name='coreDocument')
    order = sgqlc.types.Field(IntFilter, graphql_name='order')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('OrganizationFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('OrganizationFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('OrganizationFilter', graphql_name='not')


class PermanentLivestreamCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'core_id', 'external_ids', 'publication_service_id', 'title', 'image', 'core_document',
                       'stream', 'tracking', 'audios', 'image_collection_id', 'audio_binary_id', 'publisher_core_id', 'order')
    id = sgqlc.types.Field(String, graphql_name='id')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    publication_service_id = sgqlc.types.Field(
        Int, graphql_name='publicationServiceId')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field(ImageTypeInput, graphql_name='image')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    stream = sgqlc.types.Field(JSON, graphql_name='stream')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')
    audios = sgqlc.types.Field(sgqlc.types.list_of(
        'StreamTypeInput'), graphql_name='audios')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    audio_binary_id = sgqlc.types.Field(String, graphql_name='audioBinaryId')
    publisher_core_id = sgqlc.types.Field(
        String, graphql_name='publisherCoreId')
    order = sgqlc.types.Field(Int, graphql_name='order')


class PermanentLivestreamFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'core_id', 'external_ids', 'publication_service_id', 'title', 'core_document', 'stream',
                       'tracking', 'image_collection_id', 'audio_binary_id', 'publisher_core_id', 'order', 'image', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field('StringFilter', graphql_name='id')
    core_id = sgqlc.types.Field('StringFilter', graphql_name='coreId')
    external_ids = sgqlc.types.Field(
        'StringListFilter', graphql_name='externalIds')
    publication_service_id = sgqlc.types.Field(
        IntFilter, graphql_name='publicationServiceId')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    core_document = sgqlc.types.Field(JSONFilter, graphql_name='coreDocument')
    stream = sgqlc.types.Field(JSONFilter, graphql_name='stream')
    tracking = sgqlc.types.Field(JSONFilter, graphql_name='tracking')
    image_collection_id = sgqlc.types.Field(
        'StringFilter', graphql_name='imageCollectionId')
    audio_binary_id = sgqlc.types.Field(
        'StringFilter', graphql_name='audioBinaryId')
    publisher_core_id = sgqlc.types.Field(
        'StringFilter', graphql_name='publisherCoreId')
    order = sgqlc.types.Field(IntFilter, graphql_name='order')
    image = sgqlc.types.Field(ImageTypeFilter, graphql_name='image')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('PermanentLivestreamFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('PermanentLivestreamFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('PermanentLivestreamFilter', graphql_name='not')


class PlaylistConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class PlaylistCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type',
                       'entries', 'private', 'sort_index', 'title')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    entries = sgqlc.types.Field(sgqlc.types.list_of(
        ItemCreateInput), graphql_name='entries')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    sort_index = sgqlc.types.Field(Int, graphql_name='sortIndex')
    title = sgqlc.types.Field(String, graphql_name='title')


class PlaylistEntryListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'entry', 'playlist')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    entry = sgqlc.types.Field(sgqlc.types.non_null(
        ItemCreateInput), graphql_name='entry')
    playlist = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='playlist')


class PlaylistFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'modified_at',
                       'private', 'sort_index', 'title', 'user')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    private = sgqlc.types.Field(BooleanFilterB, graphql_name='private')
    sort_index = sgqlc.types.Field(IntFilterB, graphql_name='sortIndex')
    title = sgqlc.types.Field('StringFilterB', graphql_name='title')
    user = sgqlc.types.Field(EndUserRelationFilterB, graphql_name='user')


class PlaylistRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field(IDFilterB, graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class PlaylistRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'playlist')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    playlist = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='playlist')


class PlaylistUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'entries',
                       'private', 'sort_index', 'title')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    entries = sgqlc.types.Field(sgqlc.types.list_of(
        ItemCreateInput), graphql_name='entries')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    sort_index = sgqlc.types.Field(Int, graphql_name='sortIndex')
    title = sgqlc.types.Field(String, graphql_name='title')


class ProgramSetCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'publication_service_id', 'title', 'synopsis', 'number_of_elements', 'image',
                       'editorial_category_id', 'core_id', 'core_document', 'image_collection_id', 'last_item_modified', 'last_item_added')
    id = sgqlc.types.Field(Int, graphql_name='id')
    publication_service_id = sgqlc.types.Field(
        Int, graphql_name='publicationServiceId')
    title = sgqlc.types.Field(String, graphql_name='title')
    synopsis = sgqlc.types.Field(String, graphql_name='synopsis')
    number_of_elements = sgqlc.types.Field(
        Int, graphql_name='numberOfElements')
    image = sgqlc.types.Field(ImageTypeInput, graphql_name='image')
    editorial_category_id = sgqlc.types.Field(
        String, graphql_name='editorialCategoryId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    last_item_modified = sgqlc.types.Field(
        Datetime, graphql_name='lastItemModified')
    last_item_added = sgqlc.types.Field(Datetime, graphql_name='lastItemAdded')


class ProgramSetConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'empty')
    id = sgqlc.types.Field(IntFilterB, graphql_name='id')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')


class ProgramSetCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('type', 'id')
    type = sgqlc.types.Field(String, graphql_name='type')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ProgramSetFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'publication_service_id', 'title', 'synopsis', 'number_of_elements', 'editorial_category_id',
                       'core_id', 'core_document', 'image_collection_id', 'last_item_modified', 'last_item_added', 'image', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field(IntFilter, graphql_name='id')
    publication_service_id = sgqlc.types.Field(
        IntFilter, graphql_name='publicationServiceId')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    synopsis = sgqlc.types.Field('StringFilter', graphql_name='synopsis')
    number_of_elements = sgqlc.types.Field(
        IntFilter, graphql_name='numberOfElements')
    editorial_category_id = sgqlc.types.Field(
        'StringFilter', graphql_name='editorialCategoryId')
    core_id = sgqlc.types.Field('StringFilter', graphql_name='coreId')
    core_document = sgqlc.types.Field(JSONFilter, graphql_name='coreDocument')
    image_collection_id = sgqlc.types.Field(
        'StringFilter', graphql_name='imageCollectionId')
    last_item_modified = sgqlc.types.Field(
        DatetimeFilter, graphql_name='lastItemModified')
    last_item_added = sgqlc.types.Field(
        DatetimeFilter, graphql_name='lastItemAdded')
    image = sgqlc.types.Field(ImageTypeFilter, graphql_name='image')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ProgramSetFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('ProgramSetFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('ProgramSetFilter', graphql_name='not')


class ProgramSetFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(IntFilterB, graphql_name='id')


class ProgramSetRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(IntFilterB, graphql_name='id')


class ProgramSetSubscriptionConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'last_visited_at',
                       'modified_at', 'subscribed_at', 'empty')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    last_visited_at = sgqlc.types.Field(
        DateFilterB, graphql_name='lastVisitedAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    subscribed_at = sgqlc.types.Field(DateFilterB, graphql_name='subscribedAt')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')


class ProgramSetSubscriptionCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('type', 'last_visited_at',
                       'subscribed_at', 'subscribed_program_set')
    type = sgqlc.types.Field(String, graphql_name='type')
    last_visited_at = sgqlc.types.Field(DateTime, graphql_name='lastVisitedAt')
    subscribed_at = sgqlc.types.Field(DateTime, graphql_name='subscribedAt')
    subscribed_program_set = sgqlc.types.Field(sgqlc.types.non_null(
        ProgramSetCreateInput), graphql_name='subscribedProgramSet')


class ProgramSetSubscriptionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'last_visited_at',
                       'modified_at', 'subscribed_at')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    last_visited_at = sgqlc.types.Field(
        DateFilterB, graphql_name='lastVisitedAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    subscribed_at = sgqlc.types.Field(DateFilterB, graphql_name='subscribedAt')


class ProgramSetSubscriptionRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'last_visited_at',
                       'modified_at', 'subscribed_at')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    last_visited_at = sgqlc.types.Field(
        DateFilterB, graphql_name='lastVisitedAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    subscribed_at = sgqlc.types.Field(DateFilterB, graphql_name='subscribedAt')


class ProgramSetSubscriptionRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'program_set_subscription')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    program_set_subscription = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='programSetSubscription')


class ProgramSetSubscriptionUpdateByProgramSetIdInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'program_set_subscription')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    program_set_subscription = sgqlc.types.Field(sgqlc.types.non_null(
        ProgramSetSubscriptionCreateInput), graphql_name='programSetSubscription')


class ProgramSetSubscriptionUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'last_visited_at',
                       'subscribed_at', 'subscribed_program_set')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_visited_at = sgqlc.types.Field(DateTime, graphql_name='lastVisitedAt')
    subscribed_at = sgqlc.types.Field(DateTime, graphql_name='subscribedAt')
    subscribed_program_set = sgqlc.types.Field(
        ProgramSetCreateInput, graphql_name='subscribedProgramSet')


class PropertyConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class PropertyCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type', 'key', 'value')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='value')


class PropertyFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'key', 'modified_at', 'user', 'value')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    key = sgqlc.types.Field('StringFilterB', graphql_name='key')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    user = sgqlc.types.Field(EndUserRelationFilterB, graphql_name='user')
    value = sgqlc.types.Field('StringFilterB', graphql_name='value')


class PropertyRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field(IDFilterB, graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class PropertyRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'property')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    property = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='property')


class PropertyUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'key', 'value')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(String, graphql_name='key')
    value = sgqlc.types.Field(String, graphql_name='value')


class PublicationServiceCondition(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'organization_name', 'title', 'synopsis', 'genre', 'branding_color', 'dvb_service_id',
                       'number_of_elements', 'image', 'core_id', 'core_document', 'external_ids', 'homepage_url', 'order', 'parent_service_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    organization_name = sgqlc.types.Field(
        String, graphql_name='organizationName')
    title = sgqlc.types.Field(String, graphql_name='title')
    synopsis = sgqlc.types.Field(String, graphql_name='synopsis')
    genre = sgqlc.types.Field(String, graphql_name='genre')
    branding_color = sgqlc.types.Field(String, graphql_name='brandingColor')
    dvb_service_id = sgqlc.types.Field(Int, graphql_name='dvbServiceId')
    number_of_elements = sgqlc.types.Field(
        Int, graphql_name='numberOfElements')
    image = sgqlc.types.Field(ImageTypeInput, graphql_name='image')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    homepage_url = sgqlc.types.Field(String, graphql_name='homepageUrl')
    order = sgqlc.types.Field(Int, graphql_name='order')
    parent_service_id = sgqlc.types.Field(
        String, graphql_name='parentServiceId')


class PublicationServiceFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'organization_name', 'title', 'synopsis', 'genre', 'branding_color', 'dvb_service_id', 'number_of_elements',
                       'core_id', 'core_document', 'external_ids', 'homepage_url', 'order', 'parent_service_id', 'image', 'and_', 'or_', 'not_')
    id = sgqlc.types.Field(IntFilter, graphql_name='id')
    organization_name = sgqlc.types.Field(
        'StringFilter', graphql_name='organizationName')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')
    synopsis = sgqlc.types.Field('StringFilter', graphql_name='synopsis')
    genre = sgqlc.types.Field('StringFilter', graphql_name='genre')
    branding_color = sgqlc.types.Field(
        'StringFilter', graphql_name='brandingColor')
    dvb_service_id = sgqlc.types.Field(IntFilter, graphql_name='dvbServiceId')
    number_of_elements = sgqlc.types.Field(
        IntFilter, graphql_name='numberOfElements')
    core_id = sgqlc.types.Field('StringFilter', graphql_name='coreId')
    core_document = sgqlc.types.Field(JSONFilter, graphql_name='coreDocument')
    external_ids = sgqlc.types.Field(
        'StringListFilter', graphql_name='externalIds')
    homepage_url = sgqlc.types.Field(
        'StringFilter', graphql_name='homepageUrl')
    order = sgqlc.types.Field(IntFilter, graphql_name='order')
    parent_service_id = sgqlc.types.Field(
        'StringFilter', graphql_name='parentServiceId')
    image = sgqlc.types.Field(ImageTypeFilter, graphql_name='image')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('PublicationServiceFilter')), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('PublicationServiceFilter')), graphql_name='or')
    not_ = sgqlc.types.Field('PublicationServiceFilter', graphql_name='not')


class PublishScheduledItemsInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')


class PublishableThingConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class PublishableThingFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'modified_at', 'no_index')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    no_index = sgqlc.types.Field(BooleanFilterB, graphql_name='noIndex')


class PublishableThingRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field(IDFilterB, graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class QueueConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class QueueCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type', 'entries')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    entries = sgqlc.types.Field(sgqlc.types.list_of(
        ItemCreateInput), graphql_name='entries')


class QueueEntryListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'entry', 'queue')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    entry = sgqlc.types.Field(sgqlc.types.non_null(
        ItemCreateInput), graphql_name='entry')
    queue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='queue')


class QueueFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'modified_at', 'user')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    user = sgqlc.types.Field(EndUserRelationFilterB, graphql_name='user')


class QueueRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field(IDFilterB, graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class QueueRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'queue')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    queue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='queue')


class QueueUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'entries')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    entries = sgqlc.types.Field(sgqlc.types.list_of(
        ItemCreateInput), graphql_name='entries')


class RemoteIDFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_')
    eq = sgqlc.types.Field(ID, graphql_name='eq')
    ne = sgqlc.types.Field(ID, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')


class StatusFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from',
                       'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(Status, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(Status, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(Status, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        Status, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Status)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(Status)), graphql_name='notIn')
    less_than = sgqlc.types.Field(Status, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        Status, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Status, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        Status, graphql_name='greaterThanOrEqualTo')


class StreamTypeInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('url', 'title', 'mimetype', 'id')
    url = sgqlc.types.Field(String, graphql_name='url')
    title = sgqlc.types.Field(String, graphql_name='title')
    mimetype = sgqlc.types.Field(String, graphql_name='mimetype')
    id = sgqlc.types.Field(String, graphql_name='id')


class StringFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from', 'in_', 'not_in', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to', 'includes', 'not_includes', 'includes_insensitive', 'not_includes_insensitive', 'starts_with', 'not_starts_with', 'starts_with_insensitive', 'not_starts_with_insensitive', 'ends_with', 'not_ends_with',
                       'ends_with_insensitive', 'not_ends_with_insensitive', 'like', 'not_like', 'like_insensitive', 'not_like_insensitive', 'equal_to_insensitive', 'not_equal_to_insensitive', 'distinct_from_insensitive', 'not_distinct_from_insensitive', 'in_insensitive', 'not_in_insensitive', 'less_than_insensitive', 'less_than_or_equal_to_insensitive', 'greater_than_insensitive', 'greater_than_or_equal_to_insensitive')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(String, graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(String, graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(String, graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        String, graphql_name='notDistinctFrom')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(String)), graphql_name='in')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(String)), graphql_name='notIn')
    less_than = sgqlc.types.Field(String, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        String, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(String, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        String, graphql_name='greaterThanOrEqualTo')
    includes = sgqlc.types.Field(String, graphql_name='includes')
    not_includes = sgqlc.types.Field(String, graphql_name='notIncludes')
    includes_insensitive = sgqlc.types.Field(
        String, graphql_name='includesInsensitive')
    not_includes_insensitive = sgqlc.types.Field(
        String, graphql_name='notIncludesInsensitive')
    starts_with = sgqlc.types.Field(String, graphql_name='startsWith')
    not_starts_with = sgqlc.types.Field(String, graphql_name='notStartsWith')
    starts_with_insensitive = sgqlc.types.Field(
        String, graphql_name='startsWithInsensitive')
    not_starts_with_insensitive = sgqlc.types.Field(
        String, graphql_name='notStartsWithInsensitive')
    ends_with = sgqlc.types.Field(String, graphql_name='endsWith')
    not_ends_with = sgqlc.types.Field(String, graphql_name='notEndsWith')
    ends_with_insensitive = sgqlc.types.Field(
        String, graphql_name='endsWithInsensitive')
    not_ends_with_insensitive = sgqlc.types.Field(
        String, graphql_name='notEndsWithInsensitive')
    like = sgqlc.types.Field(String, graphql_name='like')
    not_like = sgqlc.types.Field(String, graphql_name='notLike')
    like_insensitive = sgqlc.types.Field(
        String, graphql_name='likeInsensitive')
    not_like_insensitive = sgqlc.types.Field(
        String, graphql_name='notLikeInsensitive')
    equal_to_insensitive = sgqlc.types.Field(
        String, graphql_name='equalToInsensitive')
    not_equal_to_insensitive = sgqlc.types.Field(
        String, graphql_name='notEqualToInsensitive')
    distinct_from_insensitive = sgqlc.types.Field(
        String, graphql_name='distinctFromInsensitive')
    not_distinct_from_insensitive = sgqlc.types.Field(
        String, graphql_name='notDistinctFromInsensitive')
    in_insensitive = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(String)), graphql_name='inInsensitive')
    not_in_insensitive = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(String)), graphql_name='notInInsensitive')
    less_than_insensitive = sgqlc.types.Field(
        String, graphql_name='lessThanInsensitive')
    less_than_or_equal_to_insensitive = sgqlc.types.Field(
        String, graphql_name='lessThanOrEqualToInsensitive')
    greater_than_insensitive = sgqlc.types.Field(
        String, graphql_name='greaterThanInsensitive')
    greater_than_or_equal_to_insensitive = sgqlc.types.Field(
        String, graphql_name='greaterThanOrEqualToInsensitive')


class StringFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('eq', 'ne', 'in_', 'gt', 'gte', 'lt',
                       'lte', 'starts_with', 'ends_with', 'matches')
    eq = sgqlc.types.Field(String, graphql_name='eq')
    ne = sgqlc.types.Field(String, graphql_name='ne')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='in')
    gt = sgqlc.types.Field(String, graphql_name='gt')
    gte = sgqlc.types.Field(String, graphql_name='gte')
    lt = sgqlc.types.Field(String, graphql_name='lt')
    lte = sgqlc.types.Field(String, graphql_name='lte')
    starts_with = sgqlc.types.Field(String, graphql_name='startsWith')
    ends_with = sgqlc.types.Field(String, graphql_name='endsWith')
    matches = sgqlc.types.Field(String, graphql_name='matches')


class StringListFilter(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('is_null', 'equal_to', 'not_equal_to', 'distinct_from', 'not_distinct_from', 'less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to',
                       'contains', 'contained_by', 'overlaps', 'any_equal_to', 'any_not_equal_to', 'any_less_than', 'any_less_than_or_equal_to', 'any_greater_than', 'any_greater_than_or_equal_to')
    is_null = sgqlc.types.Field(Boolean, graphql_name='isNull')
    equal_to = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='equalTo')
    not_equal_to = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='notEqualTo')
    distinct_from = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='distinctFrom')
    not_distinct_from = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='notDistinctFrom')
    less_than = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='greaterThanOrEqualTo')
    contains = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='contains')
    contained_by = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='containedBy')
    overlaps = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='overlaps')
    any_equal_to = sgqlc.types.Field(String, graphql_name='anyEqualTo')
    any_not_equal_to = sgqlc.types.Field(String, graphql_name='anyNotEqualTo')
    any_less_than = sgqlc.types.Field(String, graphql_name='anyLessThan')
    any_less_than_or_equal_to = sgqlc.types.Field(
        String, graphql_name='anyLessThanOrEqualTo')
    any_greater_than = sgqlc.types.Field(String, graphql_name='anyGreaterThan')
    any_greater_than_or_equal_to = sgqlc.types.Field(
        String, graphql_name='anyGreaterThanOrEqualTo')


class SubscriptionListConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class SubscriptionListCreateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'type', 'program_sets')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    type = sgqlc.types.Field(String, graphql_name='type')
    program_sets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        ProgramSetSubscriptionCreateInput)), graphql_name='programSets')


class SubscriptionListFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('created_at', 'modified_at', 'program_sets', 'user')
    created_at = sgqlc.types.Field(DateFilterB, graphql_name='createdAt')
    modified_at = sgqlc.types.Field(DateFilterB, graphql_name='modifiedAt')
    program_sets = sgqlc.types.Field(
        ProgramSetSubscriptionConnectionFilterB, graphql_name='programSets')
    user = sgqlc.types.Field(EndUserRelationFilterB, graphql_name='user')


class SubscriptionListProgramSetListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id',
                       'program_set', 'subscription_list')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    program_set = sgqlc.types.Field(sgqlc.types.non_null(
        ProgramSetSubscriptionCreateInput), graphql_name='programSet')
    subscription_list = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='subscriptionList')


class SubscriptionListRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field(IDFilterB, graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


class SubscriptionListRemoveAllListInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'subscription_list')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    subscription_list = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='subscriptionList')


class SubscriptionListUpdateInput(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'id', 'program_sets')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    program_sets = sgqlc.types.Field(sgqlc.types.list_of(
        ProgramSetSubscriptionCreateInput), graphql_name='programSets')


class SystemConnectionFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('empty', 'contains')
    empty = sgqlc.types.Field(BooleanFilterB, graphql_name='empty')
    contains = sgqlc.types.Field(ID, graphql_name='contains')


class SystemRelationFilterB(sgqlc.types.Input):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'exists')
    id = sgqlc.types.Field(IDFilterB, graphql_name='id')
    exists = sgqlc.types.Field(BooleanFilterB, graphql_name='exists')


########################################################################
# Output Objects and Interfaces
########################################################################
class AssetType(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('url', 'download_url', 'allow_download',
                       'size', 'title', 'mime_type')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')
    download_url = sgqlc.types.Field(URL, graphql_name='downloadUrl')
    allow_download = sgqlc.types.Field(Boolean, graphql_name='allowDownload')
    size = sgqlc.types.Field(Int, graphql_name='size')
    title = sgqlc.types.Field(String, graphql_name='title')
    mime_type = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='mimeType')


class Board(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('tracking', 'id', 'title', 'image', 'sections', 'widgets', 'sharing_url',
                       'recent_items', 'recent_items_list', 'program_sets', 'program_sets_list')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    image = sgqlc.types.Field('ImageType', graphql_name='image')
    sections = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Section')), graphql_name='sections', args=sgqlc.types.ArgDict((
        ('hide_unresolved_teasers', sgqlc.types.Arg(
            Boolean, graphql_name='hideUnresolvedTeasers', default=True)),
        ('hide_personalizied_sections', sgqlc.types.Arg(
            Boolean, graphql_name='hidePersonaliziedSections', default=False)),
        ('hide_errors', sgqlc.types.Arg(
            Boolean, graphql_name='hideErrors', default=True)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
    ))
    )
    widgets = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('SophoraWidget')), graphql_name='widgets')
    sharing_url = sgqlc.types.Field(URL, graphql_name='sharingUrl')
    recent_items = sgqlc.types.Field(sgqlc.types.non_null('ItemsConnection'), graphql_name='recentItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(
            sgqlc.types.non_null(ItemsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    recent_items_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Item')), graphql_name='recentItemsList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(
            sgqlc.types.non_null(ItemsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    program_sets = sgqlc.types.Field(sgqlc.types.non_null('EditorialCategoryProgramSetsManyToManyConnection'), graphql_name='programSets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ProgramSetsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    program_sets_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProgramSet'))), graphql_name='programSetsList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ProgramSetsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(ProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )


class BookmarkConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'BookmarkEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'BookmarkInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')


class BookmarkEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('BookmarkInterface', graphql_name='node')


class BookmarkInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'belongs_to',
                       'bookmarked_at', 'created_at', 'item', 'modified_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    belongs_to = sgqlc.types.Field(
        'BookmarkListInterface', graphql_name='belongsTo')
    bookmarked_at = sgqlc.types.Field(DateTime, graphql_name='bookmarkedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    item = sgqlc.types.Field('Item', graphql_name='item')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')


class BookmarkListConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'BookmarkListEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'BookmarkListInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')


class BookmarkListEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('BookmarkListInterface', graphql_name='node')


class BookmarkListInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at',
                       'entries', 'modified_at', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    entries = sgqlc.types.Field(BookmarkConnection, graphql_name='entries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(BookmarkFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(BookmarkSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    user = sgqlc.types.Field('EndUserInterface', graphql_name='user')


class BookmarkListPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_bookmark_list')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_bookmark_list = sgqlc.types.Field(
        'BookmarkList', graphql_name='changedBookmarkList')


class BookmarkPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_bookmark')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_bookmark = sgqlc.types.Field(
        'Bookmark', graphql_name='changedBookmark')


class CategoriesToProgramSetsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('CategoriesToProgramSet'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('CategoriesToProgramSetsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class CategoriesToProgramSetsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'CategoriesToProgramSet'), graphql_name='node')


class ConceptsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('Concept'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ConceptsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class ConceptsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'Concept'), graphql_name='node')


class ConfigsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('Config'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ConfigsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class ConfigsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(
        sgqlc.types.non_null('Config'), graphql_name='node')


class CoreTeaser(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'title')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='title')


class DebugShowGroupEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'DebugShowGroupsRecord'), graphql_name='node')


class DebugShowGroupsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('DebugShowGroupsRecord'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null(DebugShowGroupEdge))), graphql_name='edges')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class DebugShowGroupsRecord(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'core_id', 'publish_date', 'modified_publish_date', 'title', 'title_without_number',
                       'group_number', 'max_group_number', 'season_number', 'group_id', 'core_type', 'external_id')
    row_id = sgqlc.types.Field(Int, graphql_name='rowId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    publish_date = sgqlc.types.Field(Datetime, graphql_name='publishDate')
    modified_publish_date = sgqlc.types.Field(
        Datetime, graphql_name='modifiedPublishDate')
    title = sgqlc.types.Field(String, graphql_name='title')
    title_without_number = sgqlc.types.Field(
        String, graphql_name='titleWithoutNumber')
    group_number = sgqlc.types.Field(Int, graphql_name='groupNumber')
    max_group_number = sgqlc.types.Field(Int, graphql_name='maxGroupNumber')
    season_number = sgqlc.types.Field(Int, graphql_name='seasonNumber')
    group_id = sgqlc.types.Field(Int, graphql_name='groupId')
    core_type = sgqlc.types.Field(String, graphql_name='coreType')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')


class DeletePayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')


class DepublishExpiredItemsPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'big_int', 'query')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    big_int = sgqlc.types.Field(BigInt, graphql_name='bigInt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class EditorialCategoriesConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info',
                       'total_count', 'title', 'tracking')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCategory')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCategoriesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')
    title = sgqlc.types.Field(String, graphql_name='title')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')


class EditorialCategoriesEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'EditorialCategory'), graphql_name='node')


class EditorialCategoryProgramSetsManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ProgramSet'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(
        'EditorialCategoryProgramSetsManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class EditorialCategoryProgramSetsManyToManyEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'ProgramSet'), graphql_name='node')


class EditorialCollectionsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCollection')), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCollectionsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class EditorialCollectionsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'EditorialCollection'), graphql_name='node')


class EndUserConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'EndUserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'EndUserInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')


class EndUserEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EndUserInterface', graphql_name='node')


class EndUserInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'bookmarks', 'created_at', 'history', 'local_id',
                       'login_id', 'modified_at', 'playlists', 'properties', 'queue', 'subscriptions', 'sync_successful')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    bookmarks = sgqlc.types.Field(
        BookmarkListInterface, graphql_name='bookmarks')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    history = sgqlc.types.Field('HistoryEntryConnection', graphql_name='history', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(HistoryEntryFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(HistoryEntrySortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    local_id = sgqlc.types.Field(String, graphql_name='localId')
    login_id = sgqlc.types.Field(String, graphql_name='loginId')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    playlists = sgqlc.types.Field('PlaylistConnection', graphql_name='playlists', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(PlaylistFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(PlaylistSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    properties = sgqlc.types.Field('PropertyConnection', graphql_name='properties', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(PropertyFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(PropertySortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    queue = sgqlc.types.Field('QueueInterface', graphql_name='queue')
    subscriptions = sgqlc.types.Field(
        'SubscriptionListInterface', graphql_name='subscriptions')
    sync_successful = sgqlc.types.Field(Boolean, graphql_name='syncSuccessful')


class EndUserPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_end_user')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_end_user = sgqlc.types.Field(
        'EndUser', graphql_name='changedEndUser')


class GroupingsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('Grouping'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('GroupingsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class GroupingsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'Grouping'), graphql_name='node')


class HistoryEntryConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'HistoryEntryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'HistoryEntryInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')


class HistoryEntryEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('HistoryEntryInterface', graphql_name='node')


class HistoryEntryInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at', 'item',
                       'last_listened_at', 'modified_at', 'progress', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    item = sgqlc.types.Field('Item', graphql_name='item')
    last_listened_at = sgqlc.types.Field(
        DateTime, graphql_name='lastListenedAt')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    progress = sgqlc.types.Field(Float, graphql_name='progress')
    user = sgqlc.types.Field(EndUserInterface, graphql_name='user')


class HistoryEntryPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_history_entry')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_history_entry = sgqlc.types.Field(
        'HistoryEntry', graphql_name='changedHistoryEntry')


class ImageType(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('url', 'url1_x1', 'description', 'attribution')
    url = sgqlc.types.Field(String, graphql_name='url')
    url1_x1 = sgqlc.types.Field(String, graphql_name='url1X1')
    description = sgqlc.types.Field(String, graphql_name='description')
    attribution = sgqlc.types.Field(String, graphql_name='attribution')


class ImagesCollectionsBinariesView(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('image_collection_id', 'image_id', 'title', 'producer_name',
                       'image_binary_id', 'aspect_ratio', 'height', 'width', 'media_type', 'file_location', 'url')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    image_id = sgqlc.types.Field(String, graphql_name='imageId')
    title = sgqlc.types.Field(String, graphql_name='title')
    producer_name = sgqlc.types.Field(String, graphql_name='producerName')
    image_binary_id = sgqlc.types.Field(String, graphql_name='imageBinaryId')
    aspect_ratio = sgqlc.types.Field(String, graphql_name='aspectRatio')
    height = sgqlc.types.Field(Int, graphql_name='height')
    width = sgqlc.types.Field(Int, graphql_name='width')
    media_type = sgqlc.types.Field(String, graphql_name='mediaType')
    file_location = sgqlc.types.Field(String, graphql_name='fileLocation')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ImagesCollectionsBinariesViewsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null(ImagesCollectionsBinariesView))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ImagesCollectionsBinariesViewsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class ImagesCollectionsBinariesViewsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        ImagesCollectionsBinariesView), graphql_name='node')


class ItemConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'ItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(
        sgqlc.types.list_of('Item'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')


class ItemEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Item', graphql_name='node')


class ItemsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(
        sgqlc.types.list_of(sgqlc.types.non_null('Item'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ItemsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class ItemsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Item'), graphql_name='node')


class ItemsSearchConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('page_info', 'total_count', 'nodes')
    page_info = sgqlc.types.Field('PageInfo', graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(
        sgqlc.types.list_of(sgqlc.types.non_null('Item'))), graphql_name='nodes')


class MigrationsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('Migration'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('MigrationsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class MigrationsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'Migration'), graphql_name='node')


class Mutation(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('delete_history_entry_by_item', 'update_program_set_subscription_by_program_set', 'sync_user_data', 'update_bookmark', 'create_bookmark_list', 'update_bookmark_list', 'add_entry_to_bookmark_list', 'remove_entry_from_bookmark_list', 'remove_all_entries_from_bookmark_list', 'create_end_user', 'upsert_end_user', 'update_end_user', 'create_history_entry', 'upsert_history_entry', 'update_history_entry', 'create_playlist', 'update_playlist', 'add_entry_to_playlist',
                       'remove_entry_from_playlist', 'remove_all_entries_from_playlist', 'update_program_set_subscription', 'create_property', 'update_property', 'create_queue', 'update_queue', 'add_entry_to_queue', 'remove_entry_from_queue', 'remove_all_entries_from_queue', 'create_subscription_list', 'update_subscription_list', 'add_program_set_to_subscription_list', 'remove_program_set_from_subscription_list', 'remove_all_program_sets_from_subscription_list', 'delete_history_entry', 'delete_playlist')
    delete_history_entry_by_item = sgqlc.types.Field(DeletePayload, graphql_name='deleteHistoryEntryByItem', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(DeleteHistoryEntryByItemInput,
         graphql_name='input', default=None)),
    ))
    )
    update_program_set_subscription_by_program_set = sgqlc.types.Field('ProgramSetSubscriptionPayload', graphql_name='updateProgramSetSubscriptionByProgramSet', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ProgramSetSubscriptionUpdateByProgramSetIdInput,
         graphql_name='input', default=None)),
    ))
    )
    sync_user_data = sgqlc.types.Field(EndUserPayload, graphql_name='syncUserData', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(EndUserSyncInput, graphql_name='input', default=None)),
    ))
    )
    update_bookmark = sgqlc.types.Field(BookmarkPayload, graphql_name='updateBookmark', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            BookmarkUpdateInput), graphql_name='input', default=None)),
    ))
    )
    create_bookmark_list = sgqlc.types.Field(BookmarkListPayload, graphql_name='createBookmarkList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            BookmarkListCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_bookmark_list = sgqlc.types.Field(BookmarkListPayload, graphql_name='updateBookmarkList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            BookmarkListUpdateInput), graphql_name='input', default=None)),
    ))
    )
    add_entry_to_bookmark_list = sgqlc.types.Field(BookmarkListPayload, graphql_name='addEntryToBookmarkList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            BookmarkListEntryListInput), graphql_name='input', default=None)),
    ))
    )
    remove_entry_from_bookmark_list = sgqlc.types.Field(BookmarkListPayload, graphql_name='removeEntryFromBookmarkList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            BookmarkListEntryListInput), graphql_name='input', default=None)),
    ))
    )
    remove_all_entries_from_bookmark_list = sgqlc.types.Field(BookmarkListPayload, graphql_name='removeAllEntriesFromBookmarkList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            BookmarkListRemoveAllListInput), graphql_name='input', default=None)),
    ))
    )
    create_end_user = sgqlc.types.Field(EndUserPayload, graphql_name='createEndUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            EndUserCreateInput), graphql_name='input', default=None)),
    ))
    )
    upsert_end_user = sgqlc.types.Field(EndUserPayload, graphql_name='upsertEndUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            EndUserCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_end_user = sgqlc.types.Field(EndUserPayload, graphql_name='updateEndUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            EndUserUpdateInput), graphql_name='input', default=None)),
    ))
    )
    create_history_entry = sgqlc.types.Field(HistoryEntryPayload, graphql_name='createHistoryEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            HistoryEntryCreateInput), graphql_name='input', default=None)),
    ))
    )
    upsert_history_entry = sgqlc.types.Field(HistoryEntryPayload, graphql_name='upsertHistoryEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            HistoryEntryCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_history_entry = sgqlc.types.Field(HistoryEntryPayload, graphql_name='updateHistoryEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            HistoryEntryUpdateInput), graphql_name='input', default=None)),
    ))
    )
    create_playlist = sgqlc.types.Field('PlaylistPayload', graphql_name='createPlaylist', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PlaylistCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_playlist = sgqlc.types.Field('PlaylistPayload', graphql_name='updatePlaylist', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PlaylistUpdateInput), graphql_name='input', default=None)),
    ))
    )
    add_entry_to_playlist = sgqlc.types.Field('PlaylistPayload', graphql_name='addEntryToPlaylist', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PlaylistEntryListInput), graphql_name='input', default=None)),
    ))
    )
    remove_entry_from_playlist = sgqlc.types.Field('PlaylistPayload', graphql_name='removeEntryFromPlaylist', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PlaylistEntryListInput), graphql_name='input', default=None)),
    ))
    )
    remove_all_entries_from_playlist = sgqlc.types.Field('PlaylistPayload', graphql_name='removeAllEntriesFromPlaylist', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PlaylistRemoveAllListInput), graphql_name='input', default=None)),
    ))
    )
    update_program_set_subscription = sgqlc.types.Field('ProgramSetSubscriptionPayload', graphql_name='updateProgramSetSubscription', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            ProgramSetSubscriptionUpdateInput), graphql_name='input', default=None)),
    ))
    )
    create_property = sgqlc.types.Field('PropertyPayload', graphql_name='createProperty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PropertyCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_property = sgqlc.types.Field('PropertyPayload', graphql_name='updateProperty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            PropertyUpdateInput), graphql_name='input', default=None)),
    ))
    )
    create_queue = sgqlc.types.Field('QueuePayload', graphql_name='createQueue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            QueueCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_queue = sgqlc.types.Field('QueuePayload', graphql_name='updateQueue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            QueueUpdateInput), graphql_name='input', default=None)),
    ))
    )
    add_entry_to_queue = sgqlc.types.Field('QueuePayload', graphql_name='addEntryToQueue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            QueueEntryListInput), graphql_name='input', default=None)),
    ))
    )
    remove_entry_from_queue = sgqlc.types.Field('QueuePayload', graphql_name='removeEntryFromQueue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            QueueEntryListInput), graphql_name='input', default=None)),
    ))
    )
    remove_all_entries_from_queue = sgqlc.types.Field('QueuePayload', graphql_name='removeAllEntriesFromQueue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            QueueRemoveAllListInput), graphql_name='input', default=None)),
    ))
    )
    create_subscription_list = sgqlc.types.Field('SubscriptionListPayload', graphql_name='createSubscriptionList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            SubscriptionListCreateInput), graphql_name='input', default=None)),
    ))
    )
    update_subscription_list = sgqlc.types.Field('SubscriptionListPayload', graphql_name='updateSubscriptionList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            SubscriptionListUpdateInput), graphql_name='input', default=None)),
    ))
    )
    add_program_set_to_subscription_list = sgqlc.types.Field('SubscriptionListPayload', graphql_name='addProgramSetToSubscriptionList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            SubscriptionListProgramSetListInput), graphql_name='input', default=None)),
    ))
    )
    remove_program_set_from_subscription_list = sgqlc.types.Field('SubscriptionListPayload', graphql_name='removeProgramSetFromSubscriptionList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            SubscriptionListProgramSetListInput), graphql_name='input', default=None)),
    ))
    )
    remove_all_program_sets_from_subscription_list = sgqlc.types.Field('SubscriptionListPayload', graphql_name='removeAllProgramSetsFromSubscriptionList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            SubscriptionListRemoveAllListInput), graphql_name='input', default=None)),
    ))
    )
    delete_history_entry = sgqlc.types.Field(DeletePayload, graphql_name='deleteHistoryEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            DeleteInput), graphql_name='input', default=None)),
    ))
    )
    delete_playlist = sgqlc.types.Field(DeletePayload, graphql_name='deletePlaylist', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(
            DeleteInput), graphql_name='input', default=None)),
    ))
    )


class Node(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name='nodeId')


class OrganizationsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info',
                       'total_count', '_links', 'tracking')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('Organization'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('OrganizationsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(
        'PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')
    _links = sgqlc.types.Field(JSON, graphql_name='_links')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')


class OrganizationsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'Organization'), graphql_name='node')


class PageInfo(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('has_next_page', 'has_previous_page',
                       'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(Cursor, graphql_name='startCursor')
    end_cursor = sgqlc.types.Field(Cursor, graphql_name='endCursor')


class PermanentLivestreamsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('PermanentLivestream'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('PermanentLivestreamsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class PermanentLivestreamsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'PermanentLivestream'), graphql_name='node')


class PermantentLivestreamConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('total_count', 'nodes')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('PermanentLivestream')), graphql_name='nodes')


class PlaylistConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'PlaylistEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'PlaylistInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PlaylistEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PlaylistInterface', graphql_name='node')


class PlaylistInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at', 'entries',
                       'modified_at', 'private', 'sort_index', 'title', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    entries = sgqlc.types.Field(ItemConnection, graphql_name='entries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilterB, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(ItemSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    sort_index = sgqlc.types.Field(Int, graphql_name='sortIndex')
    title = sgqlc.types.Field(String, graphql_name='title')
    user = sgqlc.types.Field(EndUserInterface, graphql_name='user')


class PlaylistPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_playlist')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_playlist = sgqlc.types.Field(
        'Playlist', graphql_name='changedPlaylist')


class ProgramSetConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'ProgramSetEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'ProgramSet'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProgramSetEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProgramSet', graphql_name='node')


class ProgramSetEditorialCategoriesManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('EditorialCategory'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(
        'ProgramSetEditorialCategoriesManyToManyEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProgramSetEditorialCategoriesManyToManyEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'EditorialCategory'), graphql_name='node')


class ProgramSetSubscriptionConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'ProgramSetSubscriptionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'ProgramSetSubscriptionInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProgramSetSubscriptionEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(
        'ProgramSetSubscriptionInterface', graphql_name='node')


class ProgramSetSubscriptionInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'belongs_to', 'created_at',
                       'last_visited_at', 'modified_at', 'subscribed_at', 'subscribed_program_set')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    belongs_to = sgqlc.types.Field(
        'SubscriptionListInterface', graphql_name='belongsTo')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    last_visited_at = sgqlc.types.Field(DateTime, graphql_name='lastVisitedAt')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    subscribed_at = sgqlc.types.Field(DateTime, graphql_name='subscribedAt')
    subscribed_program_set = sgqlc.types.Field(
        'ProgramSet', graphql_name='subscribedProgramSet')


class ProgramSetSubscriptionPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id',
                       'changed_program_set_subscription')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_program_set_subscription = sgqlc.types.Field(
        'ProgramSetSubscription', graphql_name='changedProgramSetSubscription')


class ProgramSetsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ProgramSet'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ProgramSetsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProgramSetsEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'ProgramSet'), graphql_name='node')


class ProgramSetsSearchConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('page_info', 'total_count', 'nodes')
    page_info = sgqlc.types.Field(PageInfo, graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('ProgramSet'))), graphql_name='nodes')


class PropertyConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'PropertyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'PropertyInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PropertyEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PropertyInterface', graphql_name='node')


class PropertyInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at',
                       'key', 'modified_at', 'user', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    key = sgqlc.types.Field(String, graphql_name='key')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    user = sgqlc.types.Field(EndUserInterface, graphql_name='user')
    value = sgqlc.types.Field(String, graphql_name='value')


class PropertyPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_property')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_property = sgqlc.types.Field(
        'Property', graphql_name='changedProperty')


class PublicationServicesConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('PublicationService'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(
        sgqlc.types.non_null('PublicationServicesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='totalCount')


class PublicationServicesEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(
        'PublicationService'), graphql_name='node')


class PublishScheduledItemsPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'big_int', 'query')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    big_int = sgqlc.types.Field(BigInt, graphql_name='bigInt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class PublishableThingConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'PublishableThingEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'PublishableThingInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PublishableThingEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PublishableThingInterface', graphql_name='node')


class PublishableThingInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at',
                       'modified_at', 'no_index')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    no_index = sgqlc.types.Field(Boolean, graphql_name='noIndex')


class Query(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('all_end_users', 'all_playlists', 'bookmark', 'bookmark_list', 'end_user', 'history_entry', 'playlist', 'program_set_subscription', 'system', 'configs', 'editorial_categories', 'editorial_collections', 'groupings', 'images_collections_binaries_views', 'items', 'migrations', 'organizations', 'permanent_livestreams', 'program_sets', 'publication_services', 'audio_binary', 'categories_to_program_set', 'concept', 'config', 'editorial_category', 'editorial_category_by_sophora_id', 'editorial_collection', 'editorial_collection_by_coremedia_id', 'grouping', 'grouping_by_core_id', 'image_binary', 'image_collection', 'image', 'item', 'item_by_core_id', 'item_by_external_id', 'migration', 'migration_by_name', 'organization_by_id', 'organization', 'organization_by_core_id', 'permanent_livestream', 'permanent_livestream_by_core_id', 'program_set', 'program_set_by_core_id', 'publication_service', 'publication_service_by_title',
                       'publication_service_by_core_id', 'transcript', 'debug_show_groups', 'editorial_categories_by_ids', 'editorial_categories_by_ids_list', 'editorial_collections_by_ids', 'editorial_collections_by_ids_list', 'isnumeric', 'items_by_ids', 'items_by_ids_list', 'jsonb_array', 'program_sets_by_ids', 'program_sets_by_ids_list', 'shows_with_mapping', 'shows_with_mapping_list', 'audio_binary_by_node_id', 'categories_to_program_set_by_node_id', 'concept_by_node_id', 'config_by_node_id', 'editorial_category_by_node_id', 'editorial_collection_by_node_id', 'grouping_by_node_id', 'image_binary_by_node_id', 'image_collection_by_node_id', 'image_by_node_id', 'item_by_node_id', 'migration_by_node_id', 'organization_by_node_id', 'permanent_livestream_by_node_id', 'program_set_by_node_id', 'publication_service_by_node_id', 'transcript_by_node_id', 'search', 'homescreen', 'show', 'section', 'widget', 'widgets', 'compilations', 'teasers', 'node')
    all_end_users = sgqlc.types.Field(EndUserConnection, graphql_name='allEndUsers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(EndUserFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(EndUserSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    all_playlists = sgqlc.types.Field(PlaylistConnection, graphql_name='allPlaylists', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(PlaylistFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(PlaylistSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    bookmark = sgqlc.types.Field(BookmarkInterface, graphql_name='bookmark', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    bookmark_list = sgqlc.types.Field(BookmarkListInterface, graphql_name='bookmarkList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    end_user = sgqlc.types.Field(EndUserInterface, graphql_name='endUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    history_entry = sgqlc.types.Field(HistoryEntryInterface, graphql_name='historyEntry', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    playlist = sgqlc.types.Field(PlaylistInterface, graphql_name='playlist', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    program_set_subscription = sgqlc.types.Field(ProgramSetSubscriptionInterface, graphql_name='programSetSubscription', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    system = sgqlc.types.Field('SystemInterface', graphql_name='system', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    configs = sgqlc.types.Field(ConfigsConnection, graphql_name='configs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ConfigsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ConfigCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ConfigFilter, graphql_name='filter', default=None)),
    ))
    )
    editorial_categories = sgqlc.types.Field(EditorialCategoriesConnection, graphql_name='editorialCategories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            EditorialCategoriesOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(EditorialCategoryCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(EditorialCategoryFilter,
         graphql_name='filter', default=None)),
    ))
    )
    editorial_collections = sgqlc.types.Field(EditorialCollectionsConnection, graphql_name='editorialCollections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            EditorialCollectionsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(EditorialCollectionCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(EditorialCollectionFilter,
         graphql_name='filter', default=None)),
    ))
    )
    groupings = sgqlc.types.Field(GroupingsConnection, graphql_name='groupings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            GroupingsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(GroupingCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(GroupingFilter,
         graphql_name='filter', default=None)),
    ))
    )
    images_collections_binaries_views = sgqlc.types.Field(ImagesCollectionsBinariesViewsConnection, graphql_name='imagesCollectionsBinariesViews', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ImagesCollectionsBinariesViewsOrderBy)), graphql_name='orderBy', default=('NATURAL',))),
        ('condition', sgqlc.types.Arg(ImagesCollectionsBinariesViewCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ImagesCollectionsBinariesViewFilter,
         graphql_name='filter', default=None)),
    ))
    )
    items = sgqlc.types.Field(ItemsConnection, graphql_name='items', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ItemsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    migrations = sgqlc.types.Field(MigrationsConnection, graphql_name='migrations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            MigrationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(MigrationCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(MigrationFilter,
         graphql_name='filter', default=None)),
    ))
    )
    organizations = sgqlc.types.Field(OrganizationsConnection, graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            OrganizationsOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(OrganizationCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(OrganizationFilter,
         graphql_name='filter', default=None)),
    ))
    )
    permanent_livestreams = sgqlc.types.Field(PermanentLivestreamsConnection, graphql_name='permanentLivestreams', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            PermanentLivestreamsOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(PermanentLivestreamCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(PermanentLivestreamFilter,
         graphql_name='filter', default=None)),
    ))
    )
    program_sets = sgqlc.types.Field(ProgramSetsConnection, graphql_name='programSets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ProgramSetsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    publication_services = sgqlc.types.Field(PublicationServicesConnection, graphql_name='publicationServices', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            PublicationServicesOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(PublicationServiceCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(PublicationServiceFilter,
         graphql_name='filter', default=None)),
    ))
    )
    audio_binary = sgqlc.types.Field('AudioBinary', graphql_name='audioBinary', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='id', default=None)),
    ))
    )
    categories_to_program_set = sgqlc.types.Field('CategoriesToProgramSet', graphql_name='categoriesToProgramSet', args=sgqlc.types.ArgDict((
        ('program_set_core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='programSetCoreId', default=None)),
        ('category_sophora_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='categorySophoraId', default=None)),
    ))
    )
    concept = sgqlc.types.Field('Concept', graphql_name='concept', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(
            Int), graphql_name='itemId', default=None)),
        ('concept_source', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='conceptSource', default=None)),
    ))
    )
    config = sgqlc.types.Field('Config', graphql_name='config', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='key', default=None)),
    ))
    )
    editorial_category = sgqlc.types.Field(Board, graphql_name='editorialCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
        ('source', sgqlc.types.Arg(SourceSystem, graphql_name='source', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=12)),
    ))
    )
    editorial_category_by_sophora_id = sgqlc.types.Field('EditorialCategory', graphql_name='editorialCategoryBySophoraId', args=sgqlc.types.ArgDict((
        ('sophora_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='sophoraId', default=None)),
    ))
    )
    editorial_collection = sgqlc.types.Field('EditorialCollection', graphql_name='editorialCollection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=12)),
        ('source', sgqlc.types.Arg(SourceSystem, graphql_name='source', default=None)),
    ))
    )
    editorial_collection_by_coremedia_id = sgqlc.types.Field('EditorialCollection', graphql_name='editorialCollectionByCoremediaId', args=sgqlc.types.ArgDict((
        ('coremedia_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coremediaId', default=None)),
    ))
    )
    grouping = sgqlc.types.Field('Grouping', graphql_name='grouping', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='id', default=None)),
    ))
    )
    grouping_by_core_id = sgqlc.types.Field('Grouping', graphql_name='groupingByCoreId', args=sgqlc.types.ArgDict((
        ('core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coreId', default=None)),
    ))
    )
    image_binary = sgqlc.types.Field('ImageBinary', graphql_name='imageBinary', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='id', default=None)),
    ))
    )
    image_collection = sgqlc.types.Field('ImageCollection', graphql_name='imageCollection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='id', default=None)),
    ))
    )
    image = sgqlc.types.Field('Image', graphql_name='image', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='id', default=None)),
    ))
    )
    item = sgqlc.types.Field('Item', graphql_name='item', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    item_by_core_id = sgqlc.types.Field('Item', graphql_name='itemByCoreId', args=sgqlc.types.ArgDict((
        ('core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coreId', default=None)),
    ))
    )
    item_by_external_id = sgqlc.types.Field('Item', graphql_name='itemByExternalId', args=sgqlc.types.ArgDict((
        ('external_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='externalId', default=None)),
    ))
    )
    migration = sgqlc.types.Field('Migration', graphql_name='migration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            Int), graphql_name='id', default=None)),
    ))
    )
    migration_by_name = sgqlc.types.Field('Migration', graphql_name='migrationByName', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='name', default=None)),
    ))
    )
    organization_by_id = sgqlc.types.Field('Organization', graphql_name='organizationById', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            Int), graphql_name='id', default=None)),
    ))
    )
    organization = sgqlc.types.Field('Organization', graphql_name='organization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
    ))
    )
    organization_by_core_id = sgqlc.types.Field('Organization', graphql_name='organizationByCoreId', args=sgqlc.types.ArgDict((
        ('core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coreId', default=None)),
    ))
    )
    permanent_livestream = sgqlc.types.Field('PermanentLivestream', graphql_name='permanentLivestream', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='id', default=None)),
    ))
    )
    permanent_livestream_by_core_id = sgqlc.types.Field('PermanentLivestream', graphql_name='permanentLivestreamByCoreId', args=sgqlc.types.ArgDict((
        ('core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coreId', default=None)),
    ))
    )
    program_set = sgqlc.types.Field('ProgramSet', graphql_name='programSet', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    program_set_by_core_id = sgqlc.types.Field('ProgramSet', graphql_name='programSetByCoreId', args=sgqlc.types.ArgDict((
        ('core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coreId', default=None)),
    ))
    )
    publication_service = sgqlc.types.Field('PublicationService', graphql_name='publicationService', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
        ('source', sgqlc.types.Arg(SourceSystem, graphql_name='source', default=None)),
    ))
    )
    publication_service_by_title = sgqlc.types.Field('PublicationService', graphql_name='publicationServiceByTitle', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='title', default=None)),
    ))
    )
    publication_service_by_core_id = sgqlc.types.Field('PublicationService', graphql_name='publicationServiceByCoreId', args=sgqlc.types.ArgDict((
        ('core_id', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='coreId', default=None)),
    ))
    )
    transcript = sgqlc.types.Field('Transcript', graphql_name='transcript', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(sgqlc.types.non_null(
            Int), graphql_name='itemId', default=None)),
    ))
    )
    debug_show_groups = sgqlc.types.Field(DebugShowGroupsConnection, graphql_name='debugShowGroups', args=sgqlc.types.ArgDict((
        ('show_id', sgqlc.types.Arg(Int, graphql_name='showId', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    editorial_categories_by_ids = sgqlc.types.Field(EditorialCategoriesConnection, graphql_name='editorialCategoriesByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    editorial_categories_by_ids_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EditorialCategory')), graphql_name='editorialCategoriesByIdsList', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    editorial_collections_by_ids = sgqlc.types.Field(EditorialCollectionsConnection, graphql_name='editorialCollectionsByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    editorial_collections_by_ids_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EditorialCollection')), graphql_name='editorialCollectionsByIdsList', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    isnumeric = sgqlc.types.Field(Boolean, graphql_name='isnumeric', args=sgqlc.types.ArgDict((
        ('arg0', sgqlc.types.Arg(sgqlc.types.non_null(
            String), graphql_name='arg0', default=None)),
    ))
    )
    items_by_ids = sgqlc.types.Field(ItemsConnection, graphql_name='itemsByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('is_published', sgqlc.types.Arg(
            Boolean, graphql_name='isPublished', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    items_by_ids_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Item')), graphql_name='itemsByIdsList', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('is_published', sgqlc.types.Arg(
            Boolean, graphql_name='isPublished', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    jsonb_array = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='jsonbArray', args=sgqlc.types.ArgDict((
        ('arg0', sgqlc.types.Arg(JSON, graphql_name='arg0', default=None)),
    ))
    )
    program_sets_by_ids = sgqlc.types.Field(ProgramSetsConnection, graphql_name='programSetsByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    program_sets_by_ids_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProgramSet')), graphql_name='programSetsByIdsList', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(
            String), graphql_name='ids', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    shows_with_mapping = sgqlc.types.Field(ProgramSetsConnection, graphql_name='showsWithMapping', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    shows_with_mapping_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProgramSet')), graphql_name='showsWithMappingList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    audio_binary_by_node_id = sgqlc.types.Field('AudioBinary', graphql_name='audioBinaryByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    categories_to_program_set_by_node_id = sgqlc.types.Field('CategoriesToProgramSet', graphql_name='categoriesToProgramSetByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    concept_by_node_id = sgqlc.types.Field('Concept', graphql_name='conceptByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    config_by_node_id = sgqlc.types.Field('Config', graphql_name='configByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    editorial_category_by_node_id = sgqlc.types.Field('EditorialCategory', graphql_name='editorialCategoryByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    editorial_collection_by_node_id = sgqlc.types.Field('EditorialCollection', graphql_name='editorialCollectionByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    grouping_by_node_id = sgqlc.types.Field('Grouping', graphql_name='groupingByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    image_binary_by_node_id = sgqlc.types.Field('ImageBinary', graphql_name='imageBinaryByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    image_collection_by_node_id = sgqlc.types.Field('ImageCollection', graphql_name='imageCollectionByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    image_by_node_id = sgqlc.types.Field('Image', graphql_name='imageByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    item_by_node_id = sgqlc.types.Field('Item', graphql_name='itemByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    migration_by_node_id = sgqlc.types.Field('Migration', graphql_name='migrationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    organization_by_node_id = sgqlc.types.Field('Organization', graphql_name='organizationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    permanent_livestream_by_node_id = sgqlc.types.Field('PermanentLivestream', graphql_name='permanentLivestreamByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    program_set_by_node_id = sgqlc.types.Field('ProgramSet', graphql_name='programSetByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    publication_service_by_node_id = sgqlc.types.Field('PublicationService', graphql_name='publicationServiceByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    transcript_by_node_id = sgqlc.types.Field('Transcript', graphql_name='transcriptByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='nodeId', default=None)),
    ))
    )
    search = sgqlc.types.Field('SearchResult', graphql_name='search', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=24)),
        ('type', sgqlc.types.Arg(SearchType, graphql_name='type', default='All')),
        ('source', sgqlc.types.Arg(SourceSystem, graphql_name='source', default=None)),
    ))
    )
    homescreen = sgqlc.types.Field(Board, graphql_name='homescreen', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('source', sgqlc.types.Arg(SourceSystem, graphql_name='source', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
    ))
    )
    show = sgqlc.types.Field('ProgramSet', graphql_name='show', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    section = sgqlc.types.Field('Section', graphql_name='section', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    widget = sgqlc.types.Field('SophoraWidget', graphql_name='widget', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )
    widgets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SophoraWidget')), graphql_name='widgets', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(
            sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
    ))
    )
    compilations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SophoraCompilation')), graphql_name='compilations', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(
            sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
    ))
    )
    teasers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SophoraTeaser')), graphql_name='teasers', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(
            sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
    ))
    )
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(
            ID), graphql_name='id', default=None)),
    ))
    )


class QueueConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'QueueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'QueueInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class QueueEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('QueueInterface', graphql_name='node')


class QueueInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at',
                       'entries', 'modified_at', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    entries = sgqlc.types.Field(ItemConnection, graphql_name='entries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilterB, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(ItemSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    user = sgqlc.types.Field(EndUserInterface, graphql_name='user')


class QueuePayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_queue')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_queue = sgqlc.types.Field('Queue', graphql_name='changedQueue')


class RecommendationData(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('score', 'item')
    score = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name='score')
    item = sgqlc.types.Field('Item', graphql_name='item')


class RecommendationMeta(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('recommendation_id', 'algorithm',
                       'presentation_title', 'fallback_used', 'endpoint_url')
    recommendation_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='recommendationId')
    algorithm = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='algorithm')
    presentation_title = sgqlc.types.Field(
        String, graphql_name='presentationTitle')
    fallback_used = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name='fallbackUsed')
    endpoint_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='endpointUrl')


class RecommendationsConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('recommendation_id', 'algorithm', 'presentation_title',
                       'presentation_title_en', 'fallback_used', 'recommendations')
    recommendation_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='recommendationId')
    algorithm = sgqlc.types.Field(String, graphql_name='algorithm')
    presentation_title = sgqlc.types.Field(
        String, graphql_name='presentationTitle')
    presentation_title_en = sgqlc.types.Field(
        String, graphql_name='presentationTitleEn')
    fallback_used = sgqlc.types.Field(Boolean, graphql_name='fallbackUsed')
    recommendations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RecommendationData)), graphql_name='recommendations', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
    ))
    )


class SearchResult(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('items', 'program_sets',
                       'editorial_categories', 'editorial_collections', 'tracking')
    items = sgqlc.types.Field(ItemsSearchConnection, graphql_name='items')
    program_sets = sgqlc.types.Field(
        ProgramSetsSearchConnection, graphql_name='programSets')
    editorial_categories = sgqlc.types.Field(
        EditorialCategoriesConnection, graphql_name='editorialCategories')
    editorial_collections = sgqlc.types.Field(
        EditorialCollectionsConnection, graphql_name='editorialCollections')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')


class Section(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'title', 'layout', 'tracking',
                       'type', 'node_types', 'nodes')
    id = sgqlc.types.Field(ID, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    layout = sgqlc.types.Field(JSON, graphql_name='layout')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')
    type = sgqlc.types.Field(String, graphql_name='type')
    node_types = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(TeaserTypeATG)), graphql_name='nodeTypes')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Teaser')), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
    ))
    )


class SophoraCompilation(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'title', 'teaser_type', 'teasers')
    id = sgqlc.types.Field(ID, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    teaser_type = sgqlc.types.Field(String, graphql_name='teaserType')
    teasers = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null('SophoraTeaser')), graphql_name='teasers')


class StreamType(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('url', 'title', 'mimetype', 'row_id')
    url = sgqlc.types.Field(String, graphql_name='url')
    title = sgqlc.types.Field(String, graphql_name='title')
    mimetype = sgqlc.types.Field(String, graphql_name='mimetype')
    row_id = sgqlc.types.Field(String, graphql_name='rowId')


class SubscriptionListConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'SubscriptionListEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'SubscriptionListInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class SubscriptionListEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SubscriptionListInterface', graphql_name='node')


class SubscriptionListInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix', 'created_at',
                       'modified_at', 'program_sets', 'user')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    modified_at = sgqlc.types.Field(DateTime, graphql_name='modifiedAt')
    program_sets = sgqlc.types.Field(ProgramSetSubscriptionConnection, graphql_name='programSets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetSubscriptionFilterB,
         graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(ProgramSetSubscriptionSortOrder,
         graphql_name='orderBy', default=None)),
    ))
    )
    user = sgqlc.types.Field(EndUserInterface, graphql_name='user')


class SubscriptionListPayload(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('client_mutation_id', 'changed_subscription_list')
    client_mutation_id = sgqlc.types.Field(
        String, graphql_name='clientMutationId')
    changed_subscription_list = sgqlc.types.Field(
        'SubscriptionList', graphql_name='changedSubscriptionList')


class SystemConnection(sgqlc.types.relay.Connection):
    __schema__ = audiothek_schema
    __field_names__ = ('count', 'edges', 'nodes', 'page_info')
    count = sgqlc.types.Field(Int, graphql_name='count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(
        'SystemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(
        'SystemInterface'), graphql_name='nodes')
    page_info = sgqlc.types.Field(
        sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class SystemEdge(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SystemInterface', graphql_name='node')


class SystemInterface(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'base_id_prefix')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    base_id_prefix = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='baseIdPrefix')


class Teaser(sgqlc.types.Interface):
    __schema__ = audiothek_schema
    __field_names__ = ('id', 'title', 'synopsis', 'image', 'url',
                       'sharing_url', 'path', 'number_of_elements', 'tracking')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='title')
    synopsis = sgqlc.types.Field(String, graphql_name='synopsis')
    image = sgqlc.types.Field(ImageType, graphql_name='image')
    url = sgqlc.types.Field(String, graphql_name='url', args=sgqlc.types.ArgDict((
        ('variant', sgqlc.types.Arg(UrlVariant, graphql_name='variant', default=None)),
    ))
    )
    sharing_url = sgqlc.types.Field(URL, graphql_name='sharingUrl')
    path = sgqlc.types.Field(String, graphql_name='path')
    number_of_elements = sgqlc.types.Field(
        Int, graphql_name='numberOfElements')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')


class _Service(sgqlc.types.Type):
    __schema__ = audiothek_schema
    __field_names__ = ()


class AudioBinary(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'core_document', 'href', 'available_from', 'available_to', 'title',
                       'adaptivity', 'distribution_type', 'packaging', 'audio_channel', 'audio_bitrate', 'audio_codec')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    href = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='href')
    available_from = sgqlc.types.Field(Datetime, graphql_name='availableFrom')
    available_to = sgqlc.types.Field(Datetime, graphql_name='availableTo')
    title = sgqlc.types.Field(String, graphql_name='title')
    adaptivity = sgqlc.types.Field(String, graphql_name='adaptivity')
    distribution_type = sgqlc.types.Field(
        String, graphql_name='distributionType')
    packaging = sgqlc.types.Field(String, graphql_name='packaging')
    audio_channel = sgqlc.types.Field(String, graphql_name='audioChannel')
    audio_bitrate = sgqlc.types.Field(Int, graphql_name='audioBitrate')
    audio_codec = sgqlc.types.Field(String, graphql_name='audioCodec')


class Bookmark(sgqlc.types.Type, BookmarkInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class BookmarkList(sgqlc.types.Type, BookmarkListInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class CategoriesToProgramSet(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('program_set_core_id', 'category_sophora_id',
                       'program_set_core', 'category_sophora')
    program_set_core_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='programSetCoreId')
    category_sophora_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='categorySophoraId')
    program_set_core = sgqlc.types.Field(
        'ProgramSet', graphql_name='programSetCore')
    category_sophora = sgqlc.types.Field(
        'EditorialCategory', graphql_name='categorySophora')


class Concept(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('item_id', 'concept_source',
                       'data', 'last_updated_at', 'item')
    item_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='itemId')
    concept_source = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='conceptSource')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    last_updated_at = sgqlc.types.Field(
        sgqlc.types.non_null(Datetime), graphql_name='lastUpdatedAt')
    item = sgqlc.types.Field('Item', graphql_name='item')


class Config(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('key', 'value', 'updated_at', 'updated_by')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(JSON, graphql_name='value')
    updated_at = sgqlc.types.Field(Datetime, graphql_name='updatedAt')
    updated_by = sgqlc.types.Field(String, graphql_name='updatedBy')


class EditorialCategory(sgqlc.types.Type, Node, Teaser):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'sophora_id', 'order', 'items', 'categories_to_program_sets_by_category_sophora_id',
                       'categories_to_program_sets_by_category_sophora_id_list', 'recent_items', 'recent_items_list', 'program_sets', 'program_sets_list')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    sophora_id = sgqlc.types.Field(String, graphql_name='sophoraId')
    order = sgqlc.types.Field(Int, graphql_name='order')
    items = sgqlc.types.Field(sgqlc.types.non_null(ItemsConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ItemsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    categories_to_program_sets_by_category_sophora_id = sgqlc.types.Field(sgqlc.types.non_null(CategoriesToProgramSetsConnection), graphql_name='categoriesToProgramSetsByCategorySophoraId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            CategoriesToProgramSetsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(CategoriesToProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CategoriesToProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    categories_to_program_sets_by_category_sophora_id_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CategoriesToProgramSet))), graphql_name='categoriesToProgramSetsByCategorySophoraIdList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            CategoriesToProgramSetsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(CategoriesToProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CategoriesToProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    recent_items = sgqlc.types.Field(sgqlc.types.non_null(ItemsConnection), graphql_name='recentItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(
            sgqlc.types.non_null(ItemsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    recent_items_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Item')), graphql_name='recentItemsList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(
            sgqlc.types.non_null(ItemsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    program_sets = sgqlc.types.Field(sgqlc.types.non_null(EditorialCategoryProgramSetsManyToManyConnection), graphql_name='programSets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ProgramSetsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    program_sets_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProgramSet'))), graphql_name='programSetsList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ProgramSetsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(ProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )


class EditorialCollection(sgqlc.types.Type, Node, Teaser):
    __schema__ = audiothek_schema
    __field_names__ = ('sophora_id', 'broadcast_duration',
                       'coremedia_id', 'row_id', 'summary', 'items')
    sophora_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='sophoraId')
    broadcast_duration = sgqlc.types.Field(
        Int, graphql_name='broadcastDuration')
    coremedia_id = sgqlc.types.Field(String, graphql_name='coremediaId')
    row_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='rowId')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    items = sgqlc.types.Field(sgqlc.types.non_null(ItemsConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
    ))
    )


class EditorialCollectionSection(sgqlc.types.Type, Section):
    __schema__ = audiothek_schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field(String, graphql_name='key')


class EndUser(sgqlc.types.Type, EndUserInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class EventLivestream(sgqlc.types.Type, Teaser, CoreTeaser):
    __schema__ = audiothek_schema
    __field_names__ = ('core_id', 'core_type', 'row_id', 'external_ids', 'publish_date', 'broadcast_start',
                       'duration', 'program_set', 'summary', 'description', 'audios', 'audio_list', 'core_document', 'core')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_type = sgqlc.types.Field(
        sgqlc.types.non_null(ItemType), graphql_name='coreType')
    row_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rowId')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    publish_date = sgqlc.types.Field(
        sgqlc.types.non_null(Datetime), graphql_name='publishDate')
    broadcast_start = sgqlc.types.Field(
        sgqlc.types.non_null(Datetime), graphql_name='broadcastStart')
    duration = sgqlc.types.Field(Int, graphql_name='duration', args=sgqlc.types.ArgDict((
        ('variant', sgqlc.types.Arg(DurationVariant,
         graphql_name='variant', default=None)),
    ))
    )
    program_set = sgqlc.types.Field('ProgramSet', graphql_name='programSet')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    description = sgqlc.types.Field(HTML, graphql_name='description')
    audios = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(AssetType)), graphql_name='audios')
    audio_list = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(AudioBinary)), graphql_name='audioList')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    core = sgqlc.types.Field(JSON, graphql_name='core', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(String, graphql_name='filter', default=None)),
        ('key', sgqlc.types.Arg(String, graphql_name='key', default=None)),
    ))
    )


class FilterCompilationSection(sgqlc.types.Type, Section):
    __schema__ = audiothek_schema
    __field_names__ = ('meta',)
    meta = sgqlc.types.Field(JSON, graphql_name='meta')


class Grouping(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'programset_id', 'title', 'item_label', 'type', 'count', 'season_number',
                       'last_modified', 'core_id', 'core_document', 'show_id', 'programset', 'show', 'items_by_group_id')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    programset_id = sgqlc.types.Field(Int, graphql_name='programsetId')
    title = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='title')
    item_label = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='itemLabel')
    type = sgqlc.types.Field(Grouptype, graphql_name='type')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    season_number = sgqlc.types.Field(Int, graphql_name='seasonNumber')
    last_modified = sgqlc.types.Field(
        sgqlc.types.non_null(Datetime), graphql_name='lastModified')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    show_id = sgqlc.types.Field(String, graphql_name='showId')
    programset = sgqlc.types.Field('ProgramSet', graphql_name='programset')
    show = sgqlc.types.Field('ProgramSet', graphql_name='show')
    items_by_group_id = sgqlc.types.Field(sgqlc.types.non_null(ItemsConnection), graphql_name='itemsByGroupId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ItemsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )


class HistoryEntry(sgqlc.types.Type, HistoryEntryInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class Image(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'core_document', 'title',
                       'producer_name', 'image_binary_id')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    title = sgqlc.types.Field(String, graphql_name='title')
    producer_name = sgqlc.types.Field(String, graphql_name='producerName')
    image_binary_id = sgqlc.types.Field(String, graphql_name='imageBinaryId')


class ImageBinary(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'core_document', 'file_location',
                       'media_type', 'width', 'height', 'aspect_ratio')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    file_location = sgqlc.types.Field(String, graphql_name='fileLocation')
    media_type = sgqlc.types.Field(String, graphql_name='mediaType')
    width = sgqlc.types.Field(Int, graphql_name='width')
    height = sgqlc.types.Field(Int, graphql_name='height')
    aspect_ratio = sgqlc.types.Field(String, graphql_name='aspectRatio')


class ImageCollection(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'core_document', 'image_ids')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    image_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='imageIds')


class Item(sgqlc.types.Type, Node, Teaser, CoreTeaser):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'publish_date', 'codex_pending', 'is_published', 'program_set_id', 'title_without_number', 'group_id', 'episode_number', 'max_group_number', 'codex_last_published', 'external_ids', 'editorial_category_id', 'core_id', 'item_type', 'core_document', 'external_id', 'image_collection_id', 'show_id', 'first_publish_date', 'audio_binary_id',
                       'status', 'program_set', 'group', 'editorial_category', 'concepts', 'transcript', 'audio_list', 'editorial_categories', 'editorial_categories_list', 'has_core_document', 'has_synthetic_row_id', 'images', 'images_list', 'next_episode', 'title_clean', 'summary', 'description', 'duration', 'grouping', 'audios', 'keywords', 'subjects', 'recommendations', 'core')
    row_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rowId')
    publish_date = sgqlc.types.Field(
        sgqlc.types.non_null(Datetime), graphql_name='publishDate')
    codex_pending = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name='codexPending')
    is_published = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    program_set_id = sgqlc.types.Field(Int, graphql_name='programSetId')
    title_without_number = sgqlc.types.Field(
        String, graphql_name='titleWithoutNumber')
    group_id = sgqlc.types.Field(String, graphql_name='groupId')
    episode_number = sgqlc.types.Field(Int, graphql_name='episodeNumber')
    max_group_number = sgqlc.types.Field(Int, graphql_name='maxGroupNumber')
    codex_last_published = sgqlc.types.Field(
        BigInt, graphql_name='codexLastPublished')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    editorial_category_id = sgqlc.types.Field(
        String, graphql_name='editorialCategoryId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    item_type = sgqlc.types.Field(
        sgqlc.types.non_null(ItemType), graphql_name='itemType')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    show_id = sgqlc.types.Field(String, graphql_name='showId')
    first_publish_date = sgqlc.types.Field(
        Datetime, graphql_name='firstPublishDate')
    audio_binary_id = sgqlc.types.Field(String, graphql_name='audioBinaryId')
    status = sgqlc.types.Field(Status, graphql_name='status')
    program_set = sgqlc.types.Field('ProgramSet', graphql_name='programSet')
    group = sgqlc.types.Field(Grouping, graphql_name='group')
    editorial_category = sgqlc.types.Field(
        EditorialCategory, graphql_name='editorialCategory')
    concepts = sgqlc.types.Field(sgqlc.types.non_null(ConceptsConnection), graphql_name='concepts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ConceptsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ConceptCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ConceptFilter, graphql_name='filter', default=None)),
    ))
    )
    transcript = sgqlc.types.Field('Transcript', graphql_name='transcript')
    audio_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AudioBinary)), graphql_name='audioList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    editorial_categories = sgqlc.types.Field(sgqlc.types.non_null(EditorialCategoriesConnection), graphql_name='editorialCategories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            EditorialCategoriesOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(EditorialCategoryCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(EditorialCategoryFilter,
         graphql_name='filter', default=None)),
    ))
    )
    editorial_categories_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EditorialCategory)), graphql_name='editorialCategoriesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            EditorialCategoriesOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(EditorialCategoryCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(EditorialCategoryFilter,
         graphql_name='filter', default=None)),
    ))
    )
    has_core_document = sgqlc.types.Field(
        Boolean, graphql_name='hasCoreDocument')
    has_synthetic_row_id = sgqlc.types.Field(
        Boolean, graphql_name='hasSyntheticRowId')
    images = sgqlc.types.Field(sgqlc.types.non_null(ImagesCollectionsBinariesViewsConnection), graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    images_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImagesCollectionsBinariesView)), graphql_name='imagesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    next_episode = sgqlc.types.Field('Item', graphql_name='nextEpisode')
    title_clean = sgqlc.types.Field(String, graphql_name='titleClean')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    description = sgqlc.types.Field(HTML, graphql_name='description')
    duration = sgqlc.types.Field(Int, graphql_name='duration', args=sgqlc.types.ArgDict((
        ('variant', sgqlc.types.Arg(DurationVariant,
         graphql_name='variant', default=None)),
    ))
    )
    grouping = sgqlc.types.Field(JSON, graphql_name='grouping')
    audios = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(AssetType)), graphql_name='audios')
    keywords = sgqlc.types.Field(JSON, graphql_name='keywords')
    subjects = sgqlc.types.Field(JSON, graphql_name='subjects')
    recommendations = sgqlc.types.Field(RecommendationsConnection, graphql_name='recommendations', args=sgqlc.types.ArgDict((
        ('variant', sgqlc.types.Arg(sgqlc.types.non_null(
            ItemRecVariant), graphql_name='variant', default=None)),
    ))
    )
    core = sgqlc.types.Field(JSON, graphql_name='core', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(String, graphql_name='filter', default=None)),
        ('key', sgqlc.types.Arg(String, graphql_name='key', default=None)),
    ))
    )


class ItemSection(sgqlc.types.Type, Section):
    __schema__ = audiothek_schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field(String, graphql_name='key')


class Migration(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'name', 'hash', 'executed_at')
    row_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rowId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hash')
    executed_at = sgqlc.types.Field(Datetime, graphql_name='executedAt')


class Organization(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'name', 'core_id', 'core_document', 'order', 'title', 'publication_services_by_organization_name',
                       'images', 'images_list', 'publication_services', 'sharing_url', 'path', 'url', 'tracking', '_links', 'image')
    row_id = sgqlc.types.Field(Int, graphql_name='rowId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    order = sgqlc.types.Field(Int, graphql_name='order')
    title = sgqlc.types.Field(String, graphql_name='title')
    publication_services_by_organization_name = sgqlc.types.Field(sgqlc.types.non_null(PublicationServicesConnection), graphql_name='publicationServicesByOrganizationName', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            PublicationServicesOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(PublicationServiceCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(PublicationServiceFilter,
         graphql_name='filter', default=None)),
    ))
    )
    images = sgqlc.types.Field(sgqlc.types.non_null(ImagesCollectionsBinariesViewsConnection), graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    images_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImagesCollectionsBinariesView)), graphql_name='imagesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    publication_services = sgqlc.types.Field(sgqlc.types.non_null(PublicationServicesConnection), graphql_name='publicationServices', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            PublicationServicesOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(PublicationServiceCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(PublicationServiceFilter,
         graphql_name='filter', default=None)),
    ))
    )
    sharing_url = sgqlc.types.Field(URL, graphql_name='sharingUrl')
    path = sgqlc.types.Field(String, graphql_name='path')
    url = sgqlc.types.Field(String, graphql_name='url', args=sgqlc.types.ArgDict((
        ('variant', sgqlc.types.Arg(UrlVariant, graphql_name='variant', default=None)),
    ))
    )
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')
    _links = sgqlc.types.Field(JSON, graphql_name='_links')
    image = sgqlc.types.Field(ImageType, graphql_name='image', args=sgqlc.types.ArgDict((
        ('aspect', sgqlc.types.Arg(AspectRatio, graphql_name='aspect', default=None)),
    ))
    )


class PermanentLivestream(sgqlc.types.Type, Node, CoreTeaser):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'core_id', 'external_ids', 'publication_service_id', 'image', 'core_document', 'tracking', 'audios', 'image_collection_id',
                       'audio_binary_id', 'publisher_core_id', 'order', 'publication_service', 'audio_list', 'images', 'images_list', 'summary', 'description')
    row_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='rowId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    publication_service_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='publicationServiceId')
    image = sgqlc.types.Field(ImageType, graphql_name='image')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    tracking = sgqlc.types.Field(JSON, graphql_name='tracking')
    audios = sgqlc.types.Field(sgqlc.types.list_of(
        sgqlc.types.non_null(StreamType)), graphql_name='audios')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    audio_binary_id = sgqlc.types.Field(String, graphql_name='audioBinaryId')
    publisher_core_id = sgqlc.types.Field(
        String, graphql_name='publisherCoreId')
    order = sgqlc.types.Field(Int, graphql_name='order')
    publication_service = sgqlc.types.Field(
        'PublicationService', graphql_name='publicationService')
    audio_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AudioBinary)), graphql_name='audioList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    images = sgqlc.types.Field(sgqlc.types.non_null(ImagesCollectionsBinariesViewsConnection), graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    images_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImagesCollectionsBinariesView)), graphql_name='imagesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    summary = sgqlc.types.Field(String, graphql_name='summary')
    description = sgqlc.types.Field(HTML, graphql_name='description')


class Playlist(sgqlc.types.Type, PlaylistInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class ProgramSet(sgqlc.types.Type, Node, Teaser, CoreTeaser):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'publication_service_id', 'editorial_category_id', 'core_id', 'core_document', 'image_collection_id', 'last_item_modified', 'last_item_added', 'publication_service', 'items', 'groupings_by_programset_id', 'groupings_by_show_id',
                       'categories_to_program_sets_by_program_set_core_id', 'categories_to_program_sets_by_program_set_core_id_list', 'editorial_category', 'images', 'images_list', 'editorial_categories', 'editorial_categories_list', 'show_type', 'description', '_links', 'core')
    row_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rowId')
    publication_service_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='publicationServiceId')
    editorial_category_id = sgqlc.types.Field(
        String, graphql_name='editorialCategoryId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    image_collection_id = sgqlc.types.Field(
        String, graphql_name='imageCollectionId')
    last_item_modified = sgqlc.types.Field(
        Datetime, graphql_name='lastItemModified')
    last_item_added = sgqlc.types.Field(Datetime, graphql_name='lastItemAdded')
    publication_service = sgqlc.types.Field(
        'PublicationService', graphql_name='publicationService')
    items = sgqlc.types.Field(sgqlc.types.non_null(ItemsConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ItemsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ItemCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ItemFilter, graphql_name='filter', default=None)),
    ))
    )
    groupings_by_programset_id = sgqlc.types.Field(sgqlc.types.non_null(GroupingsConnection), graphql_name='groupingsByProgramsetId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            GroupingsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(GroupingCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(GroupingFilter,
         graphql_name='filter', default=None)),
    ))
    )
    groupings_by_show_id = sgqlc.types.Field(sgqlc.types.non_null(GroupingsConnection), graphql_name='groupingsByShowId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            GroupingsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(GroupingCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(GroupingFilter,
         graphql_name='filter', default=None)),
    ))
    )
    categories_to_program_sets_by_program_set_core_id = sgqlc.types.Field(sgqlc.types.non_null(CategoriesToProgramSetsConnection), graphql_name='categoriesToProgramSetsByProgramSetCoreId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            CategoriesToProgramSetsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(CategoriesToProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CategoriesToProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    categories_to_program_sets_by_program_set_core_id_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CategoriesToProgramSet))), graphql_name='categoriesToProgramSetsByProgramSetCoreIdList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            CategoriesToProgramSetsOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(CategoriesToProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CategoriesToProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    editorial_category = sgqlc.types.Field(
        EditorialCategory, graphql_name='editorialCategory')
    images = sgqlc.types.Field(sgqlc.types.non_null(ImagesCollectionsBinariesViewsConnection), graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    images_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImagesCollectionsBinariesView)), graphql_name='imagesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    editorial_categories = sgqlc.types.Field(sgqlc.types.non_null(ProgramSetEditorialCategoriesManyToManyConnection), graphql_name='editorialCategories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            EditorialCategoriesOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(EditorialCategoryCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(EditorialCategoryFilter,
         graphql_name='filter', default=None)),
    ))
    )
    editorial_categories_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EditorialCategory))), graphql_name='editorialCategoriesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            EditorialCategoriesOrderBy)), graphql_name='orderBy', default=None)),
        ('condition', sgqlc.types.Arg(EditorialCategoryCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(EditorialCategoryFilter,
         graphql_name='filter', default=None)),
    ))
    )
    show_type = sgqlc.types.Field(
        sgqlc.types.non_null(ShowType), graphql_name='showType')
    description = sgqlc.types.Field(HTML, graphql_name='description')
    _links = sgqlc.types.Field(JSON, graphql_name='_links')
    core = sgqlc.types.Field(JSON, graphql_name='core', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(String, graphql_name='filter', default=None)),
        ('key', sgqlc.types.Arg(String, graphql_name='key', default=None)),
    ))
    )


class ProgramSetSection(sgqlc.types.Type, Section):
    __schema__ = audiothek_schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field(String, graphql_name='key')


class ProgramSetSubscription(sgqlc.types.Type, ProgramSetSubscriptionInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class Property(sgqlc.types.Type, PropertyInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class PublicationService(sgqlc.types.Type, Node, Teaser, CoreTeaser):
    __schema__ = audiothek_schema
    __field_names__ = ('row_id', 'organization_name', 'genre', 'branding_color', 'dvb_service_id', 'core_id', 'core_document', 'external_ids',
                       'homepage_url', 'order', 'parent_service_id', 'organization', 'program_sets', 'permanent_livestreams', 'images', 'images_list', '_links')
    row_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rowId')
    organization_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name='organizationName')
    genre = sgqlc.types.Field(String, graphql_name='genre')
    branding_color = sgqlc.types.Field(String, graphql_name='brandingColor')
    dvb_service_id = sgqlc.types.Field(Int, graphql_name='dvbServiceId')
    core_id = sgqlc.types.Field(String, graphql_name='coreId')
    core_document = sgqlc.types.Field(JSON, graphql_name='coreDocument')
    external_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name='externalIds')
    homepage_url = sgqlc.types.Field(String, graphql_name='homepageUrl')
    order = sgqlc.types.Field(Int, graphql_name='order')
    parent_service_id = sgqlc.types.Field(
        String, graphql_name='parentServiceId')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    program_sets = sgqlc.types.Field(sgqlc.types.non_null(ProgramSetsConnection), graphql_name='programSets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            ProgramSetsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ProgramSetCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProgramSetFilter,
         graphql_name='filter', default=None)),
    ))
    )
    permanent_livestreams = sgqlc.types.Field(sgqlc.types.non_null(PermanentLivestreamsConnection), graphql_name='permanentLivestreams', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(
            PermanentLivestreamsOrderBy)), graphql_name='orderBy', default=('ORDER_ASC',))),
        ('condition', sgqlc.types.Arg(PermanentLivestreamCondition,
         graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(PermanentLivestreamFilter,
         graphql_name='filter', default=None)),
    ))
    )
    images = sgqlc.types.Field(sgqlc.types.non_null(ImagesCollectionsBinariesViewsConnection), graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
    ))
    )
    images_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImagesCollectionsBinariesView)), graphql_name='imagesList', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
    ))
    )
    _links = sgqlc.types.Field(JSON, graphql_name='_links')


class PublishableThing(sgqlc.types.Type, PublishableThingInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class Queue(sgqlc.types.Type, QueueInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class RecommendationSection(sgqlc.types.Type, Section):
    __schema__ = audiothek_schema
    __field_names__ = ('meta',)
    meta = sgqlc.types.Field(RecommendationMeta, graphql_name='meta')


class SophoraTeaser(sgqlc.types.Type, Teaser):
    __schema__ = audiothek_schema
    __field_names__ = ('sophora_type', 'sophora_title',
                       'type', 'content_id', 'node')
    sophora_type = sgqlc.types.Field(String, graphql_name='sophoraType')
    sophora_title = sgqlc.types.Field(String, graphql_name='sophoraTitle')
    type = sgqlc.types.Field(String, graphql_name='type')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    node = sgqlc.types.Field(Teaser, graphql_name='node')


class SophoraWidget(sgqlc.types.Type, Section):
    __schema__ = audiothek_schema
    __field_names__ = ('key', 'display_variant', 'size',
                       'title_visible', 'compilation')
    key = sgqlc.types.Field(String, graphql_name='key')
    display_variant = sgqlc.types.Field(
        WidgetDisplayVariant, graphql_name='displayVariant')
    size = sgqlc.types.Field(String, graphql_name='size')
    title_visible = sgqlc.types.Field(Boolean, graphql_name='titleVisible')
    compilation = sgqlc.types.Field(
        SophoraCompilation, graphql_name='compilation')


class SubscriptionList(sgqlc.types.Type, SubscriptionListInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class System(sgqlc.types.Type, SystemInterface):
    __schema__ = audiothek_schema
    __field_names__ = ()


class Transcript(sgqlc.types.Type, Node):
    __schema__ = audiothek_schema
    __field_names__ = ('item_id', 'xml', 'data',
                       'last_updated_at', 'item', 'start', 'end', 'text')
    item_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name='itemId')
    xml = sgqlc.types.Field(String, graphql_name='xml')
    data = sgqlc.types.Field(JSON, graphql_name='data')
    last_updated_at = sgqlc.types.Field(
        sgqlc.types.non_null(Datetime), graphql_name='lastUpdatedAt')
    item = sgqlc.types.Field(Item, graphql_name='item')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')
    text = sgqlc.types.Field(String, graphql_name='text')


########################################################################
# Unions
########################################################################
class _Entity(sgqlc.types.Union):
    __schema__ = audiothek_schema
    __types__ = (Config, EditorialCategory, Item, ProgramSet, PublicationService, Organization, PermanentLivestream, AudioBinary,
                 Grouping, CategoriesToProgramSet, Concept, Transcript, EditorialCollection, Migration, ImageBinary, ImageCollection, Image)


########################################################################
# Schema Entry Points
########################################################################
audiothek_schema.query_type = Query
audiothek_schema.mutation_type = Mutation
audiothek_schema.subscription_type = None
