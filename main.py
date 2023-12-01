from math import sqrt
import PySimpleGUI as sg
from app import linear_least_squares as lls
from app import draw_figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_canvas(x, y):
    global fig_canvas_agg
    if fig_canvas_agg:
        fig_canvas_agg.get_tk_widget().forget()
    fig = draw_figure(x, y)
    fig_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
    fig_canvas_agg.draw()
    fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


t_units = ['°C', '°F', '°K']
m_units = ['M·10⁵', 'ɸ']

t_selector = [sg.Combo(t_units, key='-T-UNIT-', default_value='°C', enable_events=True, size=(5))]
m_selector = [sg.Combo(m_units, key='-M-UNIT-', default_value='M·10⁵', enable_events=True, size=(5))]

input_grid = [
    [sg.Input(key=f"-IN{i}-{j}-", size=(7), default_text=f'{i+1}.0', enable_events=True) for j in range(2)]
    for i in range(5)
]

layout = layout = [
    [
        sg.Column([[sg.Text("Enter the points:")]] + [m_selector + t_selector] + input_grid + [[sg.Button("OK")]]),
        sg.Column([[sg.Canvas(key="-CANVAS-")]]),
    ],
    [
        sg.Text("1/b = "), sg.Text(key="-RESULT-")
    ]
]

window = sg.Window("Trabalho CN", layout, margins=(10, 10), finalize=True, font=('Helvetica', 14))

fig_canvas_agg = None
draw_canvas([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event.startswith("-IN"):
        pass
    if event == "OK":
        # Grab the values from the input fields
        x = [float(values[f'-IN{i}-{0}-']) for i in range(5)] 
        y = [float(values[f'-IN{i}-{1}-']) for i in range(5)]
        
        if 0.0 in x or 0.0 in y:
            sg.popup("Invalid input, values must be non-zero", title="Error")
            continue
        
        if values['-M-UNIT-'] == 'ɸ':
            pass
        elif values['-M-UNIT-'] == 'M·10⁵':
            x = list(map(lambda x: 1/sqrt(x*(10**5)), x))
        
        if values['-T-UNIT-'] == '°C':
            y = list(map(lambda x: x + 273, y))
        elif values['-T-UNIT-'] == '°F':
            y = list(map(lambda x: (x - 32) * 5/9 + 273, y))
        
        y = list(map(lambda x: 1/x, y))
        
        draw_canvas(x, y)
        
        #find the 1/b as b is the slope of the line
        _, b, _ = lls(x, y)
        window['-RESULT-'].update(f'{1/b:.4f}')


window.close()
