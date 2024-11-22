import os
import tensorflow as tf
from tensorflow.keras import layers, models, Input
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set the paths
train_dir = 'dataset/train'
test_dir = 'dataset/test'
data_dir = 'C:/Steganalysis CNN/dataset'
model_save_path = 'saved_model/steganography_cnn_model.h5'

def build_model():
    model = models.Sequential([
        # Explicit Input layer
        Input(shape=(128, 128, 3)),  
        
        # Convolutional and pooling layers
        layers.Conv2D(32, (3, 3), activation='relu'),  
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Flattening and dense layers
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # For binary classification
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_gen = datagen.flow_from_directory(
        train_dir,
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )

    val_gen = datagen.flow_from_directory(
        train_dir,
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )

    model = build_model()
    model.fit(train_gen, validation_data=val_gen, epochs=10)
    model.save(model_save_path)
    print(f'Model saved to {model_save_path}')

if __name__ == "__main__":
    train_model()
