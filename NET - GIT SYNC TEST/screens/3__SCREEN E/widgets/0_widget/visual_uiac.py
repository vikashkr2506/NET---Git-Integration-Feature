import pandas as pd
from codex_widget_factory_lite.visuals.simple_table import SimpleTable
# Hardcoding a sample dataframe here, please ingest you dataset or create
sample_df = pd.DataFrame(data = [['tom','US',10], ['nick','US',15],
    ['juli','US',14]], columns=['Name','country','Age'])
simpletable_output= SimpleTable(df = sample_df)
simpletable_output.add_tooltip(isTooltip=True,tooltip_text="This is a tooltip",placement="top")
dynamic_outputs = simpletable_output.json_string
