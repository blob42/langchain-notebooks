r"""°°°
# Document Loaders

- loading text from local sources
- main driver is `Unstructured` python package

## Key Concepts

### Document

container class for document information. contains:
    - page_content
    - metadata

### Loader

base class to load documents. exposes:
    - load() -> Document


## Setup Unstructured
- host dependencies
    - poppler: PDF rendering library
- Python deps:
    - Pillow: imaging library
°°°"""
#|%%--%%| <4yTe29l2Ya|srwyN0cVES>

# %pip install pillow (already installed)
%pip install -q unstructured[local-inference]

#|%%--%%| <srwyN0cVES|cbFv0eSeXq>

docs_dir="unstructured-examples"
!mkdir -p $docs_dir
!wget  https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/example-docs/example-10k.html -P $docs_dir
!wget  https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/example-docs/layout-parser-paper.pdf -P $docs_dir


#|%%--%%| <cbFv0eSeXq|U633RkWjYq>
r"""°°°
[repo link](https://github.com/Unstructured-IO/unstructured#coffee-getting-started)
The easiest way to parse a document in unstructured is to use the partition brick. If you use partition brick, unstructured will detect the file type and route it to the appropriate file-specific partitioning brick. If you are using the partition brick, ensure you first install libmagic using the instructions outlined here partition will always apply the default arguments. If you need advanced features, use a document-specific brick. The partition brick currently works for .txt, .docx, .pptx, .jpg, .png, .eml, .html, and .pdf documents.

Requires detectonr2 inference (cuda ?)
°°°"""
#|%%--%%| <U633RkWjYq|FJaYuFeL0U>

docs_dir="unstructured-examples"
#|%%--%%| <FJaYuFeL0U|9MKaXz7Bi4>

#NOTE: needs inference with facebook's detectron2

# from unstructured.partition.auto import partition

# elements = partition(docs_dir + "/layout-parser-paper.pdf")


#|%%--%%| <9MKaXz7Bi4|X4mTVZAzcD>
r"""°°°
## Unstructured Langchain FileLoader

Requires detectron2

°°°"""
#|%%--%%| <X4mTVZAzcD|9k0eAtsfvh>

from langchain.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("./unstructured-examples/layout-parser-paper.pdf")

docs = loader.load()
#|%%--%%| <9k0eAtsfvh|1lKP9jNDd4>

