
import json
from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf

class ModelPredic:

    def __init__(self, dataX=[], dataY=[]):
        self.dataX = dataX
        self.dataY = dataY
        self.setDatagetData()

    def modelPredict(self):
        self.setDatagetData()
        self.core()
        self.modelFit()
        self.plotHistory()
        self.getWeights()
        self.setOutput()
    
    def core(self):
        self.oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
        self.oculta2 = tf.keras.layers.Dense(units=3)
        self.salida = tf.keras.layers.Dense(units=1)
        self.model = tf.keras.Sequential([self.oculta1, self.oculta2, self.salida])

        self.model.compile(
            optimizer = tf.keras.optimizers.Adam(0.1),
            loss = 'mean_squared_error'
        )
        self.output = []

    def modelFit(self):
        self.historial = self.model.fit(self.celsius, self.fahrenheit, epochs=1000, verbose=False)
        self.output.append(self.historial.history["loss"])

    def plotHistory(self):
        plt.xlabel("# epoca")
        plt.ylabel("Magnitud de perdida")
        plt.plot(self.historial.history["loss"])
        plt.savefig("historyLoss.jpg")

    def getWeights(self):
        resultado1 = self.oculta1.get_weights()
        resultado2 = self.oculta2.get_weights()
        resultado3 = self.salida.get_weights()
        self.output.append([resultado1, resultado2, resultado3])

    def setDataX(self, dataX):
        self.dataX = dataX

    def setDataY(self, dataY):
        self.dataY = dataY

    def setDatagetData(self):
        self.celsius = np.array(self.dataX, dtype=float)
        self.fahrenheit = np.array(self.dataY, dtype=float)

    def setX(self, x):
        self.x = x

    def setOutput(self):
        self.output.append(self.model.predict([self.x]))

    def getOutput(self):
        prediction = self.output[len(self.output)-1][0][0]
        output = json.dumps({"output":str(prediction)}, sort_keys=True, indent=4)
        return output
