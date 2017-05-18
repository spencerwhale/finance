from math import pi

import pandas as pd

from bokeh.plotting import figure, show, output_file
# from bokeh.sampledata.stocks import MSFT

df = pd.read_csv('HistoricalPrices.csv',skipinitialspace=True)
df["Date"] = pd.to_datetime(df["Date"])

inc = df.Close > df.Open
dec = df.Open > df.Close
w = 12*60*60*1000 # half day in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

p.segment(df.Date, df.High, df.Date, df.Low, color="black")
p.vbar(df.Date[inc], w, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(df.Date[dec], w, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="black")

output_file("candlestick.html", title="candlestick bokeh")

show(p)  # open a browser
