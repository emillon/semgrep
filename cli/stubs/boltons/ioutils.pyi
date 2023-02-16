from __future__ import annotations

from codecs import StreamReaderWriter
from codecs import StreamRecoder
from io import BufferedRandom
from io import BufferedReader
from io import BytesIO
from io import StringIO
from io import TextIOWrapper
from typing import Any
from typing import List
from typing import Optional
from typing import Union

def is_text_fileobj(
    fileobj: TextIOWrapper | BytesIO | BufferedReader | StringIO | StreamReaderWriter
) -> bool: ...

class MultiFileReader:
    def __init__(self, *fileobjs: Any) -> None: ...
    def read(self, amt: int | None = ...) -> str | bytes: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...

class SpooledBytesIO:
    @property
    def _rolled(self) -> bool: ...
    @property
    def buffer(self) -> BytesIO | BufferedRandom: ...
    @property
    def len(self) -> int: ...
    def read(self, n: int = ...) -> bytes: ...
    def readline(self, length: None = ...) -> bytes: ...
    def readlines(self, sizehint: int = ...) -> list[bytes]: ...
    def rollover(self) -> None: ...
    def seek(self, pos: int, mode: int = ...) -> int: ...
    def tell(self) -> int: ...
    def write(self, s: str | bytes) -> None: ...

class SpooledIOBase:
    def __bool__(self) -> bool: ...
    def __enter__(self) -> SpooledBytesIO | SpooledStringIO: ...
    def __eq__(  # type: ignore
        self, other: str | SpooledBytesIO | SpooledStringIO
    ) -> bool: ...
    def __exit__(self, *args: Any) -> None: ...
    def __init__(self, max_size: int = ..., dir: str | None = ...) -> None: ...
    def __iter__(self) -> SpooledBytesIO | SpooledStringIO: ...
    def __len__(self) -> int: ...
    def __ne__(  # type: ignore
        self, other: str | SpooledBytesIO | SpooledStringIO
    ) -> bool: ...
    @property
    def _file(self) -> StreamRecoder | BytesIO: ...
    def _get_softspace(self) -> bool: ...
    def _set_softspace(self, val: bool) -> None: ...
    @property
    def buf(self) -> str | bytes: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def getvalue(self) -> str | bytes: ...
    def isatty(self) -> bool: ...
    def next(self) -> str | bytes: ...
    @property
    def pos(self) -> int: ...
    def truncate(self, size: int | None = ...) -> int | None: ...

class SpooledStringIO:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def _rolled(self) -> bool: ...
    def _traverse_codepoints(self, current_position: int, n: int) -> int: ...
    @property
    def buffer(self) -> StreamRecoder: ...
    @property
    def len(self) -> int: ...
    def read(self, n: int = -1) -> str: ...
    def readline(self, length: None = None) -> str: ...
    def readlines(self, sizehint: int = 0) -> list[str]: ...
    def rollover(self) -> None: ...
    def seek(self, pos: int, mode: int = 0) -> int: ...
    def tell(self) -> int: ...
    def write(self, s: str | bytes) -> None: ...
