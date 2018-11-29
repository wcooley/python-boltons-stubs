import weakref

from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    Generic,
    Iterable,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

KT = TypeVar("KT")
VT = TypeVar("VT")
T = TypeVar("T")

FuncType = Callable[..., Any]

CacheInitType = Union[
    Callable[[], MutableMapping[KT, VT]], MutableMapping[KT, VT]
]

MakeCacheKeyType = Callable[
    [Iterable, Mapping, Any, FrozenSet[Type]], _HashedKey
]

def cached(
    cache: CacheInitType,
    scoped: bool = ...,
    typed: bool = ...,
    key: Optional[MakeCacheKeyType] = ...,
) -> Callable[..., Any]: ...
def cachedmethod(
    cache: Union[CacheInitType, str],
    scoped: bool = ...,
    typed: bool = ...,
    key: Optional[MakeCacheKeyType] = ...,
) -> Callable: ...

class CachedFunction:
    def __init__(
        self,
        func: FuncType,
        cache: CacheInitType,
        scoped: bool = ...,
        typed: bool = ...,
        key: Optional[MakeCacheKeyType] = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> int: ...
    def __repr__(self) -> str: ...

class CachedMethod:
    def __init__(
        self,
        func: Callable,
        cache: Union[CacheInitType, str],
        scoped: bool = ...,
        typed: bool = ...,
        key: Optional[MakeCacheKeyType] = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    def __repr__(self) -> str: ...

class LRI(Dict[KT, VT]):
    def __init__(
        self,
        max_size: int = ...,
        values: Optional[
            Union[Mapping[KT, VT], Iterable[Tuple[KT, VT]]]
        ] = ...,
        on_miss: Optional[Callable[[KT], VT]] = ...,
    ) -> None: ...
    def __getitem__(self, key: KT) -> Optional[VT]: ...  # type: ignore
    def __setitem__(self, key: KT, value: VT) -> None: ...

class LRU(Dict[KT, VT]):
    def __init__(
        self,
        max_size: int = ...,
        values: Optional[
            Union[Mapping[KT, VT], Iterable[Tuple[KT, VT]]]
        ] = ...,
        on_miss: Optional[Callable[[KT], VT]] = ...,
    ) -> None: ...
    def __getitem__(self, key: KT) -> Optional[VT]: ...  # type: ignore
    def __setitem__(self, key: KT, value: VT) -> None: ...
    def __delitem__(self, key: KT) -> None: ...
    def __eq__(self, other: LRU) -> bool: ...  # type: ignore
    def __ne__(self, other: LRU) -> bool: ...  # type: ignore
    def __repr__(self) -> str: ...
    def _get_link_and_move_to_front_of_ll(self, key: KT) -> VT: ...
    def _init_ll(self) -> None: ...
    def _remove_from_ll(self, key: KT) -> None: ...
    def _set_key_and_add_to_front_of_ll(self, key: KT, value: VT) -> None: ...
    def _set_key_and_evict_last_in_ll(self, key: KT, value: VT) -> VT: ...
    def clear(self) -> None: ...
    def copy(self) -> LRU: ...
    def get(  # type: ignore
        self, key: KT, default: Any = ...
    ) -> Optional[VT]: ...
    def pop(self, key: KT, default: Any = ...) -> VT: ...
    def popitem(self) -> Tuple[KT, VT]: ...
    def setdefault(  # type: ignore
        self, key: KT, default: Optional[VT] = ...
    ) -> Optional[VT]: ...
    def update(  # type: ignore
        self, E: Union[Mapping[KT, VT], Iterable[Tuple[KT, VT]]], **F: Any
    ) -> None: ...

class MinIDMap(Generic[T]):
    def __init__(self) -> None: ...
    def get(self, a: T) -> int: ...
    def drop(self, a: T) -> None: ...
    def _clean(self, ref: weakref.ref) -> None: ...

class _HashedKey:
    def __hash__(self) -> int: ...
    def __init__(self, key: List[Any]) -> None: ...

class cachedproperty(Generic[T]):
    def __init__(self, func: Callable[[], T]) -> None: ...
    def __repr__(self) -> str: ...
    def __get__(self, obj: Any, objtype: Optional[Type]) -> T: ...
