import pandas as pd

cities_df = pd.read_csv('Resources/cities.csv', index_col=0)

cities_html = cities_df.to_html()