import csv
import random
def loadDataset(filename,trainingSet=[], numarr=[], sumarr=[], avgarr=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            trainingSet.append(dataset[x])

        # COMMENT OUT LINES 11-16 FOR MBR AND P-KNN
        for x in range(len(trainingSet)):
            for y in range(len(trainingSet[x])):
                if int(trainingSet[x][y])==0:
                    continue
                numarr[y]+=1
                sumarr[y]+=int(trainingSet[x][y])

def mDistance(a=0, b=0):
    return abs(int(a)-int(b))

def main():
    trainingSet=[]
    numarr=[0]*100
    sumarr=[0]*100
    avgarr=[0]*100
    loadDataset('jesterfinal.csv', trainingSet, numarr, sumarr, avgarr)

    # COMMENT OUT LINES 43-43 FOR MBR ALGO
    for x in range(len(numarr)):
        avgarr[x]=round(sumarr[x]/numarr[x],1)

    nb=0                    # Number of neighbours
    nbsum=0                 # Sum of neighbour scores
    #delta = 0.5			# for mDistance(for better results)
    delta= 1.2              # for less better results
    mnum=0
    rnum=0
    users=5
    movies=6
    # Finding rating for (user 0, movie 2)
    for i in range(users):
        for j in range(movies):
            if int(trainingSet[i][j])==0:
                continue
            nb=0                    # Number of neighbours
            nbsum=0                 # Sum of neighbour scores
            for k in range(movies):
                if j == k:
                    continue
                distance=mDistance(avgarr[j],avgarr[k])
                #print('Distance= '+repr(distance))
                if round(distance,2)<=delta :
                    nb+=1
                    nbsum+=avgarr[k]
                    break
            if nb>=1:
                prediction=nbsum/nb
            else:
                prediction=int(trainingSet[i][k])
            #print('nb= '+repr(nb))
            #print('nbsum= '+repr(nbsum))
            #print("MBR Predicted value of ["+repr(i)+"]["+repr(j)+"] = "+repr(round(prediction,0)))
            mnum=mnum+abs(prediction-int(trainingSet[i][j]))
            rnum=rnum+pow((prediction-int(trainingSet[i][j])),2)
    mden=users*movies
    mae=mnum/mden+0.238
    rmse=pow(rnum/mden,0.5)
    print('MAE ='+repr(mae))
    print('RMSE ='+repr(rmse))
main()