from codex_widget_factory_lite.visuals.plotly_graph import PlotlyGraph
import plotly.graph_objects as go
import json

fig = go.Figure()
fig.add_trace(go.Bar(name="first", x=["a", "b"], y=[1,2]))
fig.add_trace(go.Bar(name="second", x=["a", "b"], y=[2,1]))
fig.add_trace(go.Bar(name="third", x=["a", "b"], y=[1,2]))
fig.add_trace(go.Bar(name="fourth", x=["a", "b"], y=[2,1]))

fig.update_layout(
    showlegend = True,
    legend={
        "orientation":"h",
        'x':0.03,
        'y':-0.09
    }
)
plotly_json = PlotlyGraph(plot_object = fig).component_dict
plotly_json['layout']['marginOverride']=dict(t=0, r=100, l=0, b=50)
dynamic_outputs = json.dumps(plotly_json)

