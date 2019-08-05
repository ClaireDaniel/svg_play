import numpy as np
import sys
import math

def draw_rect(x, y, width, height, angle, opacity = 0.5, color='black'):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" stroke-width="0.5" stroke="{color}" opacity="{opacity}" transform="rotate{angle, x, y}"/>'

def spiral(width, height, r_width, r_height, r_angle, spiral_rotation, interval, b = 0.2):

# Defines inner SVG code for rectagles drawn at points around a logarithmic spiral

    rotation = spiral_rotation
    interval = interval

    x_list = np.array([])
    y_list = np.array([])

    a = 0.2

    angles = np.array([i*i for i in np.arange(rotation, 1, -interval)])
    angles = np.interp(angles, (angles.min(), angles.max()), (rotation,0))

    for i in angles:

        t = math.radians(i)
        x_list = np.append(x_list, a*math.exp(b*t)*math.cos(t))
        y_list = np.append(y_list, a*math.exp(b*t)* math.sin(t))

    #Scale to screen canvas size
    adj_edge = max(r_width, r_height)
    x_list = np.interp(x_list, (x_list.min(), x_list.max()), (0 + adj_edge, width - adj_edge)).astype(int)
    y_list = np.interp(y_list, (y_list.min(), y_list.max()), (0 + adj_edge, height - adj_edge)).astype(int)

    colors = ["#eed284", "#96384e", "#04354b", "#037665"]


    for i in range(0, len(x_list)):
        a = i * r_angle
        print(a)
        print(draw_rect(x_list[i], y_list[i], r_width, r_height, a, color=colors[i%len(colors)]))

def multiple_spirals_output(no_spirals, width, height, r_width, r_height, r_angle, spiral_rotation, interval, b=0.1):

#Produces full SVG text and allows for multiple spirals to be drawn

    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    print(header)

    for i in range(0, no_spirals):
        spiral(width, height, r_width, r_height, r_angle, spiral_rotation, max(interval - i,1), b = 0.1 + i*0.1)

    footer = f'</svg>'
    print(footer)

if __name__ == "__main__":

    multiple_spirals_output(2, 500, 500, 5, 40, 45, 600, 3)
