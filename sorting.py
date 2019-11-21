from matplotlib import pyplot as plt
import time

class data: ##데이터 저장 클래스
    def __init__(self):
        self.data = [] ##리스트 형태로 저장 2*2 리스트

    def addData(self, inputData): ##리스트 추가 메소드
        self.data.append(inputData)

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

    
    def bubbleSort(self, column): #column은 sort 기준으로 삼을 속성 index
        dataLen = len(self.data) - 1
        for i in range(dataLen):
            for j in range(dataLen - i):
                if self.data[j][column] > self.data[j + 1][column]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]




if __name__ == "__main__":   

    csvFile = open("/programming/GitHub/sortingAnalysis/boston.csv", mode='r') ## 파일 객체 생성
    timeList = [] #그래프를 그리기 위해 데이터 수 각각의 sort 시간을 저장할 리스트 생성
    

    ## 데이터 초기 설정
    bostonData = data() #데이터 객체 생성
    csvFile.readline()  # 속성이 적혀있는 첫번째 row 읽고 버림
    for i in csvFile: 
        i = i.split(',')  #문자열을 ',' 기준으로 나눔
        temp = []
        for j in i:
            temp.append(float(j))  #나눈 문자열을 실수(대부분의 값이 실수임)로 변경
        bostonData.addData(temp) #클래스에 저장
        startTime = time.time() #타이머 시작
        bostonData.bubbleSort(12) #12번 컬럼을 기준으로 소팅
        endTime = time.time() #타이머 저장
        totalTime = endTime - startTime #끝난 시간 - 시작 시간(총 걸린 시간) 
        timeList.append(totalTime)
        print("data len : ", len(bostonData.data), " sorting time : ", '%.10f' % totalTime)
    
    ##표 그리기
    plt.title("bubble sort") #그래프 제목
    plt.xlabel("number of dataset") #x축 
    plt.ylabel("sorting time(s)")#y축
    i = range(0, len(bostonData.data))
    plt.plot(i, timeList, 'b', label = "data") #그래프 그리기
    #plt.legend(loc="upper right")
    plt.savefig("bubbleSort.png") #파일로 저장

    

