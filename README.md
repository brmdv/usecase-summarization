# Text summarization with NLP

The goal of this project, on behalf of [Algorhythm](https://algorhythm.be/), is to explore the current state of Natural Language Processing for text summarization. There is also a [webapp](https://brams-book-summarizer.herokuapp.com) to showcase some results ([repository](https://github.com/brmdv/summarization-webapp/)).

## Technical details

### Data sources

The methods are tested on [books](https://www.gutenberg.org/) that are in the public domain, downloaded in HTML format from **Project Gutenberg**.  

### Deliverables

- Project Gutenberg book parser [book_reading.py](book_reading.py)  to extract paragraphs from selected chapters.
- Simple Flask **webapp** to [try out](https://brams-book-summarizer.herokuapp.com) some results.
- Some Jupyter notebooks where I explored the libraries and models, in _exploration/_.

### Dependancies

This project is mainly built on [HuggingFace's](https://huggingface.co/) [transformers](https://github.com/huggingface/transformers) library, as it provides an easy way into the newest pre-trained models. I opted for the Tensorflow backend, as it is already installed on [Google Collab](), so that I could easily upscale bigger test to the free resources provided by Google. For the NER I used [SpaCy](https://www.spacy.io/). 

## Notable conclusions

#### Automatic text summarization is hard

Without the full life experience of a human being behind it, all algorithms—even the most state-of-the-art deep learning backed ones—have to rely on methods that fake understanding of the text.

These methods can produce quite impressive results for news articles and other nonfiction, though. However, **summarizing literature** must be the most difficult thing to do. Here are some ways stories **differ from** more straightforward **informative texts.**

- Stories can **not** be summarized with **extractive methods**, i.e. picking and choosing the right sentences to get the most important ideas. Moreover, sentences often depend on their **context** and don’t mean much without their siblings.
- **Long**, **stylistic** sentences, that can hold important information, but are too long for any reasable summary.
- **Dialogue** is insanely complicated. Not only does it matter who says what, it is not even easy to pin-point the speaker, as for long dialogues, this is often represented merely by the alternation of quotations.
- These text are much **longer** than the typical texts, think of books with thousands of pages. In order to really understand the story, the model needs to rememebr information. Current models have either a small short-term memory, or need to hold 

#### Abstractive models

After I tried some extractive methods and—as stated before—I decided that this is not feasable for books, I explored  the most popular abstractive summarization models. I mostly tested on a short Sherlock Holmes story, mostly on the first couple of paragraphs.  

| Model   | Company  | Variations      |
| ------- | -------- | --------------- |
| PEGASUS | Google   | `large`, `xsum` |
| T5      | Google   | `small`, `base` |
| BART    | Facebook | `xsum`, `large` |

The variations specify which trainig set is used. Some **insights**:

* **T5**, for which summarization is merely one of many generative text functions, produces grammatically and substanstivaly worst results. Here is a sentence: 
  
  > but, like all such narratives, its effect is less striking when set forth en bloc in a single half-column of print than when the facts slowly evolve before your own eyes .
* **PEGASUS** gives correct sentences, but in the best case they don't mean anything in relation to the source text, in the worst case it completly makes up new information. Here is it's version of the beginning of a Serlock Holmes story, were dr. Watson to be clear, *doesn't cure Parkinson's disease*, nor even mentions it.
  
  > This is the story of the time when I cured a patient of Parkinson’s disease.
  > I guess that the trainig data contains some medical article about Parkinson's, but it is of course not disirable that the summarizer would invent a totally new subject. 
* **BART** doesn't agree well with stylistic writing, and produces unreadable sentences, like the jewel
  
  > It was in the summer of ’89, not long after that I wrote that I had written to me, and I was going to tell you of the events occurred which I am now about to summarise. 
* Both PEGASUS and BART sometimes get stuck in a repetitive loop, where the same parts get repeated over and over again.
* The results don't mean anything and take more mental energy to comprehend than just reading the the original text does.

#### Roadmap for a working book summarizer

In the limited time I didn't manage to get any good results. However, I did get some insights and ideas for tackling this problem, should one want to try to create a useable solution. 

1. A set-and-forget model will probably never work, no matter the amount of training data. In order to get good results for book summaries, we need to do some **smart preprocessing**.
   
   1. With techniques like **NER**, important information like who are the **main characters** can be extracted in advance. This way, extra weight can be given to sentences/quotes/paraghraphs/chapters with these characters.
   2. (Long) dialogues need to be preprocessed, for example by tagging each quote with its speaker. 
   3. The selection of the chunks that are passed to the summarization model. If too much information is passed. Just passing text paragraph by paragraph probably wont do. Maybe superfluous, extra descriptive text can be detected and thrown away. 

2. All current models are pretrained on informative texts. One should at least try to train a model on summarizes stories, but generating the **training set** would need a lot of human labor. 
   * One could **manually write** short summaries for all Gutenberg books, or even one summary per chapter.
   * Some clever **webscraping** to collect the *back cover text* of some books (although they're mostly teasers that don't contain major plot points). Or one could try to collect summaries from online book reviews, which often start with an overview of the story by the reviewer. 

## Links and further reading

* [Huggingface Transformers Library](https://github.com/huggingface/transformers)
* [Huggingface Summarization Models](https://huggingface.co/models?pipeline_tag=summarization) 
* [SpaCy]()
