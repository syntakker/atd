"""Generated by atdpy from type definitions in everything.atd.

This implements classes for the types defined in 'everything.atd', providing
methods and functions to convert data from/to JSON.
"""

# Disable flake8 entirely on this file:
# flake8: noqa

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, NoReturn, Optional, Tuple, Union

import json

############################################################################
# Private functions
############################################################################


def _atd_missing_json_field(type_name: str, json_field_name: str) -> NoReturn:
    raise ValueError(f"missing field '{json_field_name}'"
                     f" in JSON object of type '{type_name}'")


def _atd_bad_json(expected_type: str, json_value: Any) -> NoReturn:
    value_str = str(json_value)
    if len(value_str) > 200:
        value_str = value_str[:200] + '…'

    raise ValueError(f"incompatible JSON value where"
                     f" type '{expected_type}' was expected: '{value_str}'")


def _atd_bad_python(expected_type: str, json_value: Any) -> NoReturn:
    value_str = str(json_value)
    if len(value_str) > 200:
        value_str = value_str[:200] + '…'

    raise ValueError(f"incompatible Python value where"
                     f" type '{expected_type}' was expected: '{value_str}'")


def _atd_read_unit(x: Any) -> None:
    if x is None:
        return x
    else:
        _atd_bad_json('unit', x)


def _atd_read_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    else:
        _atd_bad_json('bool', x)


def _atd_read_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    else:
        _atd_bad_json('int', x)


def _atd_read_float(x: Any) -> float:
    if isinstance(x, (int, float)):
        return x
    else:
        _atd_bad_json('float', x)


def _atd_read_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        _atd_bad_json('str', x)


def _atd_read_list(
            read_elt: Callable[[Any], Any]
        ) -> Callable[[List[Any]], List[Any]]:
    def read_list(elts: List[Any]) -> List[Any]:
        if isinstance(elts, list):
            return [read_elt(elt) for elt in elts]
        else:
            _atd_bad_json('array', elts)
    return read_list


def _atd_read_assoc_array_into_dict(
            read_key: Callable[[Any], Any],
            read_value: Callable[[Any], Any],
        ) -> Callable[[List[Any]], Dict[Any, Any]]:
    def read_assoc(elts: List[List[Any]]) -> Dict[str, Any]:
        if isinstance(elts, list):
            return {read_key(elt[0]): read_value(elt[1]) for elt in elts}
        else:
            _atd_bad_json('array', elts)
            raise AssertionError('impossible')  # keep mypy happy
    return read_assoc


def _atd_read_assoc_object_into_dict(
            read_value: Callable[[Any], Any]
        ) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
    def read_assoc(elts: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(elts, dict):
            return {_atd_read_string(k): read_value(v)
                    for k, v in elts.items()}
        else:
            _atd_bad_json('object', elts)
            raise AssertionError('impossible')  # keep mypy happy
    return read_assoc


def _atd_read_assoc_object_into_list(
            read_value: Callable[[Any], Any]
        ) -> Callable[[Dict[str, Any]], List[Tuple[str, Any]]]:
    def read_assoc(elts: Dict[str, Any]) -> List[Tuple[str, Any]]:
        if isinstance(elts, dict):
            return [(_atd_read_string(k), read_value(v))
                    for k, v in elts.items()]
        else:
            _atd_bad_json('object', elts)
            raise AssertionError('impossible')  # keep mypy happy
    return read_assoc


def _atd_read_nullable(read_elt: Callable[[Any], Any]) \
        -> Callable[[Optional[Any]], Optional[Any]]:
    def read_nullable(x: Any) -> Any:
        if x is None:
            return None
        else:
            return read_elt(x)
    return read_nullable


def _atd_write_unit(x: Any) -> None:
    if x is None:
        return x
    else:
        _atd_bad_python('unit', x)


def _atd_write_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    else:
        _atd_bad_python('bool', x)


def _atd_write_int(x: Any) -> int:
    if isinstance(x, int):
        return x
    else:
        _atd_bad_python('int', x)


def _atd_write_float(x: Any) -> float:
    if isinstance(x, (int, float)):
        return x
    else:
        _atd_bad_python('float', x)


def _atd_write_string(x: Any) -> str:
    if isinstance(x, str):
        return x
    else:
        _atd_bad_python('str', x)


def _atd_write_list(
            write_elt: Callable[[Any], Any]
        ) -> Callable[[List[Any]], List[Any]]:
    def write_list(elts: List[Any]) -> List[Any]:
        if isinstance(elts, list):
            return [write_elt(elt) for elt in elts]
        else:
            _atd_bad_python('list', elts)
    return write_list


def _atd_write_assoc_dict_to_array(
            write_key: Callable[[Any], Any],
            write_value: Callable[[Any], Any]
        ) -> Callable[[Dict[Any, Any]], List[Tuple[Any, Any]]]:
    def write_assoc(elts: Dict[str, Any]) -> List[Tuple[str, Any]]:
        if isinstance(elts, dict):
            return [(write_key(k), write_value(v)) for k, v in elts.items()]
        else:
            _atd_bad_python('Dict[str, <value type>]]', elts)
            raise AssertionError('impossible')  # keep mypy happy
    return write_assoc


def _atd_write_assoc_dict_to_object(
            write_value: Callable[[Any], Any]
        ) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
    def write_assoc(elts: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(elts, dict):
            return {_atd_write_string(k): write_value(v)
                    for k, v in elts.items()}
        else:
            _atd_bad_python('Dict[str, <value type>]', elts)
            raise AssertionError('impossible')  # keep mypy happy
    return write_assoc


def _atd_write_assoc_list_to_object(
            write_value: Callable[[Any], Any],
        ) -> Callable[[List[Any]], Dict[str, Any]]:
    def write_assoc(elts: List[List[Any]]) -> Dict[str, Any]:
        if isinstance(elts, list):
            return {_atd_write_string(elt[0]): write_value(elt[1])
                    for elt in elts}
        else:
            _atd_bad_python('List[Tuple[<key type>, <value type>]]', elts)
            raise AssertionError('impossible')  # keep mypy happy
    return write_assoc


def _atd_write_nullable(write_elt: Callable[[Any], Any]) \
        -> Callable[[Optional[Any]], Optional[Any]]:
    def write_nullable(x: Any) -> Any:
        if x is None:
            return None
        else:
            return write_elt(x)
    return write_nullable


############################################################################
# Public classes
############################################################################


# This was inserted by the user.
import deco
from dataclasses import dataclass


@dataclass
class RecursiveClass:
    """Original type: recursive_class = { ... }"""

    id: int
    flag: bool
    children: List[RecursiveClass]

    @classmethod
    def from_json(cls, x: Any) -> 'RecursiveClass':
        if isinstance(x, dict):
            return cls(
                id=_atd_read_int(x['id']) if 'id' in x else _atd_missing_json_field('RecursiveClass', 'id'),
                flag=_atd_read_bool(x['flag']) if 'flag' in x else _atd_missing_json_field('RecursiveClass', 'flag'),
                children=_atd_read_list(RecursiveClass.from_json)(x['children']) if 'children' in x else _atd_missing_json_field('RecursiveClass', 'children'),
            )
        else:
            _atd_bad_json('RecursiveClass', x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res['id'] = _atd_write_int(self.id)
        res['flag'] = _atd_write_bool(self.flag)
        res['children'] = _atd_write_list((lambda x: x.to_json()))(self.children)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> 'RecursiveClass':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Root_:
    """Original type: kind = [ ... | Root | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return 'Root_'

    @staticmethod
    def to_json() -> Any:
        return 'Root'

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Thing:
    """Original type: kind = [ ... | Thing of ... | ... ]"""

    value: int

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return 'Thing'

    def to_json(self) -> Any:
        return ['Thing', _atd_write_int(self.value)]

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class WOW:
    """Original type: kind = [ ... | WOW | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return 'WOW'

    @staticmethod
    def to_json() -> Any:
        return 'wow'

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Amaze:
    """Original type: kind = [ ... | Amaze of ... | ... ]"""

    value: List[str]

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return 'Amaze'

    def to_json(self) -> Any:
        return ['!!!', _atd_write_list(_atd_write_string)(self.value)]

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Kind:
    """Original type: kind = [ ... ]"""

    value: Union[Root_, Thing, WOW, Amaze]

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return self.value.kind

    @classmethod
    def from_json(cls, x: Any) -> 'Kind':
        if isinstance(x, str):
            if x == 'Root':
                return cls(Root_())
            if x == 'wow':
                return cls(WOW())
            _atd_bad_json('Kind', x)
        if isinstance(x, List) and len(x) == 2:
            cons = x[0]
            if cons == 'Thing':
                return cls(Thing(_atd_read_int(x[1])))
            if cons == '!!!':
                return cls(Amaze(_atd_read_list(_atd_read_string)(x[1])))
            _atd_bad_json('Kind', x)
        _atd_bad_json('Kind', x)

    def to_json(self) -> Any:
        return self.value.to_json()

    @classmethod
    def from_json_string(cls, x: str) -> 'Kind':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Alias:
    """Original type: alias"""

    value: List[int]

    @classmethod
    def from_json(cls, x: Any) -> 'Alias':
        return cls(_atd_read_list(_atd_read_int)(x))

    def to_json(self) -> Any:
        return _atd_write_list(_atd_write_int)(self.value)

    @classmethod
    def from_json_string(cls, x: str) -> 'Alias':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Root:
    """Original type: root = { ... }"""

    id: str
    await_: bool
    x___init__: float
    items: List[List[int]]
    extras: List[int]
    aliased: Alias
    point: Tuple[float, float]
    kinds: List[Kind]
    assoc1: List[Tuple[float, int]]
    assoc2: List[Tuple[str, int]]
    assoc3: Dict[float, int]
    assoc4: Dict[str, int]
    nullables: List[Optional[int]]
    untyped_things: List[Any]
    maybe: Optional[int] = None
    answer: int = 42

    @classmethod
    def from_json(cls, x: Any) -> 'Root':
        if isinstance(x, dict):
            return cls(
                id=_atd_read_string(x['ID']) if 'ID' in x else _atd_missing_json_field('Root', 'ID'),
                await_=_atd_read_bool(x['await']) if 'await' in x else _atd_missing_json_field('Root', 'await'),
                x___init__=_atd_read_float(x['__init__']) if '__init__' in x else _atd_missing_json_field('Root', '__init__'),
                items=_atd_read_list(_atd_read_list(_atd_read_int))(x['items']) if 'items' in x else _atd_missing_json_field('Root', 'items'),
                extras=_atd_read_list(_atd_read_int)(x['extras']) if 'extras' in x else [],
                aliased=Alias.from_json(x['aliased']) if 'aliased' in x else _atd_missing_json_field('Root', 'aliased'),
                point=(lambda x: (_atd_read_float(x[0]), _atd_read_float(x[1])) if isinstance(x, list) and len(x) == 2 else _atd_bad_json('array of length 2', x))(x['point']) if 'point' in x else _atd_missing_json_field('Root', 'point'),
                kinds=_atd_read_list(Kind.from_json)(x['kinds']) if 'kinds' in x else _atd_missing_json_field('Root', 'kinds'),
                assoc1=_atd_read_list((lambda x: (_atd_read_float(x[0]), _atd_read_int(x[1])) if isinstance(x, list) and len(x) == 2 else _atd_bad_json('array of length 2', x)))(x['assoc1']) if 'assoc1' in x else _atd_missing_json_field('Root', 'assoc1'),
                assoc2=_atd_read_assoc_object_into_list(_atd_read_int)(x['assoc2']) if 'assoc2' in x else _atd_missing_json_field('Root', 'assoc2'),
                assoc3=_atd_read_assoc_array_into_dict(_atd_read_float, _atd_read_int)(x['assoc3']) if 'assoc3' in x else _atd_missing_json_field('Root', 'assoc3'),
                assoc4=_atd_read_assoc_object_into_dict(_atd_read_int)(x['assoc4']) if 'assoc4' in x else _atd_missing_json_field('Root', 'assoc4'),
                nullables=_atd_read_list(_atd_read_nullable(_atd_read_int))(x['nullables']) if 'nullables' in x else _atd_missing_json_field('Root', 'nullables'),
                untyped_things=_atd_read_list((lambda x: x))(x['untyped_things']) if 'untyped_things' in x else _atd_missing_json_field('Root', 'untyped_things'),
                maybe=_atd_read_int(x['maybe']) if 'maybe' in x else None,
                answer=_atd_read_int(x['answer']) if 'answer' in x else 42,
            )
        else:
            _atd_bad_json('Root', x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res['ID'] = _atd_write_string(self.id)
        res['await'] = _atd_write_bool(self.await_)
        res['__init__'] = _atd_write_float(self.x___init__)
        res['items'] = _atd_write_list(_atd_write_list(_atd_write_int))(self.items)
        res['extras'] = _atd_write_list(_atd_write_int)(self.extras)
        res['aliased'] = (lambda x: x.to_json())(self.aliased)
        res['point'] = (lambda x: [_atd_write_float(x[0]), _atd_write_float(x[1])] if isinstance(x, tuple) and len(x) == 2 else _atd_bad_python('tuple of length 2', x))(self.point)
        res['kinds'] = _atd_write_list((lambda x: x.to_json()))(self.kinds)
        res['assoc1'] = _atd_write_list((lambda x: [_atd_write_float(x[0]), _atd_write_int(x[1])] if isinstance(x, tuple) and len(x) == 2 else _atd_bad_python('tuple of length 2', x)))(self.assoc1)
        res['assoc2'] = _atd_write_assoc_list_to_object(_atd_write_int)(self.assoc2)
        res['assoc3'] = _atd_write_assoc_dict_to_array(_atd_write_float, _atd_write_int)(self.assoc3)
        res['assoc4'] = _atd_write_assoc_dict_to_object(_atd_write_int)(self.assoc4)
        res['nullables'] = _atd_write_list(_atd_write_nullable(_atd_write_int))(self.nullables)
        res['untyped_things'] = _atd_write_list((lambda x: x))(self.untyped_things)
        if self.maybe is not None:
            res['maybe'] = _atd_write_int(self.maybe)
        res['answer'] = _atd_write_int(self.answer)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> 'Root':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@deco.deco1
@deco.deco2(42)
@dataclass(order=True)
class RequireField:
    """Original type: require_field = { ... }"""

    req: str

    @classmethod
    def from_json(cls, x: Any) -> 'RequireField':
        if isinstance(x, dict):
            return cls(
                req=_atd_read_string(x['req']) if 'req' in x else _atd_missing_json_field('RequireField', 'req'),
            )
        else:
            _atd_bad_json('RequireField', x)

    def to_json(self) -> Any:
        res: Dict[str, Any] = {}
        res['req'] = _atd_write_string(self.req)
        return res

    @classmethod
    def from_json_string(cls, x: str) -> 'RequireField':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass
class Pair:
    """Original type: pair"""

    value: Tuple[str, int]

    @classmethod
    def from_json(cls, x: Any) -> 'Pair':
        return cls((lambda x: (_atd_read_string(x[0]), _atd_read_int(x[1])) if isinstance(x, list) and len(x) == 2 else _atd_bad_json('array of length 2', x))(x))

    def to_json(self) -> Any:
        return (lambda x: [_atd_write_string(x[0]), _atd_write_int(x[1])] if isinstance(x, tuple) and len(x) == 2 else _atd_bad_python('tuple of length 2', x))(self.value)

    @classmethod
    def from_json_string(cls, x: str) -> 'Pair':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class A:
    """Original type: frozen = [ ... | A | ... ]"""

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return 'A'

    @staticmethod
    def to_json() -> Any:
        return 'A'

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class B:
    """Original type: frozen = [ ... | B of ... | ... ]"""

    value: int

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return 'B'

    def to_json(self) -> Any:
        return ['B', _atd_write_int(self.value)]

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)


@dataclass(frozen=True)
class Frozen:
    """Original type: frozen = [ ... ]"""

    value: Union[A, B]

    @property
    def kind(self) -> str:
        """Name of the class representing this variant."""
        return self.value.kind

    @classmethod
    def from_json(cls, x: Any) -> 'Frozen':
        if isinstance(x, str):
            if x == 'A':
                return cls(A())
            _atd_bad_json('Frozen', x)
        if isinstance(x, List) and len(x) == 2:
            cons = x[0]
            if cons == 'B':
                return cls(B(_atd_read_int(x[1])))
            _atd_bad_json('Frozen', x)
        _atd_bad_json('Frozen', x)

    def to_json(self) -> Any:
        return self.value.to_json()

    @classmethod
    def from_json_string(cls, x: str) -> 'Frozen':
        return cls.from_json(json.loads(x))

    def to_json_string(self, **kw: Any) -> str:
        return json.dumps(self.to_json(), **kw)
