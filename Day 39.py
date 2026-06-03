class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        def calc(start1, dur1, start2, dur2):

            min_end = float('inf')

            for s, d in zip(start1, dur1):
                min_end = min(min_end, s + d)

            ans = float('inf')

            for s, d in zip(start2, dur2):
                ans = min(ans, max(min_end, s) + d)

            return ans

        land_then_water = calc(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        water_then_land = calc(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(land_then_water, water_then_land)


n = int(input("Enter number of land rides: "))
landStartTime = list(map(int, input("Enter land start times: ").split()))
landDuration = list(map(int, input("Enter land durations: ").split()))

m = int(input("Enter number of water rides: "))
waterStartTime = list(map(int, input("Enter water start times: ").split()))
waterDuration = list(map(int, input("Enter water durations: ").split()))

obj = Solution()

result = obj.earliestFinishTime(
    landStartTime,
    landDuration,
    waterStartTime,
    waterDuration
)

print("Earliest Finish Time:", result)


Enter number of land rides: 2
Enter land start times: 2 8
Enter land durations: 4 1
Enter number of water rides: 1
Enter water start times: 6
Enter water durations: 3


Earliest Finish Time: 9