from embedder import predictor

predictor.model.summary()
print(predictor.model.predict([1, 2, 3, 4]))
