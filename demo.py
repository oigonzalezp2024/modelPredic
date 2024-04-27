
from modelPredic import ModelPredic

redNeuronal = ModelPredic()
redNeuronal.setDataX([-40, -10, 0, 8, 15, 22, 38])
redNeuronal.setDataY([-40, 14, 32, 46, 59, 72, 100])
redNeuronal.setX(100.0)
redNeuronal.modelPredict()
prediction = redNeuronal.getOutput()
print(prediction)
