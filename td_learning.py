from __future__ import print_function

import random

ALPHA = 0.1
GAMMA = 1

U = {}
R = {}

MAX_X = 4
MAX_Y = 3

WALL_STATE = (2, 2)

TERMINAL_POSITIVE_STATE = (4, 3)
TERMINAL_POSITIVE_REWARD = 10

TERMINAL_NEGATIVE_STATE = (4, 2)
TERMINAL_NEGATIVE_REWARD = -10

ACTIONS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

NUM_EPISODES = 1000


def get_actions():
    return ACTIONS.keys()


def get_valid_actions_and_next_states(s):
    valid_actions = []
    valid_next_states = []
    valid_states = U.keys()
    for action in get_actions():
        s_next = result(s, action)
        if s_next in valid_states:
            valid_actions.append(action)
            valid_next_states.append(s_next)
    return valid_actions, valid_next_states


def result(s, a):
    return s[0] + ACTIONS[a][0], s[1] + ACTIONS[a][1]


def choose_random_next_state(s):
    actions, next_states = get_valid_actions_and_next_states(s)
    return random.choice(next_states)


def initialize_rewards():
    for x in range(1, MAX_X + 1):
        for y in range(1, MAX_Y + 1):
            if (x, y) != WALL_STATE and (x, y) != TERMINAL_POSITIVE_STATE and (x, y) != TERMINAL_NEGATIVE_STATE:
                R[(x, y)] = 0
    R[TERMINAL_POSITIVE_STATE] = TERMINAL_POSITIVE_REWARD
    R[TERMINAL_NEGATIVE_STATE] = TERMINAL_NEGATIVE_REWARD


def initialize_utility():
    for x in range(1, MAX_X + 1):
        for y in range(1, MAX_Y + 1):
            if (x, y) != WALL_STATE and (x, y) != TERMINAL_POSITIVE_STATE and (x, y) != TERMINAL_NEGATIVE_STATE:
                U[(x, y)] = 0
    U[TERMINAL_POSITIVE_STATE] = TERMINAL_POSITIVE_REWARD
    U[TERMINAL_NEGATIVE_STATE] = TERMINAL_NEGATIVE_REWARD


def td_update(s, s_next):
    U[s] = U[s] + ALPHA * (R[s] + GAMMA * U[s_next] - U[s])


def terminal_state(s):
    return s == TERMINAL_POSITIVE_STATE or s == TERMINAL_NEGATIVE_STATE


def print_state(s):
    print('-----------------')
    for y in range(MAX_Y, 0, -1):
        for x in range(1, MAX_X + 1):
            char = ' '
            if (x, y) == s:
                char = 'X'
            elif (x, y) == WALL_STATE:
                char = '#'
            print('| {} '.format(char), end='')
        print()
        print('-----------------')
    print()


def print_utilities():
    print('-----------------------------------')
    for y in range(MAX_Y, 0, -1):
        for x in range(1, MAX_X + 1):
            print('| {} '.format('#####' if (x, y) == WALL_STATE else '{:5.3f}'.format(U[(x, y)])), end='')
        print()
        print('-----------------------------------')
    print()


def q1():
    initialize_rewards()
    initialize_utility()
    for i in range(NUM_EPISODES):
        print('Episode {}'.format(i))
        s = (1, 1)
        while not terminal_state(s):
            print(s)
            print_state(s)
            s_next = choose_random_next_state(s)
            td_update(s, s_next)
            s = s_next
    print_utilities()


if __name__ == '__main__':
    q1()
