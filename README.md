Journal Title: Pattern Recognition

Title of the **Manuscript**: *FedSegment: A Novel Federated Learning Framework for Semantic Segmentation of Secondary Screen Cabinet Terminal Block in Smart Substation* 

Authors: Rong Xie, Zhong Chen, Weiguo Cao, Congying Wu and Tiecheng Li

### Ideal Model:
![image text](https://github.com/xierongpytorch/FedSegment/blob/main/PICTURE/ideal%20model.png "DBSCAN Performance Comparison")

### Federated Model:
![image text](https://github.com/xierongpytorch/FedSegment/blob/main/PICTURE/federated%20model.png "DBSCAN Performance Comparison")

### FedSegment:
![image text](https://github.com/xierongpytorch/FedSegment/blob/main/PICTURE/system%20model.png "DBSCAN Performance Comparison")

### Semantic Segmentation:
![image text](https://github.com/xierongpytorch/FedSegment/blob/main/PICTURE/segmentation%20model.png "DBSCAN Performance Comparison")

### Anonymous Protocol:
![image text](https://github.com/xierongpytorch/FedSegment/blob/main/PICTURE/anonymous%20protocol.png "DBSCAN Performance Comparison")

### Data Augmentation:
![image text](https://github.com/xierongpytorch/FedSegment/blob/main/PICTURE/data%20augmentation.png "DBSCAN Performance Comparison")

| **Symbol**                                | **Description**                                                     |
|-------------------------------------------|---------------------------------------------------------------------|
| \\( F \\)                                   | Input feature map extracted by the encoder.                         |
| \\( F' \\)                                  | Feature map after channel attention: \\( F' = M_c(F) \otimes F \\).   |
| \\( F'' \\)                                 | Feature map after spatial attention: \\( F'' = M_s(F') \otimes F' \\).|
| \\( M_c(F) \\)                              | Channel attention map generated from \\( F \\).                       |
| \\( M_s(F) \\)                              | Spatial attention map generated from \\( F \\).                       |
| \\( \sigma(\cdot) \\)                       | Sigmoid activation function.                                        |
| \\( \operatorname{MLP}(\cdot) \\)           | Multi-Layer Perceptron in channel attention.                        |
| \\( \operatorname{MaxPool}(F) \\)           | Global max pooling applied to \\( F \\).                              |
| \\( \operatorname{AvgPool}(F) \\)           | Global average pooling applied to \\( F \\).                          |
| \\( f^{7 \times 7}(\cdot) \\)               | \\( 7 \times 7 \\) convolution operation in spatial attention.        |
| \\( [\cdot \, ; \, \cdot] \\)               | Concatenation operator along the channel dimension.                 |
| \\( \otimes \\)                             | Element-wise multiplication operator.                               |
