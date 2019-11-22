from matplotlib import pyplot as plt
import time

class data: ##데이터 저장 클래스
    def __init__(self):
        self.data = [] ##리스트 형태로 저장 2*2 리스트

    def addData(self, inputData): ##리스트 추가 메소드
        self.data.append(inputData)
    
    def setData(self, inputData):
        self.data = inputData

    def printData(self, i, row = 0, column = 0):
        #i = 0 : 전부 출력, i = 1 : 해당 row 출럭, i = 2 : 해당 row column 출력, i = 3 : 해당 colum 출력
        #ex) print(i=0) print(i=1, row=4) print(i=2, row=2, column=4) print(i=3, column=2)
        if i == 0:
            print(self.data)
        if i == 1:
            print(self.data[row])
        if i == 2:
            print(self.data[row][column])
        if i == 3:
            temp = 0
            for i in self.data:
                if (temp % 5) == 0:
                    print()
                print(i[column], end=" ")
                temp = temp + 1

    def selectionSort(self, column):
        temp = self.data
        for i in range(len(temp) - 1):
            min_idx = i
            for j in range(i + 1, len(temp)):
                if temp[j][column] < temp[min_idx][column]:
                    min_idx = j
                    temp[i], temp[min_idx] = temp[min_idx], temp[i]

        return temp

    def bubbleSort(self, column): #column은 sort 기준으로 삼을 속성 index
        temp = self.data
        dataLen = len(temp) - 1
        for i in range(dataLen):
            for j in range(dataLen - i):
                if temp[j][column] > temp[j + 1][column]:
                    temp[j], temp[j+1] = temp[j+1], temp[j]
                    




if __name__ == "__main__":   

    csvFile = open("/programming/GitHub/sortingAnalysis/boston.csv", mode='r') ## 읽기 전용 파일 객체 생성
    outFile = open("/programming/GitHub/sortingAnalysis/bostonOut.csv", mode='w') ## 쓰기 전용 파일 객체 생성
    
    
    #그래프를 그리기 위해 데이터 수 각각의 sort 시간을 저장할 리스트 생성
    selectionTimeList = []
    bubbleTimeList = [] 
    

    ## 데이터 처리 시간 비교
    bostonData = data() #데이터 객체 생성
    temp = csvFile.readline()  # 속성이 적혀있는 첫번째 row 읽고 버림
    print(temp)
    outFile.write(temp)
    for i in csvFile: 
        i = i.split(',')  #문자열을 ',' 기준으로 나눔
        temp = []
        for j in i:
            temp.append(float(j))  #나눈 문자열을 실수(대부분의 값이 실수임)로 변경
        bostonData.addData(temp) #클래스에 저장

        ## selectionSort
        startTime = time.time() #타이머 시작
        bostonData.selectionSort(12) #12번 컬럼을 기준으로 소팅
        endTime = time.time() #타이머 저장
        totalTime = endTime - startTime #끝난 시간 - 시작 시간(총 걸린 시간) 
        selectionTimeList.append(totalTime)

        ## bubbleSort
        startTime = time.time() #타이머 시작
        bostonData.bubbleSort(12) #12번 컬럼을 기준으로 소팅
        endTime = time.time() #타이머 저장
        totalTime = endTime - startTime #끝난 시간 - 시작 시간(총 걸린 시간) 
        bubbleTimeList.append(totalTime)

        print("data len : ", len(bostonData.data), " sorting time : ", '%.10f' % totalTime)

    
    ##표 그리기
    plt.title("Time performance of sorting algorithms") #그래프 제목
    plt.xlabel("number of dataset") #x축 
    plt.ylabel("sorting time(s)")#y축
    i = range(0, len(bostonData.data))
    plt.plot(i, selectionTimeList, 'r', label = "selection sort") #그래프 그리기
    plt.plot(i, bubbleTimeList, 'b', label = "blubble sort") #그래프 그리기
    
    plt.legend(loc=2)
    plt.savefig("/programming/GitHub/sortingAnalysis/sorting.png") #파일로 저장

    ##최종 csv 파일 생성
    bostonData.setData(bostonData.selectionSort(12))
    for i in bostonData.data:
        outFile.writelines(str(i)+'\n')


