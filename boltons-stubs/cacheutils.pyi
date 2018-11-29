import weakref

from typing import (
    Any,
    Callable,
    Generic,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)


def cached(
    cache: Union[Callable, LRU],
    scoped: bool = ...,
    typed: bool = ...,
    key: None = ...,
) -> Callable: ...


def cachedmethod(
        cache: Union[str, Callable],
        scoped: bool = ...,
        typed: bool = ...,
        key: None = ...,
) -> Callable: ...


class CachedFunction:
    def __init__(self,
        func: Callable,
        cache: Union[Callable, LRU],
        scoped: bool = ...,
        typed: bool = ...,
        key: None = ...,
    ) -> None: ...
    def __call__(self, *args, **kwargs) -> int: ...
    def __repr__(self) -> str: ...


class CachedMethod:
    def __init__(self,
        func: Callable,
        cache: Union[Callable, str],
        scoped: bool = ...,
        typed: bool = ...,
        key: Optional[Callable] = ...,
    ) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...
    def __repr__(self) -> str: ...


class LRI(dict):
    def __init__(self,
        max_size: int = ...,
        values: None = ...,
        on_miss: Optional[Callable] = ...,
    ) -> None: ...
    def __getitem__(self, key: Union[str, _HashedKey]) -> Optional[str]: ...
    def __setitem__(self,
        key: Union[str, _HashedKey],
        value: Optional[str],
    ) -> None: ...


class LRU:
    def __init__(
        self,
        max_size: int = ...,
        values: Optional[Union[LRU, List[Tuple[str, int]]]] = ...,
        on_miss: None = ...,
    ) -> None: ...
    def __getitem__(self, key: Union[str, _HashedKey]): ...
    def __setitem__(self,
        key: Union[str, int, _HashedKey],
        value: Optional[Union[int, str]]
    ) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __eq__(self, other: LRU): ...  # type: ignore
    def __ne__(self, other: LRU) -> bool: ...  # type: ignore
    def __repr__(self) -> str: ...
    def _get_link_and_move_to_front_of_ll(self, key: Union[str, int, _HashedKey]): ...
    def _init_ll(self) -> None: ...
    def _remove_from_ll(self, key: str) -> None: ...
    def _set_key_and_add_to_front_of_ll(
        self,
        key: Union[str, int, _HashedKey],
        value: Optional[Union[str, int]]
    ) -> None: ...
    def _set_key_and_evict_last_in_ll(self, key: Union[str, int], value: Union[str, int]) -> Union[str, int]: ...
    def clear(self) -> None: ...
    def copy(self) -> LRU: ...
    def get(self, key: str, default: None = ...) -> None: ...
    def pop(self, key: str, default: Any = ...): ...
    def popitem(self): ...
    def setdefault(self, key: str, default: Optional[int] = ...): ...
    def update(self, E: Union[List[Tuple[str, int]], LRU], **F): ...


class MinIDMap:
    def __init__(self) -> None: ...
    def get(self, a: Any) -> int: ...
    def drop(self, a: Any) -> None: ...
    def _clean(self, ref: weakref.ref) -> None: ...


class _HashedKey:
    def __hash__(self) -> int: ...
    def __init__(self, key: List[str]) -> None: ...


_CPT = TypeVar('_CPT')


class cachedproperty(Generic[_CPT]):
    def __init__(self, func: Callable[[Any], _CPT]) -> None: ...
    def __repr__(self) -> str: ...
    def __get__(self, obj: Any, objtype: Optional[type]) -> _CPT: ...
