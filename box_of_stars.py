# python function to draw a box of stars

def box_of_stars(w, h):
    tb = '*'*w
    side = '*' + ' '*(w-2) + '*'

    print(tb)
    for i in range(h-2):
        print(side)
    print(tb)
