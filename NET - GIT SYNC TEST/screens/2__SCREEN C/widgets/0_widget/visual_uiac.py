import pandas as pd
from codex_widget_factory_lite.visuals.expandable_table import ExpandableTable
# Hardcoding a sample dataframe here, please ingest you dataset or create
expandable_df = pd.DataFrame(
    columns=['Region', 'Country', 'Category'],
    data=[
        ['North America', 'USA', 'Category 1'],
        ['North America', 'USA', 'Category 2'],
        ['North America', 'Canada', 'Category 1'],
        ['North America', 'Canada', 'Category 2']
    ]
)
expandable_rows_flag = [True, True, True, False]
expandable_rows_values = [{"Name":{"0":"tom"},"Age":{"0":10}},
    {"Name":{"1":"nick","2":"juli"},"Age":{"1":15,"2":14}}, {"Name":{"0" : "user-1"}, "Age": {"0": 20}}, False]
expandable_cell_editor_config = {
    "Country": {"cellEditor": "text",},
    "Name": {"cellEditor": "text",},
    "Age": {"cellEditor": "number_outline",}
}
output= ExpandableTable(expandable_df = expandable_df,
  expandable_rows_flag = expandable_rows_flag,
  expandable_rows_values = expandable_rows_values,
  expandable_cell_editor_config = expandable_cell_editor_config,
  editorMode=True)
output.add_tooltip(isTooltip=True,tooltip_text="This is a tooltip" ,placement="top")
dynamic_outputs =output.json_string

