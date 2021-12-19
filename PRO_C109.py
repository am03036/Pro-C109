import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("exam.csv")
score_list = df["reading score"].to_list()

mean = sum(score_list)/len(score_list)
std_deviation = statistics.stdev(score_list)
median = statistics.median(score_list)
mode = statistics.mode(score_list)

print(mean)
print(median)
print(mode)
print(std_deviation)

std1_start, std1_end = mean-std_deviation, mean+std_deviation
std2_start, std2_end = mean-(2*std_deviation), mean+(2*std_deviation)
std3_start, std3_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_within_1_std = [result for result in score_list if result>std1_start and result<std1_end]
list_within_2_std = [result for result in score_list if result>std2_start and result<std2_end]
list_within_3_std = [result for result in score_list if result>std3_start and result<std3_end]

print("% of data within 1st std dev ", len(list_within_1_std)/len(score_list)*100,"%", sep = '')
print("% of data within 2nd std dev ", len(list_within_2_std)/len(score_list)*100,"%", sep = '')
print("% of data within 3rd std dev ", len(list_within_3_std)/len(score_list)*100,"%", sep = '')

fig = ff.create_distplot([score_list],["Result"])
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [std1_start,std1_start], y = [0,0.17], mode = "lines", name = "STANDAR DEV 1 START"))
fig.add_trace(go.Scatter(x = [std1_end,std1_end], y = [0,0.17], mode = "lines", name = "STANDAR DEV 1 END"))
fig.add_trace(go.Scatter(x = [std2_start,std2_start], y = [0,0.17], mode = "lines", name = "STANDAR DEV 2 START"))
fig.add_trace(go.Scatter(x = [std2_end,std2_end], y = [0,0.17], mode = "lines", name = "STANDAR DEV 2 END"))
fig.add_trace(go.Scatter(x = [std3_start,std3_start], y = [0,0.17], mode = "lines", name = "STANDAR DEV 3 START"))
fig.add_trace(go.Scatter(x = [std3_end,std3_end], y = [0,0.17], mode = "lines", name = "STANDAR DEV 3 END"))
fig.show()


