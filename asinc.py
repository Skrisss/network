import math
from random import random
import matplotlib.pyplot as plt


def message_time_gen(mlambda):
    u = random()
    t = - (math.log(u) / mlambda)
    return t


messages = int(input('Введите количество сообщений'))
mlambda = 0.01
proc_time = 1
lambds = []
md_l = []
md_theory = []
while mlambda < 1:
    queue = []
    d = 0
    time = 0
    n_theory = (mlambda * (2 - mlambda)) / (2 * (1 - mlambda))
    d_theory = (n_theory / mlambda)
    for i in range(messages):
        time += message_time_gen(mlambda)
        if len(queue) == 0:
            di = proc_time
        else:
            while time > queue[0]+proc_time and len(queue) > 0:
                queue.pop(0)
            if len(queue) != 0:

                di = queue[len(queue) - 1] + proc_time * 2 - time  #
            else:
                di = proc_time
        queue.append(time+di-proc_time)
        d += di
    lambds.append(mlambda)
    md_l.append(d / messages)
    md_theory.append(d_theory)
    mlambda += 0.01
plt.plot(lambds, md_l, label="M[D] практическое")
plt.plot(lambds, md_theory, label="M[D] теоретическое")
plt.title('M[D]', fontstyle="italic")
plt.ylabel('M[D]', fontstyle="italic")
plt.xlabel('lambda', fontstyle="italic")
plt.legend()
plt.show()
