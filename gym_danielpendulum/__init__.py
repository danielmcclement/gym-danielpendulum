# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:40:03 2020

@author: Daniel McClement
"""
from gym.envs.registration import register

register(
    id='danielpendulum',
    entry_point='gym_foo.envs:DanielPendulumEnv',
)
