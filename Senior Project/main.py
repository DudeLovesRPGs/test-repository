import tensorflow as tf
from keras.callbacks import EarlyStopping
from keras import regularizers
from keras.constraints import unit_norm
import pathlib
import numpy as np
import matplotlib.pyplot as plt

#Image width and height and batch size. Tweaked batch size from 64 to 68, since it seems to give me more consistent
#results.
img_height, img_width = [256, 256]
batch_size =128

#Grabbing data from directory.
data_dir = './CNN/'
data_dir = pathlib.Path(data_dir)

#Splitting data into training and testing data sets.
train_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2, subset="training", seed=123, image_size=(img_height, img_width), batch_size=batch_size, shuffle = True)
val_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2, subset="validation", seed=123, image_size=(img_height, img_width), batch_size=batch_size, shuffle = True)

#Grabbing and printing class names.
class_names = train_ds.class_names
print(class_names)

#Rescaling every image to be in range 0-255.
normalization_layer = tf.keras.layers.Rescaling(1./255)

#Normalizing data
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]

# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))


AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
num_classes = 4
num_epochs = 23


model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(16, kernel_size=(3,3), padding = 'same', activation='relu', kernel_regularizer= regularizers.l2(0.0001), kernel_constraint= unit_norm()),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides =2),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.Conv2D(32, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer= regularizers.l2(0.0001), kernel_constraint= unit_norm()),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides = 2),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.Conv2D(64, kernel_size=(5,5), padding = 'same', activation='relu', kernel_regularizer= regularizers.l2(0.0001)),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides = 2),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.Conv2D(128, kernel_size=(2,2), padding = 'same', activation = 'relu', kernel_regularizer= regularizers.l2(0.0001)),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides =2),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.Conv2D(256, kernel_size=(2,2), padding = 'same', activation = 'relu'),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides =2),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.0001), kernel_constraint= unit_norm()),
  tf.keras.layers.Dropout(0.40),
  tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.0001), kernel_constraint= unit_norm()),
  tf.keras.layers.Dropout(0.20),
  tf.keras.layers.Dense(num_classes, activation='softmax')
])

#Same setting as in Homework 1-2, but seems to work much better.
model.compile(optimizer='adam', loss=tf.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'] )
early_stopping = EarlyStopping(patience = 2)
rms = tf.keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=1,
                                             verbose=1)
history = model.fit(train_ds, validation_data=val_ds, epochs=num_epochs)
print(history.history['val_accuracy'][num_epochs - 1])
model.save('./SavedModels/Val_acc-%s_Val_loss-%s' % (history.history['val_accuracy'][num_epochs - 1], history.history['val_loss'][num_epochs - 1]))

#All stuff for the graphs
y_vloss = history.history['val_loss']
y_loss = history.history['loss']
y_acc = history.history['accuracy']
y_vacc = history.history['val_accuracy']
plt.figure(facecolor= "white")
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(np.arange(len(y_vloss)), y_vloss, marker='.', c='red')
ax1.plot(np.arange(len(y_loss)), y_loss, marker='.', c='blue')
ax1.grid()
plt.setp(ax1, xlabel='epoch', ylabel='loss')

ax2.plot(np.arange(len(y_vacc)), y_vacc, marker='.', c='red')
ax2.plot(np.arange(len(y_acc)), y_acc, marker='.', c='blue')
ax2.grid()
plt.setp(ax2, xlabel='epoch', ylabel='accuracy')
plt.savefig("./Output/Val_acc-%s_Val_loss-%s.png" % (history.history['val_accuracy'][num_epochs - 1], history.history['val_loss'][num_epochs - 1]), dpi = 300, facecolor = "w", edgecolor = "w")
#plt.show()



