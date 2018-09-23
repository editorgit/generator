from textwrap import dedent

from zmei_generator.fields.text import TextFieldDef, LongTextFieldDef, RichTextFieldDef, RichTextFieldWithUploadDef
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


def _(code):
    tree = parse_string(dedent(code))

    return populate_collection_set(tree, 'example')


def test_text_field():
    cs = _("""
    
        #boo
        ----------
        a
        b: str(255)
        c: str(?, choices=ab:Cda,abcd:Cda1,abcdef:"Яба яба")
        d: str(?, choices=foo,bar,baz)
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, TextFieldDef)
    assert a.max_length == 100

    b = cs.collections['boo'].fields['b']

    assert isinstance(b, TextFieldDef)
    assert b.max_length == 255

    c = cs.collections['boo'].fields['c']

    assert isinstance(c, TextFieldDef)
    assert c.max_length == 6
    assert c.choices == (
        ('ab', 'Cda'),
        ('abcd', 'Cda1'),
        ('abcdef', 'Яба яба'),
    )

    d = cs.collections['boo'].fields['d']

    assert isinstance(d, TextFieldDef)
    assert d.choices == (
        ('foo', 'foo'),
        ('bar', 'bar'),
        ('baz', 'baz'),
    )

def test_longtext_field():
    cs = _("""
    
        #boo
        ----------
        a: text
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, LongTextFieldDef)


def test_html_field():
    cs = _("""
    
        #boo
        ----------
        a: html
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, RichTextFieldDef)


def test_html_media_field():
    cs = _("""
    
        #boo
        ----------
        a: html_media
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, RichTextFieldWithUploadDef)