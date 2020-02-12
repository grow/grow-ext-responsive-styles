import hashlib
import jinja2
import jinja2.ext
import os


_attribute_cache = {}


def responsive_style_id(queries_to_styles):
    pass


@jinja2.contextfunction
def get_attribute_cache(ctx):
    return _attribute_cache


@jinja2.contextfunction
def responsive_style_attribute(ctx, styles):
    if not styles:
        return ''
    doc = ctx.get('doc')
    attribute = '-rs' + hashlib.sha1(str(styles)).hexdigest()[:4]
    _attribute_cache[attribute] = styles
    return attribute


class ResponsiveStylesExtension(jinja2.ext.Extension):
    def __init__(self, env):
        super(ResponsiveStylesExtension, self).__init__(env)
        env.globals['responsive_style_attribute'] = responsive_style_attribute
        env.globals['get_attribute_cache'] = get_attribute_cache
