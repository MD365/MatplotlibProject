import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建个randowwalk实例，并将点都绘制出来
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s= 15)
    plt.show()

    keep_running = input("make another walk(y/n):")
    if keep_running == 'n':
        break