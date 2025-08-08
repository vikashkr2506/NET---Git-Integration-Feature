
import pandas as pd
from codex_widget_factory_lite.visuals.grid_table import GridTable
# Hardcoding a sample dataframe here, please ingest your dataset or create
sample_df = pd.DataFrame(data = [['tom', 'john', 10], ['nick', 'jack', 15], ['juli', 'jill', 12]],
                         columns=['Name', 'Parent', 'Age'])

# Creating grid_options object with pagination and quick search options
grid_options = {
    "enablePagination":True,
    "paginationSettings": {"rowsPerPageOptions": [10, 20, 30], "rowsPerPage": 10},
    "quickSearch": True
}

# Making 'Age' column sortable
col_props = {'Age':{'sortable':True}}
gridtable_output=GridTable(df = sample_df, col_props=col_props, grid_options=grid_options)
gridtable_output.add_tooltip(isTooltip=True,tooltip_text="This is a tooltip",placement="top")
dynamic_outputs = gridtable_output.json_string
