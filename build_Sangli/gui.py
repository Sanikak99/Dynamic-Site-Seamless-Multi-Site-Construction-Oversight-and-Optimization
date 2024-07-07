from subprocess import run
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import squarify

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
excel_file_path = (r"C:\Users\Sanika\Documents\Project II\DataSangli 2.xlsx")  # Replace with your actual file path
data = pd.read_excel(excel_file_path)

data['Cement(Bags)'] *= 20

data['Date'] = pd.to_datetime(data['Date'])

# Set 'Date' column as index
data.set_index('Date', inplace=True)

# Resample data on a monthly basis
monthly_data = data.resample('MS').sum()
material_columns = ['Cement(Bags)', 'Bricks', 'Steel', 'Sand']
electricity = ['Power Consumption (kW)','']

monthly_data.sort_values(by='Date', ascending=False, inplace=True)

# Take the most recent 7 months of data
recent_data = monthly_data.head(7)


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
    text=data["Total Material Cost"].sum(),
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

canvas.create_text(
    159.0,
    182.0,
    anchor="nw",
    text=round((data["Power Consumption (kW)"]*data["Duration (hours)"]*data["Total Electric Cost"]).sum()),
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

canvas.create_text(
    163.0,
    360.0,
    anchor="nw",
    text=round(data["Advance Payment"][0]),
    fill="#000000",
    font=("K2D Bold", 32 * -1)
)

canvas.create_text(
    159.0,
    528.0,
    anchor="nw",
    text=round(data["Budget"][0]),
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


cyan_shades = ['#005c65', '#007783', '#0099a7', '#00e1f6', '#9af5fd']

fig, ax = plt.subplots(figsize=(7.1, 4), facecolor="#D9D9D9")

# Plotting material-related data side by side
bar_width = 0.2
positions = np.arange(len(monthly_data.index))
for i, (material, color) in enumerate(zip(material_columns, cyan_shades)):
    ax.bar(positions + i * bar_width, monthly_data[material][::-1], width=bar_width, label=material, color=color)

ax.set_title('Material Consumption Over Time')
ax.set_facecolor("#D9D9D9")
ax.set_xlabel('Months')
ax.set_ylabel('Quantity')
ax.set_xticks(positions + bar_width)
ax.set_xticklabels(monthly_data.index.strftime('%b %Y')[::-1], rotation=45)
ax.grid(True)
ax.legend(framealpha=0, loc='upper left', bbox_to_anchor=(0, 1))
fig.tight_layout()

# Embedding the Matplotlib plot into Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=360, y=50)


# Reset the index to turn the 'Date' index into a regular column
data.reset_index(inplace=True)

# Move the 'Date' column to the desired position (e.g., position 0)
data.insert(0, 'Date', data.pop('Date'))

equipment_usage = data['Equipment Used'].value_counts()
months = data['Date'].dt.month_name()

def create_pie_chart(data, labels, title="Equipment Usage"):
    palette = ['#005c65', '#007783', '#0099a7', '#00e1f6', '#9af5fd']
    plt.figure(figsize=(4, 4),facecolor="#D9D9D9")
    plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=140, colors=palette)
    plt.title(title)
    plt.axis("equal")
    plt.tight_layout()

    # Embed the plot into Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(x=1160, y=50)

# Call the function with equipment usage data and month labels
create_pie_chart(equipment_usage, labels=equipment_usage.index, title="Equipment Usage (Monthly)")


monthly_sum = data.groupby(data['Date'].dt.month_name())[['Power Consumption (kW)', 'Total Electric Cost']].sum()

# Extract power consumption and total electric cost from monthly_sum DataFrame
power = monthly_sum['Power Consumption (kW)']
cost = monthly_sum['Total Electric Cost']
months = monthly_sum.index.tolist()

# Reorder months to start from May
months = months[months.index('May'):] + months[:months.index('May')]
months = [m[:3] for m in months]
# Create the plot
fig, ax1 = plt.subplots(figsize=(7.1, 2.7),facecolor="#D9D9D9")

# Plotting Power Consumption (kW) on the primary y-axis
ax1.plot(months, power, marker='o', label='Power Consumption (kW)', color='#004448',markersize=11)
ax1.set_xlabel('Months')
ax1.set_facecolor("#D9D9D9")
ax1.set_ylabel('Power Consumption (kW)', color='#004448')
ax1.tick_params(axis='y', labelcolor='#004448')

# Create a secondary y-axis for Total Electric Cost
ax2 = ax1.twinx()
ax2.plot(months, cost, marker='o', label='Total Electric Cost', color='#03e5f1')
ax2.set_ylabel('Total Electric Cost (Rs)', color='#004448')
ax2.tick_params(axis='y', labelcolor='#004448')

# Adding labels and title
plt.title('Monthly Power Consumption & Total Electric Cost')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show grid for better visualization
ax1.grid(True)

# Show legend
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 0.2),framealpha=0)

plt.tight_layout()

# Embedding the Matplotlib plot into Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=364, y=500)


monthly_material_cost = data.groupby(data['Date'].dt.month_name())['Total Material Cost'].sum()

# Define the figure and axis
fig_material_cost, ax_material_cost = plt.subplots(figsize=(5.1, 2.6), facecolor="#D9D9D9")
ax_material_cost.set_facecolor("#D9D9D9")

# Define an orange color palette
purple_palette = ['#005c65', '#007783', '#0099a7', '#00e1f6', '#9af5fd']

# Plotting the treemap with orange color palette
squarify.plot(sizes=monthly_material_cost.values, label=monthly_material_cost.index,
              color=purple_palette, alpha=0.7, ax=ax_material_cost)

# Adding labels and title
plt.title("Total Material Cost Treemap")
plt.axis('off')



# Display the Matplotlib plot in Tkinter window
canvas_material_cost = FigureCanvasTkAgg(figure=fig_material_cost, master=window)
canvas_material_cost.draw()
canvas_material_cost.get_tk_widget().place(x=1100, y=504)


window.resizable(False, False)
window.mainloop()


