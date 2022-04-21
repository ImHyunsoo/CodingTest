def solution(lines):

    # get input
    S, E = [], []
    totalLines = 0
    for line in lines:
        totalLines += 1
        type(line)
        (d, s, t) = line.split(" ")

       # time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        # E.append(seconds)
        S.append(seconds - t + 0.001)

    # count the maxTraffic
    S.sort()

    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while((countE < totalLines) & (countS < totalLines)):
        if(S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else:  # it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic


lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
         "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
# lines = ["2016-09-15 00:00:00.000 3s"]  # 1 // o
# lines = ["2016-09-15 23:59:59.999 0.001s"]  # 1 // o
# lines = ["2016-09-15 01:00:04.001 2.0s",
#          "2016-09-15 01:00:07.000 2s"]  # 1 // o
# lines = ["2016-09-15 01:00:04.002 2.0s",
#          "2016-09-15 01:00:07.000 2s"]  # 2 // o
# lines = ["2016-09-15 00:00:00.000 2.3s",
#  "2016-09-15 23:59:59.999 0.1s"]  # 1 // o
result = solution(lines)
print(result)
