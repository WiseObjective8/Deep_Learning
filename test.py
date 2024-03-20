# import keras
# import tensorflow as tf
# import matplotlib.pyplot as plt
# image_path = 'test2.jpg'
# img = plt.imread(image_path)
# plt.imshow(img)
# plt.show()
# classes = ["T-shirt/top", "Trouser", "Pullover", "Dress",
#            "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankel boot"]

# model = keras.models.load_model("./save_models/KerasMultiClass")
# height, width = 28, 28
# img = keras.preprocessing.image.load_img(
#     image_path, target_size=(height, width))
# img_array = keras.preprocessing.image.img_to_array(img)
# plt.imshow(img)
# img_array = tf.image.rgb_to_grayscale(img_array)
# plt.imshow(img_array)
# plt.show()
# img_array = tf.reshape(img_array, (28, 28))
# img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
# img_array /= 255.0
# predictions = model(img_array)
# predicted_class_index = tf.argmax(predictions, axis=1)
# predicted_class_label = classes[predicted_class_index.numpy()[0]]
# print(f'Predicted class: {predicted_class_label}')
# plt.show()
