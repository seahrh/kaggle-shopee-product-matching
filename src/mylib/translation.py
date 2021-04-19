import re
from typing import Any, NamedTuple, Tuple

__all__ = ["hand_translate"]


class Rule(NamedTuple):
    pattern: Any
    replacement: str


FLAGS = re.IGNORECASE

TRANSLATIONS: Tuple[Rule, ...] = tuple(
    [
        Rule(pattern=re.compile(r"\bwanita\b", FLAGS), replacement="women"),
        Rule(pattern=re.compile(r"\banak\b", FLAGS), replacement="child"),
        Rule(pattern=re.compile(r"\bbayi\b", FLAGS), replacement="baby"),
        Rule(pattern=re.compile(r"\btas\b", FLAGS), replacement="bag"),
        Rule(pattern=re.compile(r"\bmasker\b", FLAGS), replacement="face mask"),
        Rule(pattern=re.compile(r"\bpria\b", FLAGS), replacement="men"),
        Rule(pattern=re.compile(r"\bmurah\b", FLAGS), replacement="cheap"),
        Rule(pattern=re.compile(r"\btangan\b", FLAGS), replacement="hand"),
        Rule(pattern=re.compile(r"\balat\b", FLAGS), replacement="tool"),
        Rule(pattern=re.compile(r"\bmotif\b", FLAGS), replacement="motive"),
        Rule(pattern=re.compile(r"\bwarna\b", FLAGS), replacement="color"),
        Rule(pattern=re.compile(r"\bbahan\b", FLAGS), replacement="material"),
        Rule(pattern=re.compile(r"\bcelana\b", FLAGS), replacement="pants"),
        Rule(pattern=re.compile(r"\bbaju\b", FLAGS), replacement="clothes"),
        Rule(pattern=re.compile(r"\bkaos\b", FLAGS), replacement="t-shirt"),
        Rule(pattern=re.compile(r"\bsepatu\b", FLAGS), replacement="shoes"),
        Rule(pattern=re.compile(r"\brambut\b", FLAGS), replacement="hair"),
        Rule(pattern=re.compile(r"\bmainan\b", FLAGS), replacement="toy"),
        Rule(
            pattern=re.compile(r"\bsar[uo]ng\b", FLAGS),
            replacement="wrap knot cover lower body",
        ),
        Rule(pattern=re.compile(r"\bpolos\b", FLAGS), replacement="plain"),
        Rule(pattern=re.compile(r"\brak\b", FLAGS), replacement="rack"),
        Rule(pattern=re.compile(r"\bbotol\b", FLAGS), replacement="bottle"),
        Rule(pattern=re.compile(r"\bsabun\b", FLAGS), replacement="soap"),
        Rule(pattern=re.compile(r"\bkain\b", FLAGS), replacement="fabric"),
        Rule(pattern=re.compile(r"\bpanjang\b", FLAGS), replacement="long"),
        Rule(pattern=re.compile(r"\bkabel\b", FLAGS), replacement="cable"),
        Rule(pattern=re.compile(r"\bbuku\b", FLAGS), replacement="book"),
        Rule(pattern=re.compile(r"\bplastik\b", FLAGS), replacement="plastic"),
        Rule(pattern=re.compile(r"\bmobil\b", FLAGS), replacement="car"),
        Rule(pattern=re.compile(r"\bhitam\b", FLAGS), replacement="black"),
        Rule(pattern=re.compile(r"\bkarakter\b", FLAGS), replacement="character"),
        Rule(pattern=re.compile(r"\bputih\b", FLAGS), replacement="white"),
        Rule(pattern=re.compile(r"\bdompet\b", FLAGS), replacement="purse"),
        Rule(pattern=re.compile(r"\bkaki\b", FLAGS), replacement="feet"),
        Rule(pattern=re.compile(r"\bpembersih\b", FLAGS), replacement="cleaners"),
        Rule(pattern=re.compile(r"\blipat\b", FLAGS), replacement="folding"),
        Rule(pattern=re.compile(r"\bsilikon\b", FLAGS), replacement="silicone"),
        Rule(pattern=re.compile(r"\bminyak\b", FLAGS), replacement="oil"),
        Rule(pattern=re.compile(r"\bisi\b", FLAGS), replacement="contents"),
        Rule(pattern=re.compile(r"\bpaket\b", FLAGS), replacement="package"),
        Rule(pattern=re.compile(r"\bsusu\b", FLAGS), replacement="milk"),
        Rule(pattern=re.compile(r"\bgamis\b", FLAGS), replacement="robe"),
        Rule(pattern=re.compile(r"\bmandi\b", FLAGS), replacement="bath"),
        Rule(pattern=re.compile(r"\bmadu\b", FLAGS), replacement="honey"),
        Rule(pattern=re.compile(r"\bkulit\b", FLAGS), replacement="skin"),
        Rule(pattern=re.compile(r"\bserbaguna\b", FLAGS), replacement="multi-purpose"),
        Rule(pattern=re.compile(r"\bbisa\b", FLAGS), replacement="can"),
        Rule(pattern=re.compile(r"\bkacamata\b", FLAGS), replacement="spectacles"),
        Rule(pattern=re.compile(r"\bpendek\b", FLAGS), replacement="short"),
        Rule(pattern=re.compile(r"\btali\b", FLAGS), replacement="rope"),
        Rule(pattern=re.compile(r"\bselempang\b", FLAGS), replacement="sash"),
        Rule(pattern=re.compile(r"\btopi\b", FLAGS), replacement="hat"),
        Rule(pattern=re.compile(r"\bobat\b", FLAGS), replacement="drug"),
        Rule(pattern=re.compile(r"\bgantungan\b", FLAGS), replacement="hanger"),
        Rule(pattern=re.compile(r"\btahun\b", FLAGS), replacement="year"),
        Rule(
            pattern=re.compile(r"\bjilbab\b", FLAGS),
            replacement="religious women head covering",
        ),
        Rule(pattern=re.compile(r"\bdapur\b", FLAGS), replacement="kitchen"),
        Rule(pattern=re.compile(r"\bdinding\b", FLAGS), replacement="wall"),
        Rule(pattern=re.compile(r"\bkuas\b", FLAGS), replacement="brush"),
        Rule(pattern=re.compile(r"\bperempuan\b", FLAGS), replacement="woman"),
        Rule(pattern=re.compile(r"\bkatun\b", FLAGS), replacement="cotton"),
        Rule(pattern=re.compile(r"\bsepeda\b", FLAGS), replacement="bike"),
        Rule(pattern=re.compile(r"\blucu\b", FLAGS), replacement="funny"),
        Rule(pattern=re.compile(r"\blengan\b", FLAGS), replacement="arm"),
        Rule(pattern=re.compile(r"\bkaca\b", FLAGS), replacement="glass"),
        Rule(pattern=re.compile(r"\bgaransi\b", FLAGS), replacement="warranty"),
        Rule(pattern=re.compile(r"\bbunga\b", FLAGS), replacement="flower"),
        Rule(pattern=re.compile(r"\bhanduk\b", FLAGS), replacement="towel"),
        Rule(pattern=re.compile(r"\bdewasa\b", FLAGS), replacement="adult"),
        Rule(pattern=re.compile(r"\belektrik\b", FLAGS), replacement="electric"),
        Rule(pattern=re.compile(r"\btimbangan\b", FLAGS), replacement="balance"),
        Rule(pattern=re.compile(r"\bbesar\b", FLAGS), replacement="big"),
        Rule(pattern=re.compile(r"\bbahan\b", FLAGS), replacement="ingredient"),
        Rule(pattern=re.compile(r"\bransel\b", FLAGS), replacement="backpack"),
        Rule(pattern=re.compile(r"\bkertas\b", FLAGS), replacement="paper"),
        Rule(pattern=re.compile(r"\bgrosir\b", FLAGS), replacement="wholesaler"),
        Rule(pattern=re.compile(r"\blampu\b", FLAGS), replacement="light"),
        Rule(pattern=re.compile(r"\buntuk\b", FLAGS), replacement="to"),
        Rule(pattern=re.compile(r"\bdan\b", FLAGS), replacement="and"),
        Rule(pattern=re.compile(r"\btempat\b", FLAGS), replacement="place"),
        Rule(pattern=re.compile(r"\bwajah\b", FLAGS), replacement="face"),
        Rule(pattern=re.compile(r"\btermurah\b", FLAGS), replacement="cheapest"),
        Rule(pattern=re.compile(r"\bparfum\b", FLAGS), replacement="perfume"),
        Rule(pattern=re.compile(r"\bdengan\b", FLAGS), replacement="with"),
    ]
)


def hand_translate(s: str, rules: Tuple[Rule, ...] = TRANSLATIONS) -> str:
    res = s
    for r in rules:
        res = r.pattern.sub(r.replacement, res)
    return res
