import tkinter as tk
from tkinter import scrolledtext, messagebox
from itertools import permutations
from draw import draw_rectangles

def calculate_waste(placement):
    total_area = 20 * 20
    used_area = 0
    for piece in placement:
        used_area += piece[0] * piece[1]
    return total_area - used_area

def find_optimal_placement(pieces):
    plate_size = (20, 20)
    
    sorted_rectangles = sorted(pieces, key=lambda x: x[0] * x[1], reverse=True)

    placed_rectangles = {}

    for rect_id, rect_size in enumerate(sorted_rectangles):
        width, height = rect_size

        best_fit = None
        best_fit_score = float('inf')

        for x in range(plate_size[0] - width + 1):
            for y in range(plate_size[1] - height + 1):
                overlap = False
                for placed_rect in placed_rectangles.values():
                    if (
                        x < placed_rect['x'] + placed_rect['width'] and
                        x + width > placed_rect['x'] and
                        y < placed_rect['y'] + placed_rect['height'] and
                        y + height > placed_rect['y']
                    ):
                        overlap = True
                        break

                if not overlap:
                    score = max(plate_size[0] - (x + width), plate_size[1] - (y + height))

                    if score < best_fit_score:
                        best_fit_score = score
                        best_fit = {'x': x, 'y': y}

        if best_fit is not None:
            placed_rectangles[rect_id] = {'x': best_fit['x'], 'y': best_fit['y'], 'width': width, 'height': height}


    result = []
    print(placed_rectangles)
    print("Optimal Placement:")
    for item in placed_rectangles:
        piece = placed_rectangles[item]
        result.append((piece["width"], piece["height"], piece["x"], piece["y"]))
   
    return result, calculate_waste(result)


class AIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("balkupu")

        self.create_input_widgets()

        self.create_buttons()


        self.create_output_widgets()

        self.input_list = []

    def create_input_widgets(self):
        # İlk Giriş etiketi ve alanını oluştur
        self.input_label_1 = tk.Label(self.root, text="Width:")
        self.input_label_1.pack(pady=5)

        self.input_entry_1 = tk.Entry(self.root)
        self.input_entry_1.pack(pady=5)

        # İkinci Giriş etiketi ve alanını oluştur
        self.input_label_2 = tk.Label(self.root, text="Height:")
        self.input_label_2.pack(pady=5)

        self.input_entry_2 = tk.Entry(self.root)
        self.input_entry_2.pack(pady=10)

    def create_buttons(self):
        self.process_button = tk.Button(self.root, text="Add", command=self.process_input)
        self.process_button.pack(pady=5)

        self.continue_button = tk.Button(self.root, text="Run", command=self.show_results)
        self.continue_button.pack(pady=5)

    def create_output_widgets(self):
        self.output_label = tk.Label(self.root, text="Inputs:")
        self.output_label.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(pady=10)

    def process_input(self):
        input_data_1 = self.input_entry_1.get().strip()
        input_data_2 = self.input_entry_2.get().strip()

        if input_data_1.isdigit() and input_data_2.isdigit():
            input_data_1 = int(input_data_1)
            input_data_2 = int(input_data_2)

            self.input_list.append((input_data_1, input_data_2))
            self.output_text.insert(tk.END, f"Added input: {input_data_1}, {input_data_2}\n")
        else:
            messagebox.showerror("Error", "Please enter a number.")

        self.input_entry_1.delete(0, tk.END)
        self.input_entry_2.delete(0, tk.END)

    def show_results(self):
        result, waste_area = find_optimal_placement(self.input_list)
        self.output_text.insert(tk.END, f"Unused space: {waste_area}\n") 
        self.output_text.insert(tk.END, f"Result: {result}\n")
        draw_rectangles(result)
            


if __name__ == "__main__":
    root = tk.Tk()
    app = AIApp(root)
    root.mainloop()