# Task 3: Interactive Visualizations with Plotly

import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print(df.head(10))
print(df.tail(10))

# Clean the data
clean_df = df.copy()
clean_df['strength'] = clean_df['strength'].str.replace(r'-.*|\+', '', regex = True).astype(float)

# Create an interactive scatter plot
fig = px.scatter(clean_df, x='strength', y='frequency', color='direction', title='Strength vs. Frequency', hover_data=['frequency'])

# Save and open HTML
fig.write_html("wind.html", auto_open=True)




