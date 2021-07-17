from xml.etree.ElementTree import Element, fromstring


def gamemap(svg_xml: str) -> dict:
    svg = fromstring(svg_xml)
    layer = svg.find(ns('g'))

    return {
        'width': int(svg.attrib['width']),
        'height': int(svg.attrib['height']),
        'map': [rect(element) for element in list(layer) if element.tag == ns('rect')]
    }


def rect(_rect: Element) -> dict:
    attributes = _rect.attrib
    return {
        'x': round(float(attributes['x'])),
        'y': round(float(attributes['y'])),
        'width': round(float(attributes['width'])),
        'height': round(float(attributes['height'])),
        'style': {
            'border': attributes['stroke'],
            'background': attributes['fill'],
        }
    }


def ns(tag: str) -> str:
    return '{http://www.w3.org/2000/svg}' + tag
