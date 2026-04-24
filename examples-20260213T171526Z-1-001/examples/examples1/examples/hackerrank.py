# def countResponseTimeRegressions(responseTimes):
#     counts = []
#     for i in range(len(responseTimes)):
#         count = sum(1 for j in range(i) if responseTimes[j] < responseTimes[i] )
#         counts.append(count)
#     return counts

# res = [100, 200, 150, 300]
# print(countResponseTimeRegressions(res))

def countResponseTimeRegressions(responseTimes):
    counts = []
    for i in range(len(responseTimes)):
        if i == 0:
            counts.append(0)
        else:
            if all(responseTimes[i] > responseTimes[j] for j in range(i)):
                counts.append(1)
            else:
                counts.append(0)
    return sum(counts)


if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
