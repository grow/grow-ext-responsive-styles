# grow-ext-responsive-styles

[![Build Status](https://travis-ci.org/grow/grow-ext-responsive-styles.svg?branch=master)](https://travis-ci.org/grow/grow-ext-responsive-styles)

## Concept

This extension adds responsive design support to the `style` attribute on HTML
elements, which doesn't natively support media queries.

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
2. Add to the file: `git+git://github.com/grow/grow-ext-responsive-styles`
3. Run `grow install`.
4. Add the following sections to `podspec.yaml`:
```yaml
ext:
- extensions.responsive_styles.ResponsiveStylesExtension:
    media_queries:
      all: '(min-width: 0)'
      tablet: '(min-width: 768px)'
      desktop: '(min-width: 1280px)'
```

### Content

In the content YAML, specify responsive styles as needed:

```yaml
partials:
- partial: foo
  responsive_styles:
    all: 'font-family: Verdana; font-size: 12px'
    tablet: 'font-size: 16px; color: red'
    desktop: 'font-size: 24px; color: blue'
```

### Templates

In templates, apply responsive styles to elements to apply the style attribute:

```jinja2
<div {{responsive_style_attribute(partial.responsive_styles)}}>
  ...
</div>
```

In the partial loop, add the render for the responsive styles:

```jinja2
  {% import "/extensions/responsive_styles/responsive_styles.html" as responsive_styles with context %}
  {% for partial in doc.partials %}
    ...
    {{responsive_styles.render_responsive_styles()}}
  {% endfor %}
```

`render_responsive_styles` must come __after__ all usage of
`responsive_style_attribute`.

If your project does not use a partial loop, `render_responsive_styles()` can
be placed at the end of the page. Each time `render_responsive_styles` is
called, the context-level cache is cleared.
