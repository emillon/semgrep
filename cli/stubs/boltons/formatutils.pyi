from __future__ import annotations

from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

def construct_format_field_str(fname: str, fspec: str, conv: str | None) -> str: ...
def get_format_args(
    fstr: str,
) -> tuple[list[tuple[int, type[str]]], list[Any]] | tuple[list[tuple[int, type[str]] | tuple[int, type[int]] | tuple[int, type[float]]], list[Any]] | tuple[list[Any], list[tuple[str, type[str]]]]: ...
def infer_positional_format_args(fstr: str) -> str: ...
def split_format_str(
    fstr: str,
) -> list[tuple[str, str]] | list[tuple[str, str] | tuple[str, None]]: ...
def tokenize_format_str(
    fstr: str, resolve_pos: bool = ...
) -> list[str | BaseFormatField]: ...

class BaseFormatField:
    def __init__(
        self, fname: str, fspec: str = ..., conv: str | None = ...
    ) -> None: ...
    def set_conv(self, conv: str | None) -> None: ...
    def set_fname(self, fname: str) -> None: ...
    def set_fspec(self, fspec: str) -> None: ...

class DeferredValue:
    def __init__(self, func: Callable, cache_value: bool = ...) -> None: ...
    def __str__(self) -> str: ...
    def get_value(self) -> int: ...
