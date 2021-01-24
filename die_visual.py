from die import Die
import pygal
#创建一个d6
die = Die()

#掷骰子，并将结果储存在列表中
results = []
for roll_num in range(1000):
    result = die.rool()
    results.append(result)

#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequenty = results.count(value)  #"""返回value的出现次数。”“”
    frequencies.append(frequenty)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "results of rolling one D6 1000 times."
hist.x_labels =["1","2","3","4","5","6"]
hist.x_title = "Result"
hist.y_title = "frequency of result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')