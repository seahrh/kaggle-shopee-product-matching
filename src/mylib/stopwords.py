import re
from typing import Any, NamedTuple, Tuple

__all__ = ["remove_stopwords"]


class Rule(NamedTuple):
    pattern: Any
    replacement: str


FLAGS = re.IGNORECASE

STOPWORDS: Tuple[Rule, ...] = tuple(
    [
        Rule(pattern=re.compile(r"\b\d{1,2}\.\d{1,2}\b", FLAGS), replacement=""),
        # paste generated rules below
        Rule(pattern=re.compile(r"\ba\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\babout\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\babove\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bactual\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bafter\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bagain\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bagainst\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bain\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\ball\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bam\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\ban\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\band\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bany\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bare\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\baha\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bas\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bat\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bauthentic\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bavail(able)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbasic\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbe\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbecause\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbeen\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbest\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbefore\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbeing\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbelow\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbetween\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbonus\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bboth\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbrand(ed)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bbut\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bby\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bcan\b", FLAGS), replacement=""),
        Rule(
            pattern=re.compile(r"\b(cod|cash\W+on\W+delivery)\b", FLAGS), replacement=""
        ),
        Rule(pattern=re.compile(r"\bcasual\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bcheap\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bcheapest\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bcute\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\b(days?|daily)\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdelicious\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdelivery\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdid\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdidn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdiscount\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdo\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdoes\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdoesn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdoing\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdon\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bdown\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bduring\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\beach\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\beasy\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bedition\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bever\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfake\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfalse\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfashion(able)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfast\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfew\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bflash\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfor(ever)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfree\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfrom\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bfurther\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bgenuine\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bgift\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bguarantee[d]?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhad\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhadn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhas\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhasn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhave\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhaven\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhaving\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhe\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bher\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhere\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhers\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bherself\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhim\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhimself\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhis\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\b(hours?|hourly)\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bhow\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bi\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bif\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bimport\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bin\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\binstant\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\binto\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bis\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bisn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bit\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bits\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bitself\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bjust\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\blast[s]?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bll\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\blocal\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\blogo\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\blol\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bm\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bma\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bme\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bmightn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bmore\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bmost\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bmustn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bmy\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bmyself\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bneedn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bnew\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bno\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bnor\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bnormal\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bnot\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bnote\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bnow\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bo\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bof\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\boff(er)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bofficial\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bon\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bonce\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bonly\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bor\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\boriginal\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bother\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bour\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bours\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bourselves\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bout\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bover(all)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bown\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bperfect\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bpopular\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bpremium\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bproduct\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bpromo(tion)?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bquality\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\brandom\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\breal\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bready\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\breceipt\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bs\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\b(big\W*)?sale\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bsame\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\b(re|best)?seller\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bsimple\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bshe\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bshould\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bshipping\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bso\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bsome\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bstock[s]?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bsuch\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bt\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthan\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthat\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthe\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\btheir\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\btheirs\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthem\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthemselves\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthen\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthere\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthese\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthey\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthis\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthose\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bthrough\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\btoo?\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\btrue\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bunder\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\buntil\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bultimate\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bup\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bve\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bvery\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwas\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwasn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwe\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwere\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bweren\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhat\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhen\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhere\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhich\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhile\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwho\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhom\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwhy\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwill\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwith\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwon\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\bwouldn\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\by\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\byou\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\byour\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\byours\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\byourself\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\byourselves\b", FLAGS), replacement=""),
        Rule(pattern=re.compile(r"\byummy\b", FLAGS), replacement=""),
    ]
)


def remove_stopwords(s: str, rules: Tuple[Rule, ...] = STOPWORDS) -> str:
    res = s
    for r in rules:
        res = r.pattern.sub(r.replacement, res)
    return res
