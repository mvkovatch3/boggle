import numpy as np
from time import sleep

from functions import get_board

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Toggle, Div, Slider, Text, Button

# replace with JSON self defined MultiPolygon later
from bokeh.models.glyphs import Rect

from bokeh.plotting import figure

# Init doc for async time
global duration
duration = 0
doc = curdoc()

# Set up grid
grid = figure(
    plot_height=600,
    plot_width=600,
    x_range=[0, 5],
    y_range=[0, 5],
    tools="",
    toolbar_location=None,
    outline_line_alpha=0,
)
grid.xaxis.visible = False
grid.yaxis.visible = False
grid.xgrid.grid_line_color = None
grid.ygrid.grid_line_color = None

# Add blank dice
x_dice = np.arange(0, 5) + 0.5
x_dice, y_dice = np.meshgrid(x_dice, x_dice)
dice_src = ColumnDataSource(dict(x=x_dice, y=y_dice))
dice = Rect(x="x", y="y", width=0.95, height=0.95, fill_color="#cab2d6")
grid.add_glyph(dice_src, dice)

# Add letters
# TODO: random orientation U/D/L/R
x_letters = x_dice.reshape(25, 1)
y_letters = (y_dice - 0.3).reshape(25, 1)
text = np.ones(len(x_letters)).astype(str)
text[:] = "X"
letter_src = ColumnDataSource(dict(x=x_letters, y=y_letters, text=text))
letters = Text(x="x", y="y", text="text", text_font_size="64px", text_align="center",)
grid.add_glyph(letter_src, letters)

# Set up widgets
time_slider = Slider(start=1, end=10, value=3, step=1, title="Duration (minutes)")
special_toggle = Toggle(
    label="""Include bonus die? \n
[He, An, In, Er, Th, Qu]""",
    button_type="warning",
)
shuffle_button = Button(label="Shake!", button_type="primary")
start_button = Button(label="Start timer", button_type="success")
stop_button = Button(label="Stop timer", button_type="danger")
timer = Div(
    text=f"""Timer: <br> 0:00""",
    style={"font-size": "400%", "color": "black", "text-align": "center"},
)

# Set up callback functions
def shuffle():
    letter_src.data["text"] = get_board(special=special_toggle.active)


def start_game():
    global duration
    duration = 60.0 * time_slider.value


def run_timer():
    global duration
    duration -= 0.25
    if duration < 0:
        duration = 0
    minutes = int(duration // 60)
    seconds = int(duration - minutes * 60)
    timer.text = f"""Timer: <br> {minutes}:{seconds:02d}"""
    if duration > 30:
        timer.style["color"] = "black"
    if (duration < 30) & (duration != 0):
        if timer.style["color"] == "red":
            timer.style["color"] = "black"
        else:
            timer.style["color"] = "red"


def stop_timer():
    global duration
    duration = 0
    timer.style["color"] = "black"


# Set up callbacks
shuffle_button.on_click(shuffle)
start_button.on_click(start_game)
stop_button.on_click(stop_timer)

# Set up layouts and add to document
inputs = column(
    special_toggle, shuffle_button, time_slider, start_button, stop_button, timer
)

curdoc().add_root(row(inputs, grid, width=800))
curdoc().title = "Boggle"

doc.add_periodic_callback(run_timer, 250)
