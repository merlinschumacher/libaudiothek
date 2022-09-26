# from sgqlc.endpoint.http import HTTPEndpoint

# url = 'https://api.ardaudiothek.de'

# query = 'query { ... }'
# variables = {'term': 'kalk und welk'}

# endpoint = HTTPEndpoint(url)
# data = endpoint(query, variables)

from sgqlc.operation import Operation
from audiothek_schema import audiothek_schema as schema
from sgqlc.endpoint.http import HTTPEndpoint

op = Operation(schema.query_type)

url = 'https://api.ardaudiothek.de'
endpoint = HTTPEndpoint(url)
search = op.search(query="Kalk und Welk")
print(search)

search.items()

print(op)

data = endpoint(op)
repo = (op + data).items()
for result in repo.items.nodes():
    print(result)
