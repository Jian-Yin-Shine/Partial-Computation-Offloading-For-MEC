# Partial-Computation-Offloading-For-MEC
基于深度强化学习的部分计算任务卸载延迟优化

<img src="resources/fig1.png"/>

This repository provides the official Tensorflow implementation for the following paper:

**Intelligent Delay-Aware Partial Computing Task Offloading for Multi-User Industrial Internet of Things through Edge Computing**

> Abstract: The development of Industrial Internet of Things (IIoT) and Industry 4.0 has completely changed the traditional manufacturing industry. Intelligent IIoT technology usually involves a large number of intensive computing tasks. Resource-constrained IIoT devices often cannot meet the real-time requirements of these tasks. As a promising paradigm, Mobile Edge Computing (MEC) system migrates the computation intensive tasks from resource-constrained IIoT devices to nearby MEC servers, thereby obtaining lower delay and energy consumption. However, considering the varying channel conditions as well as the distinct delay requirements for various computing tasks, it is challenging to coordinate the computing task offloading among multiple users. In this paper, we propose an autonomous partial offloading system for delay sensitive computation tasks in multi-user IIoT MEC systems. Our goal is to provide offloading services with minimum delay for better Quality of Service (QoS). Enlighten by the recent advancement of Reinforcement Learning (RL), we propose two RL based offloading strategies to automatically optimize the delay performance. Specifically, we first implement Q-learning algorithm to provide a discrete partial offloading decision. Then, to further optimize the system performance with more flexible task offloading, the offloading decisions are given as continuous based on Deep Deterministic Policy Gradient (DDPG). The simulation results show that, the Q-learning scheme reduces the delay by 23%, and the DDPG scheme reduces the delay by 30%.

## Method
The overall architecture of our method:

<img src="resources/fig2.png"/>

## Citation

If you find our work helpful to your research, please cite our paper:

```
@article{deng2021intelligent,
  title={Intelligent Delay-Aware Partial Computing Task Offloading for Multi-User Industrial Internet of Things through Edge Computing},
  author={Deng, Xiaoheng and Yin, Jian and Guan, Peiyuan and Xiong, Neal N and Zhang, Lan and Mumtaz, Shahid},
  journal={IEEE Internet of Things Journal},
  year={2021},
  publisher={IEEE}
}
```