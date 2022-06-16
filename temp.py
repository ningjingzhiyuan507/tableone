import os

import pandas as pd

from tableone import TableOne, load_dataset

# df = load_dataset('pn2012')
df = pd.DataFrame(
    {
        'a': [1, 2, 3, 4],
        'b': [None] * 4,
        'c': [None] * 4,
    }
)
result = TableOne(df, columns=['b', 'c'])
print(result)
