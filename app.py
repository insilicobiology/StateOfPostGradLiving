# **********************************************************************
# Project           : StateOfPostGradLiving
# Program name      : app
# Author            : Susana Paço
# Date created      : 20250821
#
# Summary           : a dash app to show the current financial state of phd
# students in the european union
#
# Revision History  :
# Date        Author      Num    Summary
# 20250821    Susana      1      first prototype
#
#
# **********************************************************************


# Import Dash and required components
from dash import Dash, html

# Create a Dash application instance
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hello Dash!"),
    html.P("This is a basic Dash app.")
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
