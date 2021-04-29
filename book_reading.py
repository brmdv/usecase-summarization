import logging
import re

from bs4 import BeautifulSoup as bs

logger = logging.getLogger(__name__)
logger.setLevel(-1)


class Book:
    """Parser object for Project Gutenberg books. Easily retrieve chapters, or
    other parts."""

    def __init__(self, filename, chapter_tag="h3"):
        """Create a new Book object. """
        # logging
        self.logger = logger.getChild("Book")

        # parsing HTML
        self.logger.info(f"Parsing {filename} with BeautifulSoup.")
        try:
            with open(filename, "r") as f:
                self.soup = bs(f.read(), features="lxml")
        except FileNotFoundError:
            self.logger.critical(f"File {filename} not found.")
        except Exception:
            self.logger.exception("Problem with parsing html file.")

        # get the meta information
        self.logger.info("Parsing meta information.")
        self.book_title = self.soup.find("h1").text.strip()
        self.book_author = self.soup.find("h2").text.strip().lstrip("by ")

        # chapter detection
        self._chapter_tag = chapter_tag

        self.chapter_names = [
            title.text.strip()
            for title in self.soup.select(f".chapter {self._chapter_tag}")
        ]

        self.logger.debug(
            f"Book {self.book_title} by {self.book_author}, has {len(self.chapter_names)} chapters."
        )

    def get_paragraphs(self, chapter=None):
        """Generator for all paragraphs in a selected chapter (and section). If
        they are not specified, the full book will be traversed."""

        # select body of the chapter
        if chapter is None:
            current_p = self.soup.body.find("p")
        else:
            current_p = self._get_chapter(chapter)

        # loop
        while current_p is not None:
            if current_p.nextSibling.name == self._chapter_tag:
                break
            if current_p.name == "p":
                p = re.sub(r"\s+", " ", current_p.get_text(strip=True, separator=" "))
                # take care of big stylish character at beginning
                if current_p.select(".dropcap"):
                    p = p[0] + p[2:]

                yield p

            current_p = current_p.nextSibling


if __name__ == "__main__":
    # setup basic logger
    logstream = logging.StreamHandler()
    logstream.setLevel(logging.DEBUG)
    logstream.setFormatter(
        logging.Formatter(
            "{asctime} {name:15s} {levelname:8s} {message}",
            style="{",
            datefmt="%H:%m:%S",
        )
    )
    logger.addHandler(logstream)

    test_file = "books/80days.html"
    logger.info("Loading {test_file} as a test.")
    test_book = Book(test_file, chapter_tag="h4")
    p = test_book.get_paragraphs(0)
    print([*p])
    pass
