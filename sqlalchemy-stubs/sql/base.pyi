from typing import Any
from sqlalchemy import util
from .visitors import ClauseVisitor as ClauseVisitor
from .schema import Column

PARSE_AUTOCOMMIT: Any = ...
NO_ARG: Any = ...

class Immutable(object):
    def unique_params(self, *optionaldict, **kwargs): ...
    def params(self, *optionaldict, **kwargs): ...
    def _clone(self) -> Immutable: ...

class DialectKWArgs(object):
    @classmethod
    def argument_for(cls, dialect_name, argument_name, default): ...
    @property
    def dialect_kwargs(self): ...
    @property
    def kwargs(self): ...
    @property
    def dialect_options(self): ...

class Generative(object): ...

class Executable(Generative):
    supports_execution: bool = ...
    def execution_options(self, **kw): ...
    def execute(self, *multiparams, **params): ...
    def scalar(self, *multiparams, **params): ...
    @property
    def bind(self): ...

class SchemaEventTarget(object): ...

class SchemaVisitor(ClauseVisitor):
    __traverse_options__: Any = ...

class ColumnCollection(util.OrderedProperties[Column]):
    def __init__(self, *columns) -> None: ...
    def replace(self, column): ...
    def add(self, column): ...
    def __delitem__(self, key): ...
    def __setattr__(self, key: str, object: Column) -> None: ...
    def __setitem__(self, key, value: Column): ...
    def clear(self): ...
    def remove(self, column): ...
    def update(self, iter): ...
    def extend(self, iter): ...
    __hash__: Any = ...
    def __eq__(self, other): ...
    def __contains__(self, other): ...
    def contains_column(self, col): ...
    def as_immutable(self): ...

class ImmutableColumnCollection(util.ImmutableProperties[Column], ColumnCollection):
    def __init__(self, data, all_columns) -> None: ...
    extend: Any = ...
    remove: Any = ...

class ColumnSet(util.ordered_column_set):
    def contains_column(self, col): ...
    def extend(self, cols): ...
    def __add__(self, other): ...
    def __eq__(self, other): ...
    def __hash__(self): ...