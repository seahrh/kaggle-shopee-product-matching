__all__ = [
    "target_label",
    "metric_per_row",
    "combine_as_list",
    "combine_as_string",
    "phash_matches",
    "sbert_matches",
    "preprocess",
    "efficient_net",
]

from .translation import *
from .stopwords import *

__all__ += translation.__all__  # type: ignore  # module name is not defined
__all__ += stopwords.__all__  # type: ignore  # module name is not defined

import re
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.neighbors import NearestNeighbors
from sentence_transformers import SentenceTransformer
from typing import Set, List, Callable, Any, Iterable
from scml.nlp import to_ascii_str, expand_contractions, decode_escaped_bytes


def target_label(df: pd.DataFrame) -> pd.Series:
    tmp = df.groupby("label_group")["posting_id"].unique().to_dict()
    return df["label_group"].map(tmp)


def metric_per_row(prediction: str, target: str = "target") -> Callable[[Any], float]:
    def f1(row) -> float:
        n = len(np.intersect1d(row[target], row[prediction]))
        return 2 * n / (len(row[target]) + len(row[prediction]))

    return f1


def combine_as_list(cols: Iterable[str]) -> Callable:
    def fn(row) -> List[str]:
        s: Set[str] = set()
        s.add(row["posting_id"])
        for col in cols:
            s |= set(row[col])
        return list(s)

    return fn


def combine_as_string(cols: Iterable[str]) -> Callable:
    def fn(row) -> str:
        s: Set[str] = set()
        s.add(row["posting_id"])
        for col in cols:
            s |= set(row[col])
        return " ".join(s)

    return fn


def phash_matches(
    df: pd.DataFrame, threshold: float, n_neighbors: int = 49, hash_length: int = 16
) -> List[List[str]]:
    rows = []
    for t in df.itertuples():
        ph = getattr(t, "image_phash")
        if len(ph) != hash_length:
            raise ValueError(f"expected len(ph) is {hash_length} but found {len(ph)}")
        row = {}
        for i in range(hash_length):
            row[f"ph{i}"] = int(ph[i], 16)
        rows.append(row)
    x = pd.DataFrame.from_records(rows)
    x = x.astype(np.int8)
    nn = NearestNeighbors(n_neighbors=min(n_neighbors, len(x) - 1), metric="hamming")
    nn.fit(x)
    distances, indices = nn.kneighbors()
    res: List[List[str]] = [[] for _ in range(len(indices))]
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if distances[i][j] > threshold:
                break
            res[i].append(df.iloc[indices[i][j]]["posting_id"])
    return res


def sbert_matches(
    model_path: str,
    sentences: List[str],
    posting_ids: List[str],
    threshold: float,
    n_neighbors: int = 49,
    max_seq_length: int = 512,
) -> List[List[str]]:
    model = SentenceTransformer(model_path)
    model.max_seq_length = max_seq_length
    em = model.encode(
        sentences,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    nn = NearestNeighbors(
        n_neighbors=min(n_neighbors, len(posting_ids) - 1), metric="euclidean"
    )
    nn.fit(em)
    distances, indices = nn.kneighbors()
    res: List[List[str]] = [[] for _ in range(len(indices))]
    for i in range(len(indices)):
        for j in range(len(indices[0])):
            if distances[i][j] > threshold:
                break
            res[i].append(posting_ids[indices[i][j]])
    return res


_byte_string_literal_pattern = re.compile(r'^b"(.*)"$')
_escaped_bytes_pattern = re.compile(r"\\x[\dabcdef]{2}")


def _remove_byte_string_literal(s: str) -> str:
    m = _byte_string_literal_pattern.match(s)
    if m is None:
        return s
    return m.group(1)


def _remove_escaped_bytes(s: str) -> str:
    return _escaped_bytes_pattern.sub("", s)


def preprocess(column: str) -> Callable:
    def fn(row) -> str:
        res: str = row[column]
        res = _remove_byte_string_literal(res)
        res = decode_escaped_bytes(res)
        res = to_ascii_str(res)
        res = hand_translate(res)
        res = expand_contractions(res)
        res = remove_stopwords(res)
        return res

    return fn


def efficient_net(variant: str, directory: str, pooling: str):
    res = keras.applications.EfficientNetB0(
        include_top=False,
        input_shape=(224, 224, 3),
        pooling=pooling,
        weights=f"{directory}/efficientnetb0_notop.h5",
    )
    if variant == "efficientnetb1":
        res = keras.applications.EfficientNetB1(
            include_top=False,
            input_shape=(240, 240, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb1_notop.h5",
        )
    elif variant == "efficientnetb2":
        res = keras.applications.EfficientNetB2(
            include_top=False,
            input_shape=(260, 260, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb2_notop.h5",
        )
    elif variant == "efficientnetb3":
        res = keras.applications.EfficientNetB3(
            include_top=False,
            input_shape=(300, 300, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb3_notop.h5",
        )
    elif variant == "efficientnetb4":
        res = keras.applications.EfficientNetB4(
            include_top=False,
            input_shape=(380, 380, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb4_notop.h5",
        )
    elif variant == "efficientnetb5":
        res = keras.applications.EfficientNetB5(
            include_top=False,
            input_shape=(456, 456, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb5_notop.h5",
        )
    elif variant == "efficientnetb6":
        res = keras.applications.EfficientNetB6(
            include_top=False,
            input_shape=(528, 528, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb6_notop.h5",
        )
    elif variant == "efficientnetb7":
        res = keras.applications.EfficientNetB7(
            include_top=False,
            input_shape=(600, 600, 3),
            pooling=pooling,
            weights=f"{directory}/efficientnetb7_notop.h5",
        )
    return res
