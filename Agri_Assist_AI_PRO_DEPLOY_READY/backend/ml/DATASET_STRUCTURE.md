# Disease Dataset

Recommended dataset: PlantVillage, downloaded through the included TensorFlow Datasets exporter.

Install the dataset/training dependencies and export it from the repository root:
```powershell
pip install -r backend/requirements-ml.txt
python backend/ml/download_plantvillage.py --output_dir dataset
```

Review PlantVillage licensing and attribution terms before redistributing images or trained models.

Arrange images like:
dataset/
  Tomato_Early_Blight/
    image1.jpg
    image2.jpg
  Tomato_Late_Blight/
    image1.jpg
  Tomato_Healthy/
    image1.jpg

Then:
python backend/ml/train.py --data_dir dataset

The exact class names depend on the dataset you choose. Evaluate accuracy, precision,
recall, confusion matrix and per-class performance before using the model in a final demo.
