import pm4py
import pandas as pd

log = pm4py.read_xes("log.xes")


from pm4py.statistics.variants.log import get as variants_get
variants = variants_get.get_variants(log)

from collections import Counter
c = Counter({k: len(v) for k,v in variants.items()})
for v,f in c.most_common(10):
    print(f, ":", v)

from pm4py.objects.conversion.log import converter as log_converter

df = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)

df = df.rename(columns={
    "case:concept:name": "case",
    "concept:name": "activity",
    "time:timestamp": "timestamp"
})
df["activity"] = df["activity"].str.upper().str.strip().str.replace(" ", "_")
df.head()