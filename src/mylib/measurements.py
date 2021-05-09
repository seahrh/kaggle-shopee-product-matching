import re
from re import Pattern
from typing import Tuple, Set, NamedTuple

__all__ = ["Measurement", "get_measurements"]

FLAGS = re.IGNORECASE


class Rule(NamedTuple):
    pattern: Pattern
    uom: str
    scale: int


class Measurement(NamedTuple):
    quantity: float
    uom: str


RULES: Tuple[Rule, ...] = tuple(
    [
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(g|gr|grams?)\b", FLAGS),
            uom="gram",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(kg|kilos?|kilograms?)\b", FLAGS),
            uom="gram",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(
                r"\b(\d+(\.\d+)?)\s*(mm|millimetres?|millimeters?)\b", FLAGS
            ),
            uom="millimetre",
            scale=1,
        ),
        Rule(
            pattern=re.compile(
                r"\b(\d+(\.\d+)?)\s*(cm|centimetres?|centimeters?)\b", FLAGS
            ),
            uom="millimetre",
            scale=10,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(m|metres?|meters?)\b", FLAGS),
            uom="millimetre",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(
                r"\b(\d+(\.\d+)?)\s*(ml|millilitres?|milliliters?)\b", FLAGS
            ),
            uom="millilitre",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(l|litres?|liters?)\b", FLAGS),
            uom="millilitre",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*mi?b\b", FLAGS),
            uom="megabyte",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*gi?b\b", FLAGS),
            uom="megabyte",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*mhz\b", FLAGS),
            uom="megahertz",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*ghz\b", FLAGS),
            uom="megahertz",
            scale=1000,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(pcs?|pieces?)\b", FLAGS),
            uom="piece",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(boxs?|boxes)\b", FLAGS),
            uom="box",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*(pkts?|packets?)\b", FLAGS),
            uom="packet",
            scale=1,
        ),
        Rule(
            pattern=re.compile(r"\b(\d+(\.\d+)?)\s*bottles?\b", FLAGS),
            uom="bottle",
            scale=1,
        ),
    ]
)

MULTIPLE_LENGTHS = re.compile(r"\b(\d+)\s*x\s*(\d+)\s*x?\s*(\d+)?\b", FLAGS)


def get_measurements(s: str, rules: Tuple[Rule, ...] = RULES) -> Set[Measurement]:
    res = set()
    m = MULTIPLE_LENGTHS.search(s)
    if m:
        for g in m.groups():
            if g:
                mt = Measurement(quantity=int(g), uom="millimetre")
                res.add(mt)
    for r in rules:
        matches = r.pattern.findall(s)
        for m in matches:
            if m:
                mt = Measurement(quantity=float(m[0]) * r.scale, uom=r.uom)
                res.add(mt)
    return res
