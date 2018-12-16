#!/bin/python3


def bon_appetit(costs, item_anna_skipped, brian_charged_anna):
    annas_share = cost_of_annas_share(costs, item_anna_skipped)
    if (brian_charged_anna == annas_share):
        return "Bon Appetit"
    else:
        return brian_charged_anna - annas_share


def cost_of_annas_share(costs, item_anna_skipped):
    return int(sum(costs[:item_anna_skipped] +
                   costs[item_anna_skipped + 1:]) / 2)


_, item_anna_skipped = list(map(int, input().strip().split(' ')))
costs = list(map(int, input().strip().split(' ')))
brian_charged_anna = int(input().strip())
print(bon_appetit(costs, item_anna_skipped, brian_charged_anna))
