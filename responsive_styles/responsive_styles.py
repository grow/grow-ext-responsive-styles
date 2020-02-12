import hashlib
import jinja2
import jinja2.ext
import os


def responsive_style_id(queries_to_styles):
    pass


@jinja2.contextfunction
def render_responsive_styles(ctx, queries_to_styles):
    pod = ctx.get('doc').pod
    template_list = []
    for macro in macros:
        template_list.append(
            '{%% import "/views/macros/%(macro)s.html" as %(macro)s_lib with context %%}' % {'macro': macro})
    for macro in macros:
        template_list.append(
            '{%% macro %(macro)s(options) %%}{{%(macro)s_lib.%(macro)s(options, **kwargs)}}{%% endmacro %%}' % {'macro': macro})
    template = pod.get_jinja_env().from_string(template_str)
    return template.make_module(ctx, locals={'partial': partial})


@jinja2.contextfunction
def responsive_style_attribute(ctx, queries_to_styles):
    if not queries_to_styles:
        return ''
    doc = ctx.get('doc')
    return '-rs' + hashlib.sha1(str(queries_to_styles)).hexdigest()[:4]


class ResponsiveStylesExtension(jinja2.ext.Extension):
    def __init__(self, env):
        super(ResponsiveStylesExtension, self).__init__(env)
        env.globals['responsive_style_attribute'] = responsive_style_attribute
        env.globals['render_responsive_styles'] = render_responsive_styles
