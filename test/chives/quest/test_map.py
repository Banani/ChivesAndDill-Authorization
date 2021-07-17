from chives.map.map import gamemap
from test.resources import resource


def test_map():
    # given
    xml = resource('maps/root.svg')

    # when
    _map = gamemap(xml)

    # then
    assert _map == {
        'height': 9000,
        'width': 1000,
        'map': [
            {
                'x': 187,
                'y': 180,
                'width': 55,
                'height': 456,
                'style': {'background': '#fff', 'border': '#000'},
            },
            {
                'x': 103,
                'y': 197,
                'height': 11,
                'width': 162,
                'style': {'background': '#fff', 'border': '#000'},
            },
            {
                'x': 875,
                'y': 267,
                'height': 27,
                'width': 8,
                'style': {'background': '#fff', 'border': '#000'},
            },
            {
                'x': 861,
                'y': 267,
                'height': 6,
                'width': 22,
                'style': {'background': '#aeaeae', 'border': '#000'},
            }
        ],
    }
