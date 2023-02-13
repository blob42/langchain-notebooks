r"""°°°
# Prompt templates
[see](https://langchain.readthedocs.io/en/latest/modules/prompts/getting_started.html)
°°°"""
# |%%--%%| <IagIXdFJ76|5rNpKSE97a>

from langchain import PromptTemplate
import pprint as pp

template = """
I want you to act as a naming consultant for new companies.

Here are some examples of good company names:

- search engine, Google
- social media, Facebook
- video sharing, YouTube

The name should be short, catchy and easy to remember.

What is a good name for a company that makes {product}?
"""

prompt = PromptTemplate(
        input_variables=["product"],
        template=template,
        )

pp.pp(prompt.format(product='cookie'))

# |%%--%%| <5rNpKSE97a|UH7UDNwwOT>

# without inputs
no_input_prompt = PromptTemplate(input_variables=[],
                                 template="tell me a joke.")
no_input_prompt.format()

# with inputs
multi_input_prompt = PromptTemplate(
        input_variables=["adjective", "content"],
        template="tell me a {adjective} joke about {content}." 
        )
multi_input_prompt.format(adjective="funny", content="bats")

# |%%--%%| <UH7UDNwwOT|m4HfAhbN4T>
r"""°°°
## Loading prompt templates from LangChainHub 
°°°"""
# |%%--%%| <m4HfAhbN4T|6sAHvM0Vrt>

from langchain.prompts import load_prompt

prompt=load_prompt("lc://prompts/conversation/prompt.json")
#NOTE: is there a helper to quickly build a history ? 
print(prompt.format(history="", input="what is 1 + 1?"))

# |%%--%%| <6sAHvM0Vrt|u2xOTHeA5E>
r"""°°°
## Pass few shot examples to prompt template
°°°"""
# |%%--%%| <u2xOTHeA5E|KO5IXCuzjw>

from langchain import FewShotPromptTemplate

# create a list of few shot examples
examples = [
        {"word": "happy", "antonym": "sad"},
        {"word": "tall", "antonym": "short"},
        ]

# next e specify a template for format the examples
# we use PromptTemplate class
example_formatter_template = """
Word: {word}
Antonym: {antonym}
"""
example_pr = PromptTemplate(
        input_variables=["word", "antonym"],
        template=example_formatter_template,
        )

# now we can use FewShotPromptTemplate
few_shot_prompt = FewShotPromptTemplate(
        # examples we want to insert in prompt
        examples=examples,
        # how we want examples to be formatted in prompt
        example_prompt=example_pr,
        # The prefix is some text that goes before the examples in the prompt.
        # Usually, this consists of intructions.
        prefix="Give the antonym of every input",
        #The suffix is some text that goes after the examples in the prompt.
        suffix="Word: {input}\nAntonym:",
        # The input variables are the variables that the overall prompt expects.
        input_variables=["input"],
        # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
        example_separator="\n\n",
        )
# generate few shot prompt using input
print(few_shot_prompt.format(input="fast"))

# |%%--%%| <KO5IXCuzjw|fV1qxeDncc>
r"""°°°
## Select examples from prompt template

- for a large number of exaamples use ExampleSelector to select a subset of
  most informative ones for language model.
- LengthBasedExampleSelector selects examples based on length of input.
  practical to to construct prompt that do not extend over context window
  based on input length
°°°"""
# |%%--%%| <fV1qxeDncc|uuIdYaJ4wD>

from langchain.prompts.example_selector import LengthBasedExampleSelector

#These are a lot of examples of a pretend task of creating antonyms.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
    {"word": "energetic", "antonym": "lethargic"},
    {"word": "sunny", "antonym": "gloomy"},
    {"word": "windy", "antonym": "calm"},
]

example_selector = LengthBasedExampleSelector(
        examples=examples,
        # This is the PromptTemplate being used to format the examples.
        example_prompt=example_pr,
        # This is the maximum length that the formatted examples should be.
        # Length is measured by the get_text_length function below.
        max_length=30,
        )

# We can now use the `example_selector` to create a `FewShotPromptTemplate`.
dynamic_prompt = FewShotPromptTemplate(
    # We provide an ExampleSelector instead of examples.
    example_selector=example_selector,
    example_prompt=example_pr,
    prefix="Give the antonym of every input",
    suffix="Word: {input}\nAntonym:",
    input_variables=["input"],
    example_separator="\n\n",
)

# We can now generate a prompt using the `format` method.
print(dynamic_prompt.format(input="big"))

print("----------")

# In contrast, if we provide a very long input, the LengthBasedExampleSelector
# will select fewer examples to include in the prompt.
long_string = "big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"
print(dynamic_prompt.format(input=long_string))
