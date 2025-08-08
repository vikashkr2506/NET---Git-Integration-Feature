import pandas as pd
from codex_widget_factory_lite.visuals.expandable_table import ExpandableTable
# Hardcoding a sample dataframe here, please ingest you dataset or create
expandable_df = pd.DataFrame(
    columns=['Region', 'Country', 'Random Metric'],
    data=[
        ['North America', 'USA', 100],
        ['North America', 'USA', 200],
        ['North America', 'Canada', 10],
        ['North America', 'Canada', 20],
    ]
)
value_cols_aggfunc_dict = { "Random Metric": "sum" }
output= ExpandableTable(expandable_df = expandable_df,
  value_cols_aggfunc_dict = value_cols_aggfunc_dict)
output.add_tooltip(isTooltip=True,tooltip_text="This is a tooltip" ,placement="top")
dynamic_outputs=output.json_string
