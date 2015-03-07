# -*- coding: utf-8 -*-

"""Test OpenDocument routines."""


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from ..markdown import BlockLexer
from ..opendocument import ODFDocument, ODFRenderer


# -----------------------------------------------------------------------------
# Test ODFDocument
# -----------------------------------------------------------------------------

def test_odf_document():
    doc = ODFDocument()
    doc.show_styles()

    doc.heading("The title", 1)

    with doc.paragraph():
        doc.text("Some text. ")
        doc.bold("This is bold. ")

    with doc.list():
        with doc.list_item():
            with doc.paragraph():
                doc.text("Item 1.")
        with doc.list_item():
            with doc.paragraph():
                doc.text("Item 2.")
            with doc.list():
                with doc.list_item():
                    with doc.paragraph():
                        doc.text("Item 2.1. This is ")
                        doc.code_line("code")
                        doc.text(". Oh, and here is a link: ")
                        doc.link("http://google.com")
                        doc.text(".")
        with doc.list_item():
            with doc.paragraph():
                doc.text("Item 3.")

    doc.start_quote()
    with doc.paragraph():
        doc.text("This is a citation.")
        doc.linebreak()
        doc.text("End.")
    doc.end_quote()

    with doc.numbered_list():
        with doc.list_item():
            with doc.paragraph():
                doc.text("Item 1.")
        with doc.list_item():
            with doc.paragraph():
                doc.text("Item 2.")

    doc.code("print('Hello world!')")

    # doc.save('test.odt', overwrite=True)


def test_odf_renderer():
    doc = ODFDocument()
    renderer = ODFRenderer(doc)
    block_lexer = BlockLexer(renderer=renderer)
    text = "Hello world!"
    block_lexer.read(text)
