# libaudiothek

This is a python library to access the ARD Audiothek API. The ARD Audiothek is a service of the German public broadcaster ARD. It provides a large collection of audio files, mostly radio shows and podcasts. It's API is very complex and this library is a wrapper around it. It provides a simple interface to access the audio files.

## Supported features

* Search for audio files

## Usage

### Search for audio files

```python
from libaudiothek import Audiothek

# create an instance of the Audiothek class
audiothek = Audiothek()
# search for items with the keyword "Krimi"
result = audiothek.search("Krimi")

# print the result
print(result.items)
print(result.items[0])

print(result.program_sets)
print(result.program_sets[0])
```
