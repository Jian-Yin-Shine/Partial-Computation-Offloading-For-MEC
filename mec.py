import numpy as np
import argparse


class Env():
    def __init__(self, W, F, K, Dn, Cn, f, dist, pn, pi):
        # W 带宽 10 MHz
        # F 边缘服务器总计算能力
        # K 用户数量
        # Dn, Cn 任务量大小，所需cpu周期数, (300~500kb), (900, 1100)兆周期数 1Mhz = 1000khz = 1000*1000hz
        # f 用户本地计算能力 1GHz/s | [0.5, 1.5]GHz/s (1000*1000*1000)
        # dist 用户距离
        # pn, pi 上传功率，闲时功率 | mW (毫瓦)
        # state 系统状态

        self.W, self.F, self.K = W, F, K
        self.pn, self.pi = pn, pi
        self.Dn, self.Cn, self.f, self.dist = Dn, Cn, f, dist

        self.state = 0
        self.reward = 0
        # self.pre_state = 5


    def step(self, action):

        # 把action 特殊处理了一下，防止出现算法bug，小于0的置为0，大于1的置为1，无限大的置为1
        action[action < 0] = 0
        action[action > 1] = 1
        action[np.isnan(action)] = 1

        # 用于返回的状态和奖励
        self.state = 0
        self.reward = 0

        # 有几个需要计算卸载
        rk = np.sum(action > 0)

        # 所有用户卸载了多少到边缘服务器，之后依据这个按比例分配计算资源
        sum_c = 0
        for i in range(self.K):
            if action[i] > 0:
                sum_c += self.Cn[i] * action[i]

        mw = pow(10, -174 / 10) * 0.001     # 噪声功率转化 -174dbm 转成瓦特
        for i in range(self.K):
            if action[i] > 0:
                tmp_rn = self.W * 1000 / rk * 1000  # W / K 速率公式的一部分
                rn = tmp_rn * np.log2(1 + self.pn * 0.001 * pow(self.dist[i], -3) / (tmp_rn * mw))      # 计算速率

                # 部分卸载部分的第一步卸载延迟
                to1 = action[i] * self.Dn[i] * 1024 / rn

                # 部分卸载的第二步计算延迟
                to2 = action[i] * self.Cn[i] / (self.F * 1000 * action[i] * self.Cn[i] / sum_c)

                # 部分卸载的本地计算部分 1-action
                tl = (1 - action[i]) * self.Cn[i] / (self.f * 1000)

                # 时延是max(本地计算延迟，计算卸载的部分的延迟)
                self.state += max(to1 + to2, tl)

            elif action[i] == 0:
                # 本地执行的延迟
                self.state += (self.Cn[i]) / (self.f * 1000)

        # self.reward = (self.pre_state - self.state) / self.pre_state
        # 奖励是状态的相反数
        self.reward = -self.state

        return self.state, self.reward, False, {}

    def reset(self):
        # random_action = np.random.uniform(0, 1, self.K)
        # state, _, _, _ = self.step(random_action)
        # state, _, _, _ = self.step(np.array([0.5] * self.K))
        state, _, _, _ = self.step(np.zeros(self.K))
        return state

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-ue', type=int, default=5)    # 用户数量
    parser.add_argument('--F', type=int, default=5)         # 边缘服务器计算量
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print(args)

    num_ue = args.num_ue
    F = args.F

    env = Env(W=10, F=5, K=num_ue,
              Dn=np.random.uniform(300, 500, num_ue), Cn=np.random.uniform(900, 1100, num_ue),
              f=1, dist=np.random.uniform(0, 200, num_ue), pn=500, pi=100)

    state, reward, _, _ = env.step(np.ones(num_ue))
    print(state)
    state, reward, _, _ = env.step(np.array([0.5, 0.5, 0.5, 0.5, 0.5]))
    print(state)

    state, reward, _, _ = env.step(np.array([1/3, 1/3, 1/3, 2/3, 2/3]))
    print(state)
