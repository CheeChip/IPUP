#++++++++++++++++++++++++++++++++++++++++++++++++
# 题目
#   （物理方面：加速度）平均加速度的定义是速度变化量除以
#   变化所占用的时间
#       a = (v_1 - v_0) / t
#   编写一个程序，提示用户输入以 m/s 为单位的初始速度 v_1
#   和末速度 v_2，以秒为单位的时间 t，然后显示平均加速度。
#++++++++++++++++++++++++++++++++++++++++++++++++

v0, v1, t = eval(input("Enter v0, v1, and t: "))

a = (v1 - v0) / t

print("The average acceleration is %f" % a)