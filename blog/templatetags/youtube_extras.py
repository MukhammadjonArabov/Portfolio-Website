from urllib.parse import urlparse, parse_qs
from django import template

register = template.Library()


@register.filter
def youtube_id(value):
    """Extract a YouTube ID from a full URL or return the value if it already looks like an ID."""
    if not value:
        return ''
    v = value.strip()
    # If looks like a plain id (11 chars, common YouTube id length)
    if len(v) == 11 and '/' not in v and 'watch' not in v:
        return v
    try:
        parsed = urlparse(v)
    except Exception:
        return v
    # For URLs like https://www.youtube.com/watch?v=VIDEOID
    if parsed.query:
        qs = parse_qs(parsed.query)
        if 'v' in qs:
            return qs['v'][0]
    # For short urls like https://youtu.be/VIDEOID or /embed/VIDEOID
    path = parsed.path or ''
    if path:
        # strip trailing slash
        parts = [p for p in path.split('/') if p]
        if parts:
            return parts[-1]
    return v
