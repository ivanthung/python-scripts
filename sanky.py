import yaml
import plotly.graph_objects as go

# Load data from YAML file
with open('data.yaml') as file:
    data = yaml.full_load(file)

# Extract nodes
nodes = data['nodes']

# Create labels for the nodes
labels = [node['id'] for node in nodes]

# Extract links
links = data['links']

# Create source, target, and value for the links
source = [labels.index(link['source']) for link in links]
target = [labels.index(link['target']) for link in links]
value = [link['value'] for link in links]

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    )
)])

fig.update_layout(title_text=data['title'], font_size=10)
fig.show()