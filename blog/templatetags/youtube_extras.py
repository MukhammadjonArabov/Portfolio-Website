from urllib.parse import urlparse, parse_qs
from django import template

register = template.Library()


@register.filter
def youtube_id(value):
    if not value:
        return ''
    v = value.strip()
    if len(v) == 11 and '/' not in v and 'watch' not in v:
        return v
    try:
        parsed = urlparse(v)
    except Exception:
        return v
    if parsed.query:
        qs = parse_qs(parsed.query)
        if 'v' in qs:
            return qs['v'][0]
    path = parsed.path or ''
    if path:
        parts = [p for p in path.split('/') if p]
        if parts:
            return parts[-1]
    return v
