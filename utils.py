
#|%%--%%| <f0GEGDeLRe|bNvqfQkX7p>
r"""°°°
# Utils

Connect LLMs to tools and other sources of knowledge

- Text Splitter
- Embeddigs:
    - Return embeddigns (list of floats)
- Vectorstores
    - Datastores to store embeddings of documents in vector form.
    - Expose methods for passing in a string and retrieve similar document
- Python Repl
- Bash
- Requests Wrapper (requests lib)
- Search

## Generic Utilities

### Bash
°°°"""
#|%%--%%| <bNvqfQkX7p|ph5kvpzBNj>

from langchain.utilities import BashProcess

bash = BashProcess()
print(bash.run("ls"))

#|%%--%%| <ph5kvpzBNj|4qBrDqHb3v>

#TODO: rest of utils
