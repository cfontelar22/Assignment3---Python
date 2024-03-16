import dash
from dash import dcc, html, dash_table  
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.read_csv("/home/cfontelar/Assignment3/Tree_Inventory.csv")

# Preparing data for plotting
common_name_counts = df['Common Name'].value_counts().reset_index()
common_name_counts.columns = ['Common Name', 'Count']  # Renaming columns for clarity

# Creating the bar plot
fig = px.bar(common_name_counts, x='Common Name', y='Count', labels={'Common Name': 'Common Name', 'Count': 'Count'}, title='Count of Trees by Common Name')

# Defining app layout with a DataTable for displaying DataFrame data
app.layout = html.Div(children=[
    html.H1(children='Winnipeg Tree Inventory Data'),
    dcc.Graph(id='tree-common-name-graph', figure=fig),
    html.H2('Tree Counts by Common Name'),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in common_name_counts.columns],  # Defines table columns
        data=common_name_counts.to_dict('records'),  # Converts DataFrame to a list of dictionaries for the DataTable
        style_table={'overflowX': 'auto'},  # Styles for the table to enable horizontal scrolling
        filter_action="native",  # Enables filtering of data by user input
        sort_action="native",  # Enables data sorting
        sort_mode="multi",  # Allows multi-column sort
        column_selectable="single",  # Allows users to select a single column
        row_selectable="multi",  # Allows users to select multiple rows
        page_action="native",  # Enables table pagination
        page_current=0,  # Sets the initial page
        page_size=10,  # Sets the number of rows per page
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
gi