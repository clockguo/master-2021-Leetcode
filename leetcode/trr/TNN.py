

# import tensorflow as tf
#
# hello = tf.constant("Hello!TensorFlow")
# sess = tf.Session()
# print(sess.run(hello))
#
# import tensorflow as tf
# # mnist = tf.keras.datasets.mnist
# # (x_train, y_train),(x_test, y_test) = mnist.load_data()
# # x_train, x_test = x_train / 255.0, x_test / 255.0
# # model = tf.keras.models.Sequential([
# #   tf.keras.layers.Flatten(),
# #   tf.keras.layers.Dense(512, activation=tf.nn.relu),
# #   tf.keras.layers.Dropout(0.2),
# #   tf.keras.layers.Dense(10, activation=tf.nn.softmax)
# # ])
# # model.compile(optimizer='adam',
# #               loss='sparse_categorical_crossentropy',
# #               metrics=['accuracy'])
# # model.fit(x_train, y_train, epochs=5)
# # model.evaluate(x_test, y_test)
# # from sklearn import neural_network
# # from sklearn import naive_bayes
#
#
# a=tf.constant([1.0,2.0],name="a")
# b=tf.constant([2.0,3.0],name="b")
# result=a+b
# sess=tf.Session()#创建一个会话
# sess.run(result)#得到result的值
# print(a.graph is tf.get_default_graph())
#
# import tensorflow as tf
#
# node1 = tf.constant(3.0, dtype=tf.float32)
# node2 = tf.constant(4.0)  # also tf.float32 implicitly
# print(node1, node2)
#
# sess = tf.Session()
# print(sess.run([node1, node2]))
#
# # from __future__ import print_function
# node3 = tf.add(node1, node2)
# print("node3:", node3)
# print("sess.run(node3):", sess.run(node3))
#
# # 占位符
# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adder_node = a + b  # + provides a shortcut for tf.add(a, b)
#
# print(sess.run(adder_node, {a: 3, b: 4.5}))
# print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))
#
# add_and_triple = adder_node * 3.
# print(sess.run(add_and_triple, {a: 3, b: 4.5}))
# print(sess.run(add_and_triple, {a: [3,2], b:[2, 4.5]}))
#
# # 多个变量求值
# W = tf.Variable([.3], dtype=tf.float32)
# b = tf.Variable([-.3], dtype=tf.float32)
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b
#
# #  变量初始化
# init = tf.global_variables_initializer()
# sess.run(init)
#
# print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
#
# # loss function
# y = tf.placeholder(tf.float32)
# # print('\n',y)
# squared_deltas = tf.square(linear_model - y)
# #
# # print('\n',"squared_deltas:", sess.run(squared_deltas,{x: [1,2,4,5], y:[0,1,-1,2]}))
# #
# loss = tf.reduce_sum(squared_deltas)
# # print("loss function", sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
# #
# # ss = (0 - 0) * (0 - 0) + (0.3 + 1) * (0.3 + 1) + (0.6 + 2) * (0.6 + 2) + (0.9 + 3) * (0.9 + 3)  # 真实算法
# # print("真实算法ss", ss)
# #
# # print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, 0.3, 0.6, 0.9]}))  # 测试参数
#
# # tf.assign 变量重新赋值
# print('\n',"get try again",'\n')
# fixW = tf.assign(W, [-1.])
# fixb = tf.assign(b, [1.])
# sess.run([fixW, fixb])
# print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
# print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
#
# # tf.train API
# optimizer = tf.train.GradientDescentOptimizer(0.01)  # 梯度下降优化器
# train = optimizer.minimize(loss)  # 最小化损失函数
# sess.run(init)  # reset values to incorrect defaults.
# for i in range(1000):
#     sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
#
# print(sess.run([W, b]))
#
# print("------------------------------------1")
#
# # Complete program:The completed trainable linear regression model is shown here:完整的训练线性回归模型代码
# # Model parameters
# W = tf.Variable([.3], dtype=tf.float32)
# b = tf.Variable([-.3], dtype=tf.float32)
# # Model input and output
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b
# y = tf.placeholder(tf.float32)
#
# # loss
# loss = tf.reduce_sum(tf.square(linear_model - y))  # sum of the squares
# # optimizer
# optimizer = tf.train.GradientDescentOptimizer(0.01)
# train = optimizer.minimize(loss)
#
# # training data
# x_train = [1, 2, 3, 4]
# y_train = [0, -1, -2, -3]
# # training loop
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)  # reset values to wrong
# for i in range(1000):
#     sess.run(train, {x: x_train, y: y_train})
#
# # evaluate training accuracy
# curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
# print("W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))
#
# print("------------------------------------2")

# tf.estimator  使用tf.estimator实现上述训练
# Notice how much simpler the linear regression program becomes with tf.estimator:
# NumPy is often used to load, manipulate and preprocess data.
import numpy as np
import tensorflow as tf

# Declare list of features. We only have one numeric feature. There are many
# other types of columns that are more complicated and useful.
# feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]

# An estimator is the front end to invoke training (fitting) and evaluation
# (inference). There are many predefined types like linear regression,
# linear classification, and many neural network classifiers and regressors.
# The following code provides an estimator that does linear regression.
# estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

# TensorFlow provides many helper methods to read and set up data sets.
# Here we use two data sets: one for training and one for evaluation
# We have to tell the function how many batches
# of data (num_epochs) we want and how big each batch should be.
# x_train = np.array([1., 2., 3., 4.])
# y_train = np.array([0., -1., -2., -3.])
# x_eval = np.array([2., 5., 8., 1.])
# y_eval = np.array([-1.01, -4.1, -7, 0.])
# input_fn = tf.estimator.inputs.numpy_input_fn(
#     {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
# train_input_fn = tf.estimator.inputs.numpy_input_fn(
#     {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
# eval_input_fn = tf.estimator.inputs.numpy_input_fn(
#     {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)
#
# # We can invoke 1000 training steps by invoking the  method and passing the
# # training data set.
# estimator.train(input_fn=input_fn, steps=1000)
#
# # Here we evaluate how well our model did.
# train_metrics = estimator.evaluate(input_fn=train_input_fn)
# eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
# print("train metrics: %r" % train_metrics)
# print("eval metrics: %r" % eval_metrics)
#
# print("------------------------------------3")
#
#
# # A custom model：客户自定义实现训练
# # Declare list of features, we only have one real-valued feature
# def model_fn(features, labels, mode):
#     # Build a linear model and predict values
#     W = tf.get_variable("W", [1], dtype=tf.float64)
#     b = tf.get_variable("b", [1], dtype=tf.float64)
#     y = W * features['x'] + b
#     # Loss sub-graph
#     loss = tf.reduce_sum(tf.square(y - labels))
#     # Training sub-graph
#     global_step = tf.train.get_global_step()
#     optimizer = tf.train.GradientDescentOptimizer(0.01)
#     train = tf.group(optimizer.minimize(loss),
#                      tf.assign_add(global_step, 1))
#     # EstimatorSpec connects subgraphs we built to the
#     # appropriate functionality.
#     return tf.estimator.EstimatorSpec(
#         mode=mode,
#         predictions=y,
#         loss=loss,
#         train_op=train)
#
#
# estimator = tf.estimator.Estimator(model_fn=model_fn)
# # define our data sets
# x_train = np.array([1., 2., 3., 4.])
# y_train = np.array([0., -1., -2., -3.])
# x_eval = np.array([2., 5., 8., 1.])
# y_eval = np.array([-1.01, -4.1, -7., 0.])
# input_fn = tf.estimator.inputs.numpy_input_fn(
#     {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
# train_input_fn = tf.estimator.inputs.numpy_input_fn(
#     {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
# eval_input_fn = tf.estimator.inputs.numpy_input_fn(
#     {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)
#
# # train
# estimator.train(input_fn=input_fn, steps=1000)
# # Here we evaluate how well our model did.
# train_metrics = estimator.evaluate(input_fn=train_input_fn)
# eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
# print("train metrics: %r" % train_metrics)
# print("eval metrics: %r" % eval_metrics)


# import tensorflow as tf
#
# # 1.读取数据集，第一次TensorFlow会自动下载数据集到线面的路径中
# from tensorflow.examples.tutorials.mnist import input_data
#
# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
#
# # 2.数据集会自动被分成3个子集，train、validation和test。以下代码显示数据集的大小
# print("Training data size: ", mnist.train.num_examples)
# print("Validating data size: ", mnist.validation.num_examples)
# print("Testing data size: ", mnist.test.num_examples)
#
# # 3.查看training数据集中某个成员的像素矩阵生成的一维数组和其属于的数字标签
# print("Example traning data: ", mnist.train.images[0])
# # print("Example training data label: ",mnist.train.lables[0])
#
# # 4.使用mnist,train,next_batch来实现随机梯度下降
# batch_size = 100
# xs, ys = mnist.train.next_batch(batch_size)  # 从train的集合中选取batch_size个训练数据
# print("X shape:", xs.shape)
# print("Y shape:", ys.shape)


# # -*- coding:utf-8 -*-
# from PIL import Image
#
# IMG = 'E:\PycharmCode\\20180819213900.jpg'
#
# # IMG = 'D:\Download\\20180816102903.jpg'
#
# WIDTH = 800
# HEIGHT = 1067
#
# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#
#
# # 将256灰度映射到70个字符上
# def get_char(r, g, b, alpha=256):  # alpha透明度
#     if alpha == 0:
#         return ' '
#     length = len(ascii_char)
#     gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
#     unit = (256.0 + 1) / length
#     return ascii_char[int(gray / unit)]  # 不同的灰度对应着不同的字符
#     # 通过灰度来区分色块
#
#
# if __name__ == '__main__':
#     im = Image.open(IMG)
#     im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
#     txt = ""
#     for i in range(HEIGHT):
#         for j in range(WIDTH):
#             txt += get_char(*im.getpixel((j, i)))
#         txt += '\n'
#
#     print(txt)
#     # 写入文件
#     with open("outputquan.txt", 'w') as f:
#         f.write(txt)

# import numpy as np
#
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# b = np.reshape(a, [-1,4])
# c = a.reshape(2, -1)
# print('a=',a)
# print('b=',b)
# print('c=',c)

# import tensorflow as tf
# import numpy as np
#
# A = [[1, 3, 4, 5, 6]]
# B = [[1, 3, 4], [2, 4, 1]]
#
# with tf.Session() as sess:
#     print(sess.run(tf.argmax(A, 1)))
#     print(sess.run(tf.argmax(B, 1)))

import numpy as np
from tensorflow.contrib import learn
import tensorflow as tf

x_text = ['This is a cat','This must be boy', 'This is a a dog']
max_document_length = max([len(x.split(" ")) for x in x_text])

## Create the vocabularyprocessor object, setting the max lengh of the documents.
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
# VOCAB_PROCESSOR = tf.data(max_document_length)
# print(VOCAB_PROCESSOR)

## Transform the documents using the vocabulary.
x = np.array(list(vocab_processor.fit_transform(x_text)))

## Extract word:id mapping from the object.
vocab_dict = vocab_processor.vocabulary_._mapping

## Sort the vocabulary dictionary on the basis of values(id).
## Both statements perform same task.
#sorted_vocab = sorted(vocab_dict.items(), key=operator.itemgetter(1))
sorted_vocab = sorted(vocab_dict.items(), key = lambda x : x[1])

## Treat the id's as index into list and create a list of words in the ascending order of id's
## word with id i goes at index i of the list.
vocabulary = list(list(zip(*sorted_vocab))[0])

print(vocabulary)
print(x)