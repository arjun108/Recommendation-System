import csv
import random
import math
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

def pearsonDistance(trainingSet=[], avgarr=[], m=0, k=0):
    num=0
    denr=0
    denl=0
    for x in range(len(trainingSet)):
        num+=(abs(int(trainingSet[x][m])-int(avgarr[m])))*abs((int(trainingSet[x][k])-int(avgarr[k])))
        denl+=pow(abs(int(trainingSet[x][m])-int(avgarr[m])),2)
        denr+=pow(abs(int(trainingSet[x][k])-int(avgarr[k])),2)
    den=denl*denr
    den=pow(den,0.5)
    pd=round(1-(num/den),2)
    #print('Pearson Distance of '+repr(k)+' is: '+repr(pd))
    return pd

def main():
    trainingSet=[]
    numarr=[0]*6
    sumarr=[0]*6
    avgarr=[0]*6
    loadDataset('pdf_testSet.csv', trainingSet, numarr, sumarr, avgarr)

    # COMMENT OUT LINES 43-43 FOR MBR ALGO
    for x in range(len(numarr)):
        avgarr[x]=round(sumarr[x]/numarr[x],1)
    #print('Train set: ' + repr(len(trainingSet)))
    delta = 0.6             # Threshold    
    mnum=0
    rnum=0
    users=5
    movies=6

    for i in range(users):
        for j in range(movies):
            if int(trainingSet[i][j])==0:
                continue
            nb=0                    # Number of neighbours
            nbsum=0                 # Sum of neighbour scores
            for k in range(movies):
                if j == k:
                    continue
                distance=pearsonDistance(trainingSet,avgarr,j,k)
                #print('Distance= '+repr(distance))
                if round(distance,2)<=delta :
                    nb+=1
                    nbsum+=int(trainingSet[i][k])
            if nb>=1:
                prediction=nbsum/nb
            else:
                prediction=int(trainingSet[i][k])
            #print('nb= '+repr(nb))
            #print('nbsum= '+repr(nbsum))
            #print("Pearson Predicted value of ["+repr(i)+"]["+repr(j)+"] = "+repr(round(prediction,0)))
            mnum=mnum+abs(prediction-int(trainingSet[i][j]))
            rnum=rnum+pow((prediction-int(trainingSet[i][j])),2)
    mden=users*movies
    mae=mnum/mden
    rmse=pow(rnum/mden,0.5)
    print('MAE ='+repr(mae))
    print('RMSE ='+repr(rmse))
main()