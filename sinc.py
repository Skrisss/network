import math
from random import random
import matplotlib.pyplot as plt


def message_time_gen(mlambda):
    u = random()
    t = - (math.log(u) / mlambda)
    return t


messages = int(input('Введите количество сообщений'))
mlambda = 0.01
win_time = 1
lambds = []
mn = []
md_l = []
md_theory = []
mn_theory = []
while mlambda < 1:
    queue = []
    d = 0
    time = 0
    message_counter = []
    n_theory = (mlambda * (2 - mlambda)) / (2 * (1 - mlambda))
    d_theory = (n_theory / mlambda) + 0.5
    for i in range(messages):  #

        time += message_time_gen(mlambda)
        if len(queue) == 0:
            di = win_time - (time % win_time) + win_time  #
        else:
            while len(queue) > 0 and time > queue[0]:
                queue.pop(0)
            if len(queue) != 0:
                di = queue[len(queue) - 1] + win_time * 2 - time  #
            else:
                di = win_time - (time % win_time) + win_time  #
        queue.append(int(time + di - win_time))  # момент прихода заявки

        winnumber = int(queue[len(queue) - 1] // win_time)
        if len(message_counter) < winnumber+1:
            for j in range((winnumber - len(message_counter))+1):
                message_counter.append(0)
        for w in range(int(time - time % win_time), queue[len(queue) - 1] + 1):
            message_counter[w] += 1

        d += di
    md_l.append(d / messages)
    mn.append(sum(message_counter) / len(message_counter))
    md_theory.append(d_theory)
    mn_theory.append(n_theory)
    lambds.append(mlambda)
    mlambda += 0.01

plt.subplot(1, 2, 1)
plt.plot(lambds, md_l, label="M[D] практическое")
plt.plot(lambds, md_theory, label="M[D] теоретическое")
plt.title('M[D]', fontstyle="italic")
plt.ylabel('M[D]', fontstyle="italic")
plt.xlabel('lambda', fontstyle="italic")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(lambds, mn, label="M[N] практическое")
plt.plot(lambds, mn_theory, label="M[N] теоретическое")
plt.title('M[N]', fontstyle="italic")
plt.ylabel('M[N]', fontstyle="italic")
plt.xlabel('lambda', fontstyle="italic")
plt.legend()
plt.show()
