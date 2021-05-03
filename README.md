# Text summarization with NLP

The goal of this project, on behalf of [Algorhythm](https://algorhythm.be/), is to explore the current state of Natural Language Processing for text summarization.

## Technical details

### Data sources

The methods are tested on [books](https://www.gutenberg.org/) that are in the public domain. 

### Deliverables

- **Project Gutenberg** [book parser](book_reading.py), to extract paragraphs from selected chapters.
- 

### Installation and usage

This project is mainly built on HuggingFace's transformers library, as it provides an easy way into the newest pre-trained models. I opted for the 

## Notable conclusions

**Automatic text summarization is hard.** Without the full life experience of a human being behind it, all algorithms—even the most state-of-the-art deep learning backed ones—have to rely on methods that fake understanding of the text.

These methods can produce quite impressive results for news articles and other nonfiction, though. However, summarizing literature must be the most difficult thing to do. Here are some ways stories differ from more straightforward informative texts.

- Stories can **not** be summarized with **extractive methods**, i.e. picking and choosing the right sentences to get the most important ideas. Moreover, sentences often depend on their **context** and don’t mean much without their siblings.
- **Long**, **stylistic** sentences, that can hold important information.
- **Dialogue** is insanely complicated. Not only does it matter who says what, it is not even easy to pin-point the speaker, as for long dialogues, this is often represented merely by the alternation of quotations.

In order to get good results for book summaries, we need to do some smart preprocessing. 
