from textwrap import dedent

from zmei_generator.contrib.web.fields.number import IntegerFieldDef, FloatFieldDef, DecimalFieldDef
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_int_field():
    cs = _("""
    
        #boo
        ----------
        b: int
        c: int(choices=2:Cda, 4:Cda1, 5:"Яба яба")
        d: int(choices=foo,bar,baz)
    """)

    b = cs.collections['boo'].fields['b']

    assert isinstance(b, IntegerFieldDef)

    c = cs.collections['boo'].fields['c']

    assert isinstance(c, IntegerFieldDef)
    assert c.choices == (
        (2, 'Cda'),
        (4, 'Cda1'),
        (5, 'Яба яба'),
    )

    d = cs.collections['boo'].fields['d']

    assert isinstance(d, IntegerFieldDef)
    assert d.choices == (
        (0, 'foo'),
        (1, 'bar'),
        (2, 'baz'),
    )


def test_float_field():
    cs = _("""

        #boo
        ----------
        a: float
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, FloatFieldDef)


def test_decimal_field():
    cs = _("""

        #boo
        ----------
        a: decimal
    """)

    a = cs.collections['boo'].fields['a']

    assert isinstance(a, DecimalFieldDef)
