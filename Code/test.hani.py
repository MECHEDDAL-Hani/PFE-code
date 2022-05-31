""" docstring """
from matplotlib import pyplot as plt
from progress_query_data import SQLite
# import pandas as pd


plt.style.use("fivethirtyeight")

# time_x = []
q = SQLite()

time_y = [
    # q.select_avg_result("Query 1", "case 1"),
    q.select_avg_result("Query 6", "case 2"),
    q.select_avg_result("Query 6", "case 3"),
    q.select_avg_result("Query 6", "case 4")]
case_x = [
    # "sample data base",
    "with index",
    "Replication",
    "Sharding"]

print(time_y)
plt.barh(case_x, time_y, color="#444444", label="All Case")

# # py_dev_y = [45372, 48876, 53850, 57287, 63016,
# #             65998, 70003, 70000, 71496, 75370, 83640]
# # plt.barh(ages_x, py_dev_y, color="#008fd5", label="Python")

# # js_dev_y = [37810, 43515, 46823, 49293, 53437,
# #             56373, 62375, 66674, 68745, 68746, 74583]
# # plt.barh(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")

plt.legend()

# plt.title("Median Salary (USD) by Age")
plt.xlabel("Time (ms)")
plt.ylabel("Case")

plt.tight_layout()

plt.show()
