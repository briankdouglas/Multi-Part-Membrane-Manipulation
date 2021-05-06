rawData = []
newData = []
output = []
avg = 0.0
minLength = 6
spikesUnsorted = []
spikes = []
numSpikes = 3

def endpoint(x, a):
    return( (a-rawData[x]) / (rawData[x]-rawData[x-1]) + x )

def rawOutput(x):
    print("Raw Output:")
    finalString = ""
    for i in x:
        finalString += (str(i) + "\n")
    print(finalString)

def area(endpoint1, start, end, endpoint2):
    totalArea = 0
    totalArea += (start - endpoint1) * (avg + rawData[start]) / 2
    #print(totalArea)
    for x in range(start, end):
        totalArea += (rawData[x] + rawData[x+1]) / 2
    #print(totalArea - ((start - endpoint1) * (avg + rawData[start]) / 2) )
    totalArea += (endpoint2 - end) * (rawData[end] + avg) / 2
    #print((endpoint2 - end) * (rawData[end] + avg) / 2)
    #print("")
    return(totalArea)


def main():
    while True:
        line = raw_input()
        if line:
            rawData.append(float(line))
        else:
            break
    
    avg = sum(rawData)/len(rawData)
    print("Average: " + str(avg))

    for i in rawData:
        if i == avg:
            newData.append(0)
        elif i > avg:
            newData.append(1)
        else:
            newData.append(-1)

    length = 1
    for x in range(1,len(newData)):
        if newData[x-1] * newData[x] > 0:
            length += 1
        if newData[x-1] * newData[x] <= 0:
            if length >= minLength:
                confidence = round(max(max(rawData[x-length : x-1])-avg, avg-min(rawData[x-length : x-1])) / (max(rawData)-avg), 2)
                spikesUnsorted.append([ confidence, length, x-length, x-1, area( endpoint(x-length, avg), x-length, x-1, endpoint(x, avg) ) ])
            length = 1 

    for i in sorted(spikesUnsorted):
        spikes.insert(0,i)
        
    rawOutput(spikes)

    for x in range(len(rawData)):
        output.append(0)

    for x in range(numSpikes):
        for y in range(spikes[x][1]):
            output[spikes[x][2] + y] = 4 #spikes[x][1]

    rawOutput(output)
    
main()
