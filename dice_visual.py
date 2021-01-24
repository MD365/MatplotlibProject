from die import Die
import pygal
import matplotlib.pyplot as plt
#创建两个d6
die1 = Die()
die2 = Die(10)
#掷骰子，并将结果储存在列表中
results = []
for roll_num in range(1000):
    result = die1.rool() + die2.rool()
    results.append(result)

#分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequenty = results.count(value)  #"""返回value的出现次数。”“”
    frequencies.append(frequenty)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "results of rolling one D6 1000 times."
hist.x_labels =["2","3","4","5","6",'7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "frequency of result"

hist.add("D6+D6", frequencies)
hist.render_to_file('dice_visual.svg')
plt.scatter(frequencies,hist.x_labels)
plt.show()