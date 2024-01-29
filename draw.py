import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

def draw_rectangles(rectangles):
    fig, ax = plt.subplots(figsize=(5, 5))

    for rect_params in rectangles:
        length, width, x, y = rect_params
        rectangle = patches.Rectangle((x, y), length, width, edgecolor='r', facecolor=(random.random(), random.random(), random.random()))
        ax.add_patch(rectangle)

    ax.set(xlim=(0, 20), xticks=np.arange(0, 21),
       ylim=(0, 20), yticks=np.arange(0, 21))
    ax.set_aspect('equal', 'box')  

    plt.show()