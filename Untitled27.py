#!/usr/bin/env python
# coding: utf-8

# In[3]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Analysis Dashboard"

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Sales Statistics', 'value': 'Yearly Sales Statistics'},
    {'label': 'Recession Period Sales Statistics', 'value': 'Recession Period Sales Statistics'}
]

# Create the layout of the app
app.layout = html.Div([
    # Title of the dashboard
    html.H1("Automobile Sales Analysis Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Dropdown menu for selecting options
    dcc.Dropdown(
        id='dropdown-menu',
        options=dropdown_options,
        value='Yearly Sales Statistics',  # Default value
        style={'width': '50%'}
    ),
    
    # Placeholder for the graph
    dcc.Graph(id='line-plot')
])

# Define the callback to update the graph based on dropdown selection
@app.callback(
    Output('line-plot', 'figure'),
    [Input('dropdown-menu', 'value')]
)
def update_graph(selected_option):
    if selected_option == 'Yearly Sales Statistics':
        # Filter and process the data for yearly statistics
        df_yearly = data.groupby('Year').agg({'Automobile_Sales': 'sum'}).reset_index()
        fig = px.line(df_yearly, x='Year', y='Automobile_Sales', title='Yearly Sales Statistics')
    elif selected_option == 'Recession Period Sales Statistics':
        # Example recession periods (for demonstration)
        recession_periods = {
            '1980-1982': [1980, 1981, 1982],
            '1990-1991': [1990, 1991],
            '2007-2009': [2007, 2008, 2009]
        }
        # Create a new DataFrame to store recession period statistics
        df_recession = data[data['Year'].isin([year for years in recession_periods.values() for year in years])]
        df_recession = df_recession.groupby(['Year']).agg({'Automobile_Sales': 'sum'}).reset_index()
        
        fig = px.bar(df_recession, x='Year', y='Automobile_Sales', 
                     title='Sales During Recession Periods')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[4]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Analysis Dashboard"

# Create the dropdown menu options
dropdown_statistics_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024)]

# Create the layout of the app
app.layout = html.Div([
    # Title of the dashboard
    html.H1("Automobile Sales Analysis Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Dropdown menu for selecting statistics
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_statistics_options,
            value='Yearly Statistics',
            placeholder='Select a report type',
            style={'textAlign': 'center', 'width': '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ]),
    
    # Dropdown menu for selecting year (initially hidden)
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year',
            value=None,  # No default value selected
            style={'textAlign': 'center', 'width': '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ], id='year-dropdown-container'),
    
    # Placeholder for the graph
    dcc.Graph(id='line-plot')
])

# Define the callback to update the graph based on dropdown selection
@app.callback(
    [Output('line-plot', 'figure'),
     Output('select-year', 'style')],
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_graph(selected_statistics, selected_year):
    # Update the visibility of the year dropdown based on statistics selection
    year_dropdown_style = {'display': 'none'}
    
    if selected_statistics == 'Yearly Statistics':
        # Filter and process the data for yearly statistics
        df_yearly = data.groupby('Year').agg({'Automobile_Sales': 'sum'}).reset_index()
        fig = px.line(df_yearly, x='Year', y='Automobile_Sales', title='Yearly Sales Statistics')
    
    elif selected_statistics == 'Recession Period Statistics':
        # Update the visibility of the year dropdown
        year_dropdown_style = {'display': 'block'}
        
        # Example recession periods (for demonstration)
        recession_periods = {
            '1980-1982': [1980, 1981, 1982],
            '1990-1991': [1990, 1991],
            '2007-2009': [2007, 2008, 2009]
        }
        if selected_year:
            # Filter data for the selected year
            df_recession = data[data['Year'] == selected_year]
        else:
            # Filter data for all recession periods
            df_recession = data[data['Year'].isin([year for years in recession_periods.values() for year in years])]
        
        df_recession = df_recession.groupby(['Year']).agg({'Automobile_Sales': 'sum'}).reset_index()
        fig = px.bar(df_recession, x='Year', y='Automobile_Sales', title='Sales During Recession Periods')

    return fig, year_dropdown_style

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[5]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Analysis Dashboard"

# Create the dropdown menu options
dropdown_statistics_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024)]

# Create the layout of the app
app.layout = html.Div([
    # Title of the dashboard
    html.H1("Automobile Sales Analysis Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Dropdown menu for selecting statistics
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_statistics_options,
            value='Yearly Statistics',
            placeholder='Select a report type',
            style={'textAlign': 'center', 'width': '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ]),
    
    # Dropdown menu for selecting year (initially hidden)
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year',
            value=None,  # No default value selected
            style={'textAlign': 'center', 'width': '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ], id='year-dropdown-container'),
    
    # Division for output display
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    
    # Placeholder for the graph
    dcc.Graph(id='line-plot')
])

# Define the callback to update the graph and output display based on dropdown selection
@app.callback(
    [Output('line-plot', 'figure'),
     Output('select-year', 'style'),
     Output('output-container', 'children')],
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_graph(selected_statistics, selected_year):
    # Update the visibility of the year dropdown based on statistics selection
    year_dropdown_style = {'display': 'none'}
    output_text = ""
    
    if selected_statistics == 'Yearly Statistics':
        # Filter and process the data for yearly statistics
        df_yearly = data.groupby('Year').agg({'Automobile_Sales': 'sum'}).reset_index()
        fig = px.line(df_yearly, x='Year', y='Automobile_Sales', title='Yearly Sales Statistics')
        output_text = f"Displaying yearly statistics from {df_yearly['Year'].min()} to {df_yearly['Year'].max()}."
    
    elif selected_statistics == 'Recession Period Statistics':
        # Update the visibility of the year dropdown
        year_dropdown_style = {'display': 'block'}
        
        # Example recession periods (for demonstration)
        recession_periods = {
            '1980-1982': [1980, 1981, 1982],
            '1990-1991': [1990, 1991],
            '2007-2009': [2007, 2008, 2009]
        }
        if selected_year:
            # Filter data for the selected year
            df_recession = data[data['Year'] == selected_year]
            output_text = f"Displaying recession data for {selected_year}."
        else:
            # Filter data for all recession periods
            df_recession = data[data['Year'].isin([year for years in recession_periods.values() for year in years])]
            output_text = "Displaying data for all recession periods."
        
        df_recession = df_recession.groupby(['Year']).agg({'Automobile_Sales': 'sum'}).reset_index()
        fig = px.bar(df_recession, x='Year', y='Automobile_Sales', title='Sales During Recession Periods')

    return fig, year_dropdown_style, html.Div(output_text, style={'font-size': '18px', 'padding': '10px'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[6]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Analysis Dashboard"

# Create the dropdown menu options
dropdown_statistics_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024)]

# Create the layout of the app
app.layout = html.Div([
    # Title of the dashboard
    html.H1("Automobile Sales Analysis Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Dropdown menu for selecting statistics
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_statistics_options,
            value='Yearly Statistics',
            placeholder='Select a report type',
            style={'textAlign': 'center', 'width': '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ]),
    
    # Dropdown menu for selecting year
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select a year',
            value=None,  # No default value selected
            style={'textAlign': 'center', 'width': '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ], id='year-dropdown-container'),
    
    # Division for output display
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    
    # Placeholder for the graph
    dcc.Graph(id='line-plot')
])

# Callback to enable or disable the year dropdown based on the selected statistics
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False  # Enable the year dropdown
    else:
        return True  # Disable the year dropdown

# Callback to update the graph and output container based on dropdown selections
@app.callback(
    [Output('line-plot', 'figure'),
     Output('output-container', 'children')],
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistics, selected_year):
    if selected_statistics == 'Yearly Statistics':
        # Filter and process the data for yearly statistics
        df_yearly = data.groupby('Year').agg({'Automobile_Sales': 'sum'}).reset_index()
        fig = px.line(df_yearly, x='Year', y='Automobile_Sales', title='Yearly Sales Statistics')
        output_text = f"Displaying yearly statistics from {df_yearly['Year'].min()} to {df_yearly['Year'].max()}."
    
    elif selected_statistics == 'Recession Period Statistics':
        if selected_year:
            # Filter data for the selected year
            df_recession = data[data['Year'] == selected_year]
            fig = px.bar(df_recession, x='Month', y='Automobile_Sales', title=f'Sales During {selected_year}')
            output_text = f"Displaying data for the year {selected_year}."
        else:
            # Filter data for all recession periods
            recession_data = data[data['Recession'] == 1]
            df_recession = recession_data.groupby('Year').agg({'Automobile_Sales': 'sum'}).reset_index()
            fig = px.bar(df_recession, x='Year', y='Automobile_Sales', title='Sales During Recession Periods')
            output_text = "Displaying data for all recession periods."

    return fig, html.Div(output_text, style={'font-size': '18px', 'padding': '10px'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[7]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Analysis Dashboard"

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Sales Statistics', 'value': 'Yearly Sales Statistics'},
    {'label': 'Recession Period Sales Statistics', 'value': 'Recession Period Sales Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024)]

# Create the layout of the app
app.layout = html.Div([
    # Title of the dashboard
    html.H1("Automobile Sales Analysis Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Dropdown menu for selecting statistics
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Yearly Sales Statistics',
            placeholder='Select a report type',
            style={'textAlign': 'center','width' : '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ]),
    
    # Dropdown for selecting year
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select year',
            value=None
        )
    ]),
    
    # Division for output display
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'})
])

# Callback to enable/disable year dropdown based on selected statistics
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Sales Statistics':
        return False
    else:
        return True

# Callback to update the output container based on selected statistics and year
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'), Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Sales Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        # Plot 1: Average Automobile Sales fluctuation over Recession Period
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation over Recession Period")
        )

        # Plot 2: Average Number of Vehicles Sold by Vehicle Type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Number of Vehicles Sold by Vehicle Type")
        )

        # Plot 3: Pie Chart for Total Expenditure Share by Vehicle Type during Recessions
        total_expenditure = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(total_expenditure,
                values='Advertising_Expenditure', 
                names='Vehicle_Type',
                title='Total Expenditure Share by Vehicle Type during Recessions')
        )

        # Plot 4: Effect of Unemployment Rate on Vehicle Type and Sales
        unemp_data = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data,
                x='Vehicle_Type',
                y='Automobile_Sales',
                color='Vehicle_Type',
                labels={'Vehicle_Type': 'Vehicle Type', 'Automobile_Sales': 'Average Automobile Sales'},
                title='Effect of Unemployment Rate on Vehicle Type and Sales')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'})
        ]
    else:
        # Placeholder for other statistics or a default message
        return html.Div("Please select a report type.")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[8]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Sales Analysis Dashboard"

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Sales Statistics', 'value': 'Yearly Sales Statistics'},
    {'label': 'Recession Period Sales Statistics', 'value': 'Recession Period Sales Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024)]

# Create the layout of the app
app.layout = html.Div([
    # Title of the dashboard
    html.H1("Automobile Sales Analysis Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    # Dropdown menu for selecting statistics
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Yearly Sales Statistics',
            placeholder='Select a report type',
            style={'textAlign': 'center','width' : '80%', 'padding': '3px', 'font-size': '20px'}
        )
    ]),
    
    # Dropdown for selecting year
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder='Select year',
            value=None
        )
    ]),
    
    # Division for output display
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'})
])

# Callback to enable/disable year dropdown based on selected statistics
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Sales Statistics':
        return False
    else:
        return True

# Callback to update the output container based on selected statistics and year
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'), Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Sales Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        # Plot 1: Average Automobile Sales fluctuation over Recession Period
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales Fluctuation over Recession Period")
        )

        # Plot 2: Average Number of Vehicles Sold by Vehicle Type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Number of Vehicles Sold by Vehicle Type")
        )

        # Plot 3: Pie Chart for Total Expenditure Share by Vehicle Type during Recessions
        total_expenditure = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(total_expenditure,
                values='Advertising_Expenditure', 
                names='Vehicle_Type',
                title='Total Expenditure Share by Vehicle Type during Recessions')
        )

        # Plot 4: Effect of Unemployment Rate on Vehicle Type and Sales
        unemp_data = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data,
                x='Vehicle_Type',
                y='Automobile_Sales',
                color='Vehicle_Type',
                labels={'Vehicle_Type': 'Vehicle Type', 'Automobile_Sales': 'Average Automobile Sales'},
                title='Effect of Unemployment Rate on Vehicle Type and Sales')
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'})
        ]
    
    elif (input_year and selected_statistics == 'Yearly Sales Statistics'):
        # Filter data for the selected year
        yearly_data = data[data['Year'] == input_year]
        
        # Plot 1: Yearly Automobile Sales using line chart
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas, 
                x='Year', 
                y='Automobile_Sales', 
                title='Automobile Sales by Year')
        )
        
        # Plot 2: Total Monthly Automobile Sales using line chart
        mas = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas,
                x='Month',
                y='Automobile_Sales',
                title='Total Monthly Automobile Sales')
        )
        
        # Plot 3: Average Number of Vehicles Sold During the Given Year
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title='Average Vehicles Sold by Vehicle Type in the Year {}'.format(input_year))
        )
        
        # Plot 4: Total Advertisement Expenditure for Each Vehicle Using Pie Chart
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
                names='Vehicle_Type',
                values='Advertising_Expenditure',
                title='Total Advertisement Expenditure for Each Vehicle in {}'.format(input_year))
        )

        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)], style={'display': 'flex'})
        ]

    else:
        return html.Div("Please select a report type or year.")

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




