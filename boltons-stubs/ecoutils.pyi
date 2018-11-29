from typing import Any, Dict, List, Optional, Union

def _args2sh(args: List[str], sep: str = ...) -> str: ...
def _escape_shell_args(
    args: List[str], sep: str = ..., style: Optional[str] = ...
) -> str: ...
def get_profile(
    **kwargs: Any
) -> Dict[
    str,
    Union[
        str,
        Dict[str, str],
        int,
        Dict[
            str,
            Union[str, List[Union[str, int]], Dict[str, Union[str, bool]]],
        ],
        float,
    ],
]: ...
def get_python_info() -> Dict[
    str, Union[str, List[Union[str, int]], Dict[str, Union[str, bool]]]
]: ...
