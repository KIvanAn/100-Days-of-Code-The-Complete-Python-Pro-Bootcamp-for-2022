import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0)
window.rowconfigure(1)
window.rowconfigure(2)

# Labels
label_miles = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
label_km = tkinter.Label(text="Km", font=("Arial", 14, "bold"))
label_to_result = tkinter.Label(text="Is equal to", font=("Arial", 14, "bold"))
label_result = tkinter.Label(text="0", font=("Arial", 14, "bold"))

# Entry
input_miles = tkinter.Entry()


# Button
def convert_miles_to_km():
    label_result["text"] = round(float(input_miles.get()) * 1.609)


calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)

# Gird elements
label_to_result.grid(column=0, row=1)
input_miles.grid(column=1, row=0)
label_miles.grid(column=2, row=0)
label_km.grid(column=2, row=1)
label_result.grid(column=1, row=1)
calculate_button.grid(column=1, row=2)

window.mainloop()
