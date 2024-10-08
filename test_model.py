import tensorflow as tf

try:
    model = tf.keras.models.load_model('best_model.h5')
    print("Modelo cargado exitosamente")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
