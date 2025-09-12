# **********************************************************************
# Project           : StateOfPostGradLiving
# Program name      : app
# Author            : Susana Paço
# Date created      : 20250821
#
# Summary           : a dash app to show the current financial state of phd
# students in the European Union
#
# Revision History  :
# Date        Author      Num    Summary
# 20250821    Susana      1      first prototype
#
#
# **********************************************************************

import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Load data
phd_stipend_df = pd.read_excel("Data/AveragePhDStipend_EuropeanUnion.xlsx")
minimum_wage_df = pd.read_excel("Data/MinimumWage_EuropeanUnion.xlsx")

# Prepare dataframes
phd_stipend_df = phd_stipend_df[["Country", "MinimumPhDStipend_Net"]].rename(columns={"MinimumPhDStipend_Net": "Net_PhD_Stipend"})
minimum_wage_df = minimum_wage_df[["Country", "Net Minimum Wage (€/month)"]].rename(columns={"Net Minimum Wage (€/month)": "Net_Minimum_Wage"})

# Merge on Country
merged_df = pd.merge(phd_stipend_df, minimum_wage_df, on="Country", how="inner")

# Sort countries alphabetically for consistent x-axis
merged_df = merged_df.sort_values("Country")

# Create app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Net PhD Stipends vs Minimum Wages in EU Countries", style={"textAlign": "center"}),
    dcc.Graph(
        id='wage-comparison-chart',
        figure={
            'data': [
                go.Bar(
                    x=merged_df['Country'],
                    y=merged_df['Net_PhD_Stipend'],
                    name='PhD Stipend (Net)',
                    marker_color='steelblue'
                ),
                go.Bar(
                    x=merged_df['Country'],
                    y=merged_df['Net_Minimum_Wage'],
                    name='Minimum Wage (Net)',
                    marker_color='seagreen'
                )
            ],
            'layout': go.Layout(
                barmode='group',
                xaxis={'title': 'Country', 'tickangle': -45},
                yaxis={'title': 'Net Monthly Wage (€)'},
                margin={'b': 150},
                legend={'x': 0, 'y': 1},
                height=600,
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)
