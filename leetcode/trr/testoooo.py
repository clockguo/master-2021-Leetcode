# import tensorflow as tf
# x = tf.Variable(0.0)
# x_plus = tf.assign_add(x, 1)
# with tf.control_dependencies([x_plus]):#只有当内部为操作时以来才会生效
#     y = tf.identity(x)#将该语句变为操作
# init = tf.global_variables_initializer()
# with tf.Session() as session:
#     init.run()
#     for i in range(8):
#         print(y.eval())
#     print(x.eval())#5

# import tensorflow as tf
# x = tf.Variable(0.0)
# x_plus = tf.assign_add(x, 1)
# with tf.control_dependencies([x_plus]):#只有当内部为操作时以来才会生效
#     #y = tf.identity(x)#将该语句变为操作
#     y = x
#     update = tf.group(y)#将该语句变为操作
#     print('lazha',x_plus)
# init = tf.global_variables_initializer()
# with tf.Session() as session:
#     init.run()
#     for i in range(5):
#         session.run(update)
#         print('what',y.eval())
#         print('lazha',session.run(y))##session.run()he eval()de yongfda
#     print(x.eval())#5

# import numpy as np
# a=np.ones((1000,1))
# b=np.ones((1,1000),dtype=np.float,order='C')
# C=a*b
# U=np.dot(a,b)
# P=np.dot(b,a)
# print(U)
# print(P ,'lazja ')
# print(C)
#
# d=np.random.random(5)
# print(d)
# a=np.random.randn(5,1)
# print(a,'\n',a.T)
# assert ( a==(5,1))



# import tensorflow as tf
# def get_weight(shape,lambda1):
#     var = tf.Variable(tf.random_normal(shape),dtype = tf.float32)
#     tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(lambda1 )(var))
#     return var
#
# x=tf.placeholder(tf.float32,shape=(None,2))
# y_ = tf.placeholder(tf.float32,shape=(None,1))
# batch_size=8
# layer_dimension=[2,10,10,10,1]
# n_layers = len(layer_dimension)
# print(n_layers)
# cur_layer = x
# in_dimension = layer_dimension[0]
# for i in range(1,n_layers):
#     out_dimension=layer_dimension[i]
#     weight=get_weight([in_dimension,out_dimension],0.001)
#     bias = tf.Variable(tf.constant(0.1,shape=[out_dimension]))
#     # tf.Print(bias)
#     print(bias)
#     # sess = tf.Session()
#     # print(sess.run(bias))
#     cur_layer=tf.nn.relu(tf.matmul(cur_layer,weight)+bias)
#     # tf.Print(cur_layer)
#     in_dimension = layer_dimension[i]
#
# mse_loss = tf.reduce_mean(tf.square(y_-cur_layer))
# tf.add_to_collection('losses',mse_loss)
# loss = tf.add_n(tf.get_collection('losses'))

# sess = tf.Session()#S大写
# sess = tf.InteractiveSession()
# sess.run(tf.Print(loss,[loss]))

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 1.设置输入和输出节点的个数,配置神经网络的参数
INPUT_NODE = 784  # 输入节点,即图片像素
OUTPUT_NODE = 10  # 输出节点，即类别数目。在MNIST数据集中需要区分的是0~9这10个数字，所以这里输出层节点数为10
LAYER1_NODE = 500  # 隐藏层数.使用只有一个隐藏层的网络结构，这个隐藏层有500个节点
BATCH_SIZE = 100  # 每次batch打包的样本个数。
# 一个训练batch中的训练数据个数。数字越小，训练过程越接近随机梯度下降；数字越大，训练越接近梯度下降。

# 模型相关的参数
LEARNING_RATE_BASE = 0.8  # 基础的学习率
LEARNING_RATE_DECAY = 0.99  # 学习率的衰减率
REGULARAZTION_RATE = 0.0001  # 描述模型复杂度的正则化项在损失函数中的系数
TRAINING_STEPS = 5000  # 训练轮数
MOVING_AVERAGE_DECAY = 0.99  # 滑动平均衰减率


# 2. 定义辅助函数来计算前向传播结果，使用ReLU做为激活函数。
def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    # 不使用滑动平均类
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        return tf.matmul(layer1, weights2) + biases2
    else:
        # 使用滑动平均类
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


# 3. 定义训练过程
def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')
    # 生成隐藏层的参数。
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
    # 生成输出层的参数。
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    # 计算不含滑动平均类的前向传播结果
    y = inference(x, None, weights1, biases1, weights2, biases2)

    # 定义训练轮数及相关的滑动平均类
    global_step = tf.Variable(0, trainable=False)  # 不需要计算滑动平均值，所以这里指定这个变量为不可训练的变量(trainable=False)
    #  给定训练轮数的变量可以加快训练早期变量的更新速度
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variables_averages_op = variable_averages.apply(tf.trainable_variables())  # 在所有代表神经网络参数的变量上使用滑动平均
    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)  # 计算使用了滑动平均之后的前向传播结果

    # 计算交叉熵及其平均值
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)  # 计算在当前batch中所有样例的交叉熵平均值

    # 损失函数的计算
    regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)  # L2正则化损失函数
    regularaztion = regularizer(weights1) + regularizer(weights2)  # 计算模型的正则化损失
    loss = cross_entropy_mean + regularaztion  # 总损失等于交叉熵损失和正则化损失的和

    # 设置指数衰减的学习率。
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,  # 基础的学习率
        global_step,  # 当前迭代的轮数
        mnist.train.num_examples / BATCH_SIZE,  # 过完所有的训练数据需要的迭代次数
        LEARNING_RATE_DECAY,  # 学习率衰减速度
        staircase=True)

    # 优化损失函数
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    # 反向传播更新参数和更新每一个参数的滑动平均值
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

    # 计算正确率
    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 初始化回话并开始训练过程。
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}  # 准备验证数据，来大致判断停止的条件和评判训练的效果
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}  # 准备测试数据。作为模型优劣的最后评价标准

        # 循环的训练神经网络。
        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:  # 每1000轮输出一次在验证数据集上的测试结果。
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)  # 计算滑动平均模型在验证数据上的结果
                print("After %d training step(s), validation accuracy using average model is %g " % (i, validate_acc))

            xs, ys = mnist.train.next_batch(BATCH_SIZE)  # 产生这一轮使用的一个batch的训练数据，并运行训练过程
            sess.run(train_op, feed_dict={x: xs, y_: ys})
        # 在训练结束之后，在测试数据上检测神经网络模型的最终正确率
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print(("After %d training step(s), test accuracy using average model is %g" % (TRAINING_STEPS, test_acc)))


# 4. 主程序入口，这里设定模型训练次数为(5000)30000次。
def main(argv=None):
    # mnist = input_data.read_data_sets("/tmp/MNIST_data", one_hot=True)
    mnist = input_data.read_data_sets("E:\PycharmCode\ProjectText\MNIST_data", one_hot=True)
    train(mnist)


if __name__ == '__main__':
    main()



