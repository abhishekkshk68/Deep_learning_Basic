#code written by Abhishek Kaushik
import keras
#five steps of neural network
from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
#Define Network
#input
visible=Input(shape=(10,))
#Three input layers
#first hidden ;ayer
hidden1=Dense(10,activation='relu')(visible)
#Second hidden layer
hidden2=Dense(20,activation='relu')(hidden1)
#Third hidden layer
hidden3=Dense(10,activation='relu')(hidden2)
#outpot
output=Dense(1,activation='sigmoid')(hidden3)


#Compile network

model=Model(input=visible,output=output)
#Fit Network
#Evaluate Network
#Make predictions
# This things will dicuss in the futher neural network
#for now we will see only the summary of the Modal
print(model.summary())
#plot_model(model,to_file=r'C:\Users\Abhi\Google Drive\PycharmProjects\deep_learning\MLP.png')