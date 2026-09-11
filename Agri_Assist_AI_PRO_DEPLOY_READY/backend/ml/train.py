import argparse
from pathlib import Path
import tensorflow as tf

parser=argparse.ArgumentParser()
parser.add_argument("--data_dir",required=True)
parser.add_argument("--epochs",type=int,default=8)
a=parser.parse_args()

data=Path(a.data_dir)
out=Path(__file__).resolve().parents[1]/"ml_model"
out.mkdir(exist_ok=True)

train=tf.keras.utils.image_dataset_from_directory(
    data,validation_split=.2,subset="training",seed=42,image_size=(224,224),batch_size=32)
val=tf.keras.utils.image_dataset_from_directory(
    data,validation_split=.2,subset="validation",seed=42,image_size=(224,224),batch_size=32)

classes=train.class_names
(out/"classes.txt").write_text("\n".join(classes),encoding="utf-8")

base=tf.keras.applications.MobileNetV2(input_shape=(224,224,3),include_top=False,weights="imagenet")
base.trainable=False
inputs=tf.keras.Input(shape=(224,224,3))
x=tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
x=base(x,training=False)
x=tf.keras.layers.GlobalAveragePooling2D()(x)
x=tf.keras.layers.Dropout(.2)(x)
outputs=tf.keras.layers.Dense(len(classes),activation="softmax")(x)
model=tf.keras.Model(inputs,outputs)
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
history = model.fit(train,validation_data=val,epochs=a.epochs)
metrics = model.evaluate(val, verbose=0, return_dict=True)
model.save(out/"crop_disease.keras")
print("Validation metrics:", {key: round(float(value), 4) for key, value in metrics.items()})
print("Saved",out/"crop_disease.keras")
