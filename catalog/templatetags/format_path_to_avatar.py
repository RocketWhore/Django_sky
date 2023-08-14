from django import template
register = template.Library()


@register.filter()
def format_path_to_avatar(text):
    return f'/media/{text}'

@register.simple_tag()
def tag_path_to_avatar(text):
    return f'{format_path_to_avatar} {text}'


@register.filter()
def format_version(text):
    return f'Версия: {text}'
@register.simple_tag()
def tag_version(text):
    return f'{format_path_to_avatar} {text}'