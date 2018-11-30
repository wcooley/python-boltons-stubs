import socket
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from dictutils import OrderedMultiDict

T = TypeVar("T")

def to_unicode(obj: str) -> str: ...
def find_all_links(
    text: str, with_text: bool, default_scheme: str, schemes: Tuple[str, ...]
) -> Union[List[Union[URL, str]], List[URL]]: ...
def quote_path_part(text: str, full_quote: bool) -> str: ...
def quote_query_part(text: str, full_quote: bool) -> str: ...
def quote_fragment_part(text: str, full_quote: bool) -> str: ...
def quote_userinfo_part(text: str, full_quote: bool) -> str: ...
def unquote(string: str, encoding: str, errors: str) -> str: ...
def unquote_to_bytes(string: str) -> bytes: ...
def register_scheme(
    text: str, uses_netloc: bool, default_port: int
) -> None: ...
def resolve_path_parts(path_parts: Tuple[str, ...]) -> List[str]: ...

class cachedproperty(Generic[T]):
    def __init__(self, func: Callable[[Any], T]) -> None: ...
    def __get__(self, obj: URL, objtype: Optional[Type]) -> T: ...
    def __repr__(self) -> str: ...

class URL:
    def __init__(self, url: Union[URL, bytes, str]) -> None: ...
    @classmethod
    def from_parts(
        cls,
        scheme: str,
        host: str,
        path_parts: Union[List[str], Tuple[str, ...]],
        query_params: QueryParamDict,
        fragment: str,
        port: Optional[str],
        username: Optional[str],
        password: Optional[str],
    ) -> URL: ...
    @cachedproperty
    def query_params(self) -> QueryParamDict: ...
    @overload
    @property
    def path(self) -> str: ...
    @overload
    @property
    def path(self, path_text: str) -> None: ...
    @property
    def uses_netloc(self) -> Union[bool, str]: ...
    @property
    def default_port(self) -> int: ...
    def normalize(self, with_case: bool) -> None: ...
    def navigate(self, dest: Union[URL, str]) -> URL: ...
    def get_authority(self, full_quote: bool, with_userinfo: bool) -> str: ...
    def to_text(self, full_quote: bool) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: URL) -> bool: ...  # type: ignore
    def __ne__(self, other: URL) -> bool: ...  # type: ignore

def parse_host(
    host: Optional[str]
) -> Tuple[Optional[socket.AddressFamily], str]: ...
def parse_url(
    url_text: str
) -> Union[Dict[str, Optional[str]], Dict[str, str]]: ...
def parse_qsl(
    qs: str, keep_blank_values: bool, encoding: str
) -> Union[
    List[Tuple[str, None]],
    List[Tuple[str, Optional[str]]],
    List[Tuple[str, str]],
]: ...

class QueryParamDict(OrderedMultiDict):
    @classmethod
    def from_text(cls, query_string: str) -> QueryParamDict: ...
    def to_text(self, full_quote: bool) -> str: ...