from typing import Any, Dict, Iterator, List, Set, Tuple, Type, Union
from uuid import UUID

def asciify(text: str, ignore: bool = ...) -> bytes: ...
def format_int_list(
    int_list: List[int],
    delim: str = ...,
    range_delim: str = ...,
    delim_space: bool = ...,
) -> str: ...
def indent(
    text: str, margin: str, newline: str = ..., key: Type[bool] = ...
) -> str: ...
def is_uuid(obj: Union[str, UUID, Set[str]], version: int = ...) -> bool: ...
def iter_splitlines(text: str) -> Iterator[str]: ...
def multi_replace(
    text: str, sub_map: Dict[str, str], **kwargs: Any
) -> str: ...
def parse_int_list(
    range_string: str, delim: str = ..., range_delim: str = ...
) -> List[int]: ...

class DeaccenterDict:
    def __missing__(self, key: int) -> int: ...

class MultiReplace:
    def __init__(
        self,
        sub_map: Union[List[Tuple[str, str]], Dict[str, str]],
        **kwargs: Any,
    ) -> None: ...
    def sub(self, text: str) -> str: ...
