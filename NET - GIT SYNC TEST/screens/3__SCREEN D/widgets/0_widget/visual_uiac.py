import pandas as pd
from codex_widget_factory_lite.visuals.simple_table import SimpleTable
# Hardcoding a sample dataframe here, please ingest you dataset or create
sample_df = pd.DataFrame(data = [['tom', 10], ['nick', 15],
    ['juli', 14]], columns=['Name', 'Age'])
color_df = pd.DataFrame(['red','green','red'], columns=['Age'])
dynamic_outputs = SimpleTable(df = sample_df, color_df=color_df).json_string

