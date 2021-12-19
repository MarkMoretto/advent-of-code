

from .types import *

def unpacker_old(obj: Iterable, depth_level: int = 1, parent_index: int = 0, total_index: list = [-1]) -> Iterator:
    """Recursively walk nested, hashable iterable object.

    Parameters
    ---------
    obj : Iterable
        Main nested iterable object.
    depth_level : int
        Current depth level
    parent_index : int
        Current parent depth level
    total_index : List[int]
        Running index for entire series.
    """
    if depth_level == 1:
        # Clear total_index list and "reset" for each new run.
        total_index.clear()
        total_index = [0]

        yield total_index[-1], parent_index, depth_level, obj
        yield from unpacker(obj, depth_level + 1, depth_level, total_index)
    else:
        for item in obj:
            if isinstance(item, list):
                total_index.append(total_index[-1] + 1)
                yield total_index[-1], parent_index, depth_level, item
                yield from unpacker(item, depth_level + 1, depth_level, total_index)
            # else: # For individual number granularity, uncomment
            #     yield level, parent, item
    return

def unpacker(obj: Iterable, total_index: list = [-1], parent_depth: int = 0, child_depth: int = 1) -> Iterator:
    if child_depth == 1:
        total_index.clear()
        total_index = [0]
        yield total_index[-1], parent_depth, child_depth, obj
        yield from unpacker(obj, total_index, child_depth, child_depth + 1)
    else:
        for nested_item in obj:
            if isinstance(nested_item, list):
                total_index.append(total_index[-1] + 1)
                yield total_index[-1], parent_depth, child_depth, nested_item
                yield from unpacker(nested_item, total_index, child_depth, child_depth + 1)
    return

def unpack_from(obj: Iterable, minimum_depth: int = 0) -> Iterable:
    """Iterates unpacker(), but doesn't return output until minimum depth
    is met."""
    i = -1
    for _, parent, depth_lvl, item in unpacker(obj):
        if depth_lvl >= minimum_depth:
            i += 1
            yield i, parent, depth_lvl, item


def view_levels(iterable: list, minimum_depth: int = 0):
    """Print results of unpack() function. Features optional parameter
    to specify a minimum depth until results start showing up.
    """
    for idx, parent, depth_lvl, item in unpacker(iterable):
        if depth_lvl >= minimum_depth:
            print(f"{idx:<3}-> Parent: {parent:<2}-> Depth:{depth_lvl:^3}-> {item}")














def reducer(iterable):
    """Recursive aggregate summation

    Example
    -------
    >>> reducer([2,3,4,5])
    14
    """

    length = len(iterable)
    def inner(i, total):
        if i == length:
            return total
        return inner(i+1, total + iterable[i])
    return inner(0, 0)
