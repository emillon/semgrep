from __future__ import annotations

from typing import Any
from typing import Callable
from typing import List
from typing import Union

class BasePriorityQueue:
    def __init__(self, **kw: Any) -> None: ...
    def __len__(self) -> int: ...
    def _cull(self, raise_exc: bool = ...) -> None: ...
    def add(self, task: Callable, priority: None = ...) -> None: ...
    def pop(self, default: Any = ...) -> Callable: ...
    def remove(self, task: Callable) -> None: ...

class HeapPriorityQueue:
    @staticmethod
    def _pop_entry(
        backend: list[list[Any] | list[int | Callable]] | list[list[int | Callable]]
    ) -> list[int | Callable] | list[Any]: ...
    @staticmethod
    def _push_entry(
        backend: list[list[Any]], entry: list[int | Callable]
    ) -> None: ...

class SortedPriorityQueue:
    @staticmethod
    def _pop_entry(
        backend: list[list[Any] | list[int | Callable]] | list[list[int | Callable]]
    ) -> list[int | Callable] | list[Any]: ...
    @staticmethod
    def _push_entry(
        backend: list[list[Any]], entry: list[int | Callable]
    ) -> None: ...
