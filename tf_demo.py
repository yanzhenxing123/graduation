"""
@Author: yanzx
@Date: 2023/1/29 18:09
@Description: Study for tf_v1
"""

import tensorflow as tf

# 1. assign

"""
tf.assign(ref, value, validate_shape=None, use_locking=None, name=None)
"""

import tensorflow as tf

# 必须是variable
A = tf.Variable([1, 2, 3])

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(A))  ## [1，2，3]
    sess.run(tf.assign(A, [1, 2, 5]))
    print(sess.run(A))

# 2. constant
"""
tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const',
    verify_shape=False
)


value: 要创建的常量(可以为字符、数字矩阵等)
dtype: 常量的类型（tf.float16/32/64 tf.int8/16/32/64）
shape: 生成常量的形状（如矩阵）
name: 为常量命名


tf. Variable（）

Variable()需要初始值，一旦初始值确定，那么该变量的类型和形状都确定了。
更改值通过assign方法。
想要改变形状，需要使用assign+validate_shape=False。

参数：

initial_value：默认为None，可以搭配tensorflow随机生成函数，如上例。

trainable：默认为True，可以后期被算法优化的。如果不想该变量被优化，改为False。

validate_shape：默认为True，形状不接受更改，如果需要更改，validate_shape=False。

name：默认为None，给变量确定名称。
"""
# 3. Variable

print("\nVariable:")

v1 = tf.Variable(tf.random_normal(shape=[4, 3], mean=0, stddev=1), name='v1')
v2 = tf.Variable(tf.constant([1, 2]), name='v2')
v3 = tf.Variable(tf.ones([4, 3]), name='v3')
with tf.Session() as sess:
    # 需要先初始化变量，而常量不用初始化 注意：只要使用tf.Variable()语法，必须先初始化变量
    sess.run(tf.global_variables_initializer())
    print(sess.run(v1))
    print(sess.run(v2))
    print(sess.run(v3))

# 4. placehoder


input1 = tf.placeholder(tf.float32)  # 需要定义placeholder的数据类型，一般为float32
input2 = tf.placeholder(tf.float32)

# 定义output步骤

output = tf.multiply(input1, input2)  # 乘法

# 执行

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [5.3], input2: [2.0]}))
