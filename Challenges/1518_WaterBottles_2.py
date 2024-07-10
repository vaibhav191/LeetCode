class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
# for every numExchange-1 empty water bottle, we can drink one water bottle that we currently have, then add it to the
# number of empties then exchange them to get one more full water bottle.
# now for every numBottles-1 empty bottle, we can drink one bottle and add it to it to get one free bottle

