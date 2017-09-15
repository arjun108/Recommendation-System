import csv
import random
import math
def loadDataset(filename,trainingSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            trainingSet.append(dataset[x])

def cosineDistance(trainingSet=[], j=0, k=0):
    num=0
    denr=0
    denl=0
    for x in range(len(trainingSet)):
        num+=int(trainingSet[x][j])*int(trainingSet[x][k])
        denl+=pow(int(trainingSet[x][j]),2)
        denr+=pow(int(trainingSet[x][k]),2)
    den=denl*denr
    den=pow(den,0.5)
    cd=round(1-(num/den),2)
    #print('Cosine Distance of '+repr(k)+' is: '+repr(cd))
    return cd

def main():
    trainingSet=[]
    loadDataset('pdf_testSet.csv', trainingSet)
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
                distance=cosineDistance(trainingSet,j,k)
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
            #print("Cosine Predicted value of ["+repr(i)+"]["+repr(j)+"] = "+repr(round(prediction,0)))
            mnum=mnum+abs(prediction-int(trainingSet[i][j]))
            rnum=rnum+pow((prediction-int(trainingSet[i][j])),2)
    mden=users*movies
    mae=mnum/mden
    rmse=pow(rnum/mden,0.5)
    print('MAE ='+repr(mae))
    print('RMSE ='+repr(rmse))
main()