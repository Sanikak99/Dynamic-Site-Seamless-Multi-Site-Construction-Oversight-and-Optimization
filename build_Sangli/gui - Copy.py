from subprocess import run
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import squarify
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanika\Documents\Project II\build_Sangli\assets\frame0")


def open_gui5():
    run(["python", str(Path(r"C:\Users\Sanika\Documents\Project II\build_W_SA\gui.py"))])

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1644x795")
window.configure(bg = "#FFFFFF")

# Load data from Excel sheet
excel_file_path = (r"C:\Users\Sanika\Documents\Project II\Rocktech infrastructre.xlsx")  # Replace with your actual file path
revenue_data = pd.read_excel(excel_file_path)
revenue_data = revenue_data.dropna(subset=['Vehicals (No.)'])
revenue_data['Vehicals (No.)'] = revenue_data['Vehicals (No.)'].astype(str)

revenue_data = revenue_data.dropna(subset=['Trips'])
total_trips_data = revenue_data.groupby('Vehicals (No.)')['Trips'].sum().reset_index()
total_maintanance = revenue_data['Maintaince (Rs)'].sum()


total_fuel_consumption_data = revenue_data.groupby('Vehicals (No.)')['Fuel'].sum().reset_index()
total_fuel_consumption_data = total_fuel_consumption_data.sort_values(by='Fuel', ascending=False)



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1644,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    717.0,
    241.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1361.0,
    241.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1361.0,
    624.0,
    image=image_image_3
)

canvas.create_text(
    132.0,
    420.0,
    anchor="nw",
    text="Total Advance\nPayment",
    fill="#F27026",
    font=("K2D Bold", 24 * -1)
)

canvas.create_text(
    171.0,
    581.0,
    anchor="nw",
    text="Budget",
    fill="#F8AD16",
    font=("K2D Bold", 24 * -1)
)

canvas.create_text(
    136.0,
    80.0,
    anchor="nw",
    text="Total Material\nCost",
    fill="#2690F2",
    font=("K2D Bold", 24 * -1)
)

canvas.create_text(
    136.0,
    249.0,
    anchor="nw",
    text="Total Electric\nCost",
    fill="#00D053",
    font=("K2D Bold", 24 * -1)
)

canvas.create_text(
    163.0,
    24.0,
    anchor="nw",
    text="120000",
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

canvas.create_text(
    159.0,
    182.0,
    anchor="nw",
    text="120000",
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

canvas.create_text(
    163.0,
    360.0,
    anchor="nw",
    text="120000",
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

canvas.create_text(
    159.0,
    528.0,
    anchor="nw",
    text="120000",
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    75.0,
    417.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    719.0,
    625.0,
    image=image_image_5
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui5,
    relief="flat"
)
button_1.place(
    x=6.0,
    y=638.0,
    width=344.7057189941406,
    height=136.749267578125
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    65.0,
    82.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    75.0,
    572.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    75.0,
    245.0,
    image=image_image_8
)


# Create a Matplotlib figure and axis  bar
fig_1, ax_1 = plt.subplots(figsize=(7, 2.9), facecolor="#D9D9D9")
ax_1.set_facecolor("#D9D9D9")
ax_1.tick_params(labelsize=7, colors="Black")
fig_1.autofmt_xdate()

# Plotting the bar graph
ax_1.bar(revenue_data['Vehicals (No.)'], revenue_data['Maintaince (Rs)'], color="Orange", label='Maintenance Cost')
ax_1.grid(visible=True)

# Adding legend and labels
ax_1.set_title("Maintenance cost of Vehicle")
ax_1.set_xlabel('Vehicle Number Plates')
ax_1.set_ylabel('Maintenance Cost (Rs)')

canvas = FigureCanvasTkAgg(figure=fig_1, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=356, y=480)



fig_2, ax_2 = plt.subplots(figsize=(5, 2.9), facecolor="#D9D9D9")
ax_2.set_facecolor("#D9D9D9")
ax_2.tick_params(labelsize=7, colors="Black")
fig_2.autofmt_xdate()

# Plotting the Line graph
ax_2.plot(total_trips_data['Vehicals (No.)'], total_trips_data['Trips'], color="red", label='Maintenance Cost')
ax_2.scatter(total_trips_data['Vehicals (No.)'], total_trips_data['Trips'], color="red", label='Maintenance Cost')
ax_2.grid(visible=True)

# Adding legend and labels
ax_2.set_title("Total Trips of individual Vehicle")
ax_2.set_xlabel('Vehicle Number Plates')
ax_2.set_ylabel('Trips')

canvas = FigureCanvasTkAgg(figure=fig_2, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=1110, y=480)

print(total_trips_data)


print(total_trips_data['Trips'].sum())


fig_4, ax_4 = plt.subplots(figsize=(5, 4), facecolor="#D9D9D9")
ax_4.set_facecolor("#D9D9D9")

# Define an orange color palette
orange_palette = ['#FFA07A', '#FF8C00', '#FF6347', '#FF4500', '#FFD700']

# Plotting the treemap with orange color palette
squarify.plot(sizes=total_fuel_consumption_data['Fuel'],
              label=total_fuel_consumption_data['Vehicals (No.)'],
              color=orange_palette)

# Adding labels
plt.title("Fuel Consumption Treemap")
plt.axis('off')

# Display the Matplotlib plot in Tkinter window
canvas = FigureCanvasTkAgg(figure=fig_4, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=1098, y=52)


window.resizable(True, True)
window.mainloop()
