import logging
import re
from collections import Counter

from bs4 import BeautifulSoup as bs

logger = logging.getLogger(__name__)
logger.setLevel(-1)


class Book:
    """Parser object for Project Gutenberg books. Easily retrieve chapters, or
    other parts."""

    def __init__(self, filename: str, chapter_tag: str = None):
        """Create a new Book object.

        :param filename: Path to html file
        :param chapter_tag: html tag that
        """
        # logging
        self.logger = logger.getChild("Book")

        # parsing HTML
        self.logger.info(f"Parsing {filename} with BeautifulSoup.")
        try:
            with open(filename, "r") as f:
                self.soup = bs(f.read(), features="html.parser")
        except FileNotFoundError:
            self.logger.critical(f"File {filename} not found.")
            raise FileNotFoundError()
        except Exception:
            self.logger.exception("Problem with parsing html file.")
            raise Exception

        # get the meta information
        self.logger.info("Parsing meta information.")
        try:
            # look for title and author in first 1000 chars of body source
            self.book_author = re.search(
                r"Author: ([^<\n]+)", str(self.soup.body)[:1000]
            ).group(1)
            self.book_title = re.search(
                r"Title: ([^<\n]+)", str(self.soup.body)[:1000]
            ).group(1)
        except:
            self.logger.warning(f"Title and auhtor not automatically found")
            self.book_title = self.soup.find("h1").text.strip()
            self.book_author = "AUTHOR NOT FOUND"

        # chapter detection
        if chapter_tag is not None:
            self._chapter_tag = chapter_tag
        else:
            # try to detect chapter tag automatically
            self.logger.info(
                "Chapter tag not specified, trying to detect from context."
            )
            # count all headers
            header_count = Counter(
                [header.name for header in self.soup.find_all(re.compile("^h[1-6]$"))]
            )
            self._chapter_tag = header_count.most_common(1)[0][0]
            self.logger.debug(f"Selected {self._chapter_tag} for chapter headers.")

        self.chapter_names = [
            title.text.strip()
            for title in self.soup.select(f"{self._chapter_tag}")
            if not (
                "contents" in title.text.lower()  # remove table of contents
                or title.text.strip().lower().startswith("by ")  # remove author tags
            )
        ]

        self.logger.debug(
            f"Book {self.book_title} by {self.book_author}, has {len(self.chapter_names)} chapters."
        )

    def get_paragraphs(self, chapter: int = None):
        """Generator for all paragraphs in a selected chapter (and section).

        :param chapter: chapter number, if not specified, the full book will be traversed.
        """

        # select body of the chapter
        if chapter is None:
            current_p = self.soup.body.find("p")
        else:
            current_p = self.soup.select(self._chapter_tag)[chapter].nextSibling

        # loop
        while current_p is not None:
            if current_p.name == self._chapter_tag:
                break
            if current_p.name == "p":
                p = re.sub(r"\s+", " ", current_p.get_text(strip=True, separator=" "))
                # take care of big stylish character at beginning
                if current_p.select(".dropcap"):
                    p = p[0] + p[2:]

                yield p

            current_p = current_p.nextSibling

    def get_chapter(self, chapter: int, merge: bool = False):
        """Return al text of chapter with given number.

        :param chapter: chapter number
        :param merge: Whether paragraphs should be merged, separated by two newlines, default False.
        """
        if merge:
            return "\n\n".join([*self.get_paragraphs(chapter)])
        else:
            return [*self.get_paragraphs(chapter)]


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
    logger.info(f"Loading {test_file} as a test.")
    test_book = Book(test_file)
    p = test_book.get_paragraphs(1)
    # print([*p])
    pass
