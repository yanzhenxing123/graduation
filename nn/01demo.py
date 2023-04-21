"""
@Author: yanzx
@Date: 2023/4/11 11:36
@Description: 使用tensorflow搭建一个简单的神经网络
"""
from loguru import logger

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data  # 数据集的获取

# 载入MINIST数据集,MINIST_data表示当前目录下的这个文件夹,也可以改为别的路径  read_data_sets时会默认把图像reshape（展开），若想保留图像的二维结构，可以传入reshape=False
mnist = input_data.read_data_sets("MNIST_data",
                                  one_hot=True)
# 定义模型
x = tf.placeholder(tf.float32, shape=[None, 784])
y = tf.placeholder(tf.float32, shape=[None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
logits = tf.matmul(x, W) + b
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits))

# 定义优化器和训练操作
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 创建 Saver 对象
saver = tf.train.Saver()

# 训练模型
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    # 保存模型
    logger.info("*" * 100)
    saver.save(sess, "./tmp/model.ckpt")
    logger.info("*" * 100)

