# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: TripBrief
def tag_add(item, tag):
    if item.get("tags"):
        tags = list(item["tags"])
    else:
        tags = []
    if tag not in tags:
        tags.append(tag)
        item["tags"] = tags
    return item

def tag_remove(item, tag):
    if not item.get("tags"):
        return item
    tags = list(item["tags"])
    if tag in tags:
        tags.remove(tag)
        item["tags"] = tags
    else:
        raise ValueError(f"Tag '{tag}' not found on {item.get('title', 'item')}")
    return item

def summarize_by_tags(items, group_by=None):
    result = {}
    for it in items:
        key = tag or (group_by and it.get(group_by)) if "tag" in dir() else None
