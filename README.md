心得体会:
1. 按照作业要求先在本地创建训练所需要的文件，修改代码和配置文件，然后通过不同的方式去执行训练、验证、输出。最后在tinymind上进行调试，更新参数和文件夹结构。在进行了这些操作之后对object_detection还是不了解，只知道如何利用当前的环境训练数据并输出结果。下面需要自己动手实现整个流程。

2. Tinymind的数据集功能有点坑啊，自己创建的数据集老是引用不成功，而且更新数据源的时候总是提示我数据集无法识别...最后把数据文件统一上传到github才把模型跑通...



Codes are based on TensorFlow Models:
# TensorFlow Models

This repository contains a number of different models implemented in [TensorFlow](https://www.tensorflow.org):

The [official models](official) are a collection of example models that use TensorFlow's high-level APIs. They are intended to be well-maintained, tested, and kept up to date with the latest stable TensorFlow API. They should also be reasonably optimized for fast performance while still being easy to read. We especially recommend newer TensorFlow users to start here.

The [research models](research) are a large collection of models implemented in TensorFlow by researchers. It is up to the individual researchers to maintain the models and/or provide support on issues and pull requests.

The [samples folder](samples) contains code snippets and smaller models that demonstrate features of TensorFlow, including code presented in various blog posts.

The [tutorials folder](tutorials) is a collection of models described in the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).
