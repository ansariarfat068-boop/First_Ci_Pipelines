"""Program 27: Rotate a list right by k positions; negative k rotates left."""
def rotate_list(items, k):
    if not items:
        return []
    shift = k % len(items)
    if shift == 0:
        return items.copy()
    return items[-shift:] + items[:-shift]
