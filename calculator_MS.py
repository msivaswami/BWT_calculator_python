import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import sys


# Function to calculate the size of a string in bytes
def calculate_size(input_string):
    size_in_bytes = sys.getsizeof(input_string)
    return size_in_bytes


# Predefined options for strings
strings_to_process = [
    "GATTACA",
    "ATTACATTAC",
    "ATATATATATA",
    "ATATATATAT",
    "AATAATAATAAT",
    "AAAATAAATAAA",
    "ATATACACACA",
    "ATATGTATACAT"
]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Calculating the String Size"),

    dcc.Checklist(
        id='use_predefined',
        options=[{'label': 'Use predefined strings?', 'value': True}],
        value=[True]
    ),

    dcc.Input(id='input_string_custom', type='text', value='', style={'width': '50%'}),

    dcc.Dropdown(
        id='input_string',
        options=[{'label': string, 'value': string} for string in strings_to_process],
        value=strings_to_process[0],
        style={'width': '50%'}
    ),

    html.Div(id='output_size')
])


# Define callback to update the output based on user input
@app.callback(
    Output('output_size', 'children'),
    [Input('use_predefined', 'value'),
     Input('input_string_custom', 'value'),
     Input('input_string', 'value')]
)
def update_output(use_predefined, input_string_custom, input_string):
    if use_predefined:
        input_string = input_string
    else:
        input_string = input_string_custom

    size_in_bytes = calculate_size(input_string)
    return f"Size in bytes: {size_in_bytes}"


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
