from __future__ import absolute_import

from dictutils import OrderedMultiDict
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Union

def backoff(
    start: int,
    stop: Union[int, float],
    count: Optional[int] = ...,
    factor: Union[int, float] = ...,
    jitter: Union[int, float] = ...,
) -> Union[List[Union[float, int]], List[float]]: ...
def backoff_iter(
    start: int,
    stop: Union[int, float],
    count: Optional[int] = ...,
    factor: Union[int, float] = ...,
    jitter: Union[int, float] = ...,
) -> Iterator[Union[float, int]]: ...
def default_enter(
    path: Tuple, key: Optional[Union[str, int]], value: Any
) -> Any: ...
def default_exit(
    path: Tuple,
    key: Optional[Union[int, str]],
    old_parent: Any,
    new_parent: Union[
        frozenset, OrderedMultiDict, Dict[str, Union[None, int]]
    ],
    new_items: Any,
) -> Any: ...
def first(
    iterable: Union[List[int], List[Union[Tuple, int]]],
    default: Optional[Union[int, float]] = ...,
    key: Optional[Callable] = ...,
) -> Optional[Union[int, float]]: ...
def get_path(
    root: Union[Dict[str, List[str]], List[str], Dict[str, str]],
    path: Union[Tuple[str, int], str, Tuple[str], Tuple[int]],
    default: Any = ...,
) -> str: ...
def remap(
    root: Any,
    visit: Union[str, Callable] = ...,
    enter: Union[str, Callable] = ...,
    exit: Union[str, Callable] = ...,
    **kwargs: Any,
) -> Any: ...
def research(
    root: Dict[str, str], query: Optional[Callable] = ..., reraise: bool = ...
) -> List[Tuple[Tuple[str], str]]: ...

class GUIDerator:
    def __init__(self, size: int = ...) -> None: ...
    def __next__(self) -> str: ...
    def reseed(self) -> None: ...

class SequentialGUIDerator:
    def __next__(self) -> str: ...
    def reseed(self) -> None: ...
