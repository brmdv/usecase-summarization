# Text summarization with NLP

The goal of this project, on behalf of [Algorhythm](https://algorhythm.be/), is to explore the current state of Natural Language Processing for text summarization.

{:toc}

## Technical details

### Data sources

The methods are tested on [books](https://www.gutenberg.org/) that are in the public domain, downloaded in HTML format from Project Gutenberg.  

### Deliverables

- **Project Gutenberg** [book parser](book_reading.py), to extract paragraphs from selected chapters.
- Simple Flask **webapp** to [try out](#) some results.

### Installation and usage

This project is mainly built on [HuggingFace's](https://huggingface.co/) [transformers](https://github.com/huggingface/transformers) library, as it provides an easy way into the newest pre-trained models. I opted for the Tensorflow backend, as it is already installed on [Google Collab](), so that I could easily upscale bigger test to the free resources provided by Google. 

## Notable conclusions

**Automatic text summarization is hard.** Without the full life experience of a human being behind it, all algorithms—even the most state-of-the-art deep learning backed ones—have to rely on methods that fake understanding of the text.

These methods can produce quite impressive results for news articles and other nonfiction, though. However, summarizing literature must be the most difficult thing to do. Here are some ways stories differ from more straightforward informative texts.

- Stories can **not** be summarized with **extractive methods**, i.e. picking and choosing the right sentences to get the most important ideas. Moreover, sentences often depend on their **context** and don’t mean much without their siblings.
- **Long**, **stylistic** sentences, that can hold important information.
- **Dialogue** is insanely complicated. Not only does it matter who says what, it is not even easy to pin-point the speaker, as for long dialogues, this is often represented merely by the alternation of quotations.

In order to get good results for book summaries, we need to do some smart preprocessing. 

## Roadmap for a working book summarizer

In the limited time I didn't manage to get any usable results. However, I did get some insights and  ideas for tackling this problem, should one want to try to create one. 

1. 

## Links and further reading

* https://github.com/huggingface/transformers

* [Huggingface Summarization Models](https://huggingface.co/models?pipeline_tag=summarization) 

* 
