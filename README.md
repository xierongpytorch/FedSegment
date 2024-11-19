Journal Title: Pattern Recognition

Title of the **Manuscript**: *FedSegment: A Novel Federated Learning Framework for Semantic Segmentation of Secondary Screen Cabinet Terminal Block in Smart Substation* 

Authors: Rong Xie, Zhong Chen, Weiguo Cao, Congying Wu and Tiecheng Li

### Symbols and Notations Used in the Methodology[替换文本](https://www.baidu.com/)
| **Symbol**                                | **Description**                                                     |
|-------------------------------------------|---------------------------------------------------------------------|
| $F$                                 | Input feature map extracted by the encoder.                         |
| $F'$                                  | Feature map after channel attention: $ F' = M_c(F) \otimes F $.   |
| $ F''$                                | Feature map after spatial attention: $ F'' = M_s(F') \otimes F' $.|
| $ M_c(F) $                              | Channel attention map generated from $ F $.                       |
| $ M_s(F) $                              | Spatial attention map generated from $ F $.                       |
| $ \sigma(\cdot) $                       | Sigmoid activation function.                                        |
| $ \operatorname{MLP}(\cdot) $           | Multi-Layer Perceptron in channel attention.                        |
| $ \operatorname{MaxPool}(F) $           | Global max pooling applied to $ F $.                              |
| $ \operatorname{AvgPool}(F) $           | Global average pooling applied to $ F $.                          |
| $ f^{7 \times 7}(\cdot) $               | $ 7 \times 7 $ convolution operation in spatial attention.        |
| $ [\cdot \, ; \, \cdot] $               | Concatenation operator along the channel dimension.                 |
| $ \otimes $                             | Element-wise multiplication operator.                               |
| $ l $                                           | Security parameter determining key sizes.                           |
| $ p $                                           | Large prime number, $ p > 2^l $, order of the groups.             |
| $ G_1 $                                         | Cyclic additive group of order $ p $.                             |
| $ G_2 $                                         | Cyclic multiplicative group of order $ p $.                       |
| $ e(\cdot, \cdot) $                             | Bilinear pairing function, $ e: G_1 \times G_1 \rightarrow G_2 $. |
| $ P $                                           | Generator of the group $ G_1 $.                                   |
| $ H_1(\cdot) $                                  | Hash function, $ H_1: \{0,1\}^* \rightarrow G_1 $.                |
| $ H_2(\cdot) $                                  | Hash function, $ H_2: \{0,1\}^* \times G_1 \rightarrow \mathbb{Z}_p^* $. |
| $ H_3(\cdot) $                                  | Hash function, $ H_3: \{0,1\}^* \rightarrow \mathbb{Z}_p^* $.     |
| $ X_{\text{TTP}} $, $ Y_{\text{TTP}} $        | Private key and public key of the TTP.                              |
| $ X_{\text{CS}}' $, $ Y_{\text{CS}}' $        | Private and public key components of the Cloud Server (CS).         |
| $ X_{\text{PS}}' $, $ Y_{\text{PS}}' $        | Private and public key components of the Power Station (PS).        |
| $ X_s' $, $ Y_s' $                            | Private and public key components of substation $ s $.            |
| $ ID_{\text{CS}} $, $ ID_{\text{PS}} $, $ ID_s $ | Identity strings of CS, PS, and substation $ s $.           |
| $ s_{cp} $, $ s_{ip} $                        | Shared secrets for secure communication.                            |
| $ M $, $ M_1 $, $ M_2 $                     | Training parameters; $ M_1 $ for substations, $ M_2 $ for PS.   |
| $ T_s $, $ T_i $                              | Timestamps or session identifiers.                                  |
| $ r $, $ v $                                  | Random parameters used in signature generation.                     |
| $ D_s $, $ D_i $                              | Hash values used for signature verification.                        |
| $ k_s $, $ k_i $                              | Signature components computed by participants.                      |
| $ U_s $, $ U_i $                              | Signature components involving private keys and hash functions.     |
| $ \sigma_s $, $ \sigma_i $                    | Signatures composed of signature components.                        |
| $ Z_s $, $ Z_i $                              | Session parameters in signature generation.                         |
| $ Z_s' $, $ Z_i' $                            | Encrypted session parameters sent to PS and CS.                     |
| $ \operatorname{Enc}_s(\cdot) $, $ \operatorname{Enc}_i(\cdot) $ | Encryption functions. |
| $ \operatorname{Dec}_s(\cdot) $, $ \operatorname{Dec}_i(\cdot) $ | Decryption functions. |
| $ req_s $, $ req_i $                          | Update request messages sent by participants.                       |
| $ R $                                           | Set of requests used in batch verification.                         |
| $ N $, $ M $                                  | Number of substations $ N $ and power stations $ M $ involved.  |
| $ I_0 $, $ I_0' $                             | Original image dataset and preprocessed image dataset.              |
| $ I(x, y) $                                     | Pixel value at position $ (x, y) $ in image $ I $.              |
| $ I'(x, y) $                                    | Pixel value after transformations.                                  |
| $ R(I(x, y), \theta) $                          | Rotation of pixel $ I(x, y) $ by angle $ \theta $.              |
| $ Z(I(x, y), s) $                               | Zoom operation on pixel $ I(x, y) $ with scale $ s $.           |
| $ C(I(x, y), \alpha) $                          | Contrast adjustment of pixel $ I(x, y) $ by factor $ \alpha $.  |
| $ D(I(x, y), \delta) $                          | Distortion applied to pixel $ I(x, y) $ with magnitude $ \delta $. |
| $ p_{\text{rot}} $, $ p_{\text{zoom}} $       | Probabilities of rotation and zoom transformations.                 |
| $ p_{\text{con}} $, $ p_{\text{dist}} $       | Probabilities of contrast adjustment and distortion.                |
| $ \epsilon $                                     | Gaussian noise sampled from $ \mathcal{N}(0, I) $.                |
| $ \overline{a}_t $                              | Cumulative product of noise schedule parameters up to time $ t $. |
| $ I_t' $                                        | Noisy image at timestep $ t $ in the diffusion process.           |
| $ \epsilon_\theta(I_t', t) $                    | Predicted noise by the neural network at time $ t $.              |
| $ \hat{I}_0' $                                  | Estimated original image from noisy image $ I_t' $.               |
| $ D_{\text{CLIP}} $                             | CLIP-based loss function measuring image-text discrepancy.          |
| $ \text{CLIP}_{\text{img}}(\cdot) $             | Image encoder of the CLIP model.                                    |
| $ \text{CLIP}_{\text{txt}}(\cdot) $             | Text encoder of the CLIP model.                                     |
| $ d $                                           | Text description or prompt for image generation.                    |
| $ m $                                           | Mask indicating the region of interest in the image.                |
| $ D_c $                                         | Cosine distance function for embeddings.                            |
| $ \odot $                                       | Element-wise multiplication (Hadamard product).                     |
| $ I_{t-1,\text{fg}}' $, $ I_{t-1,\text{bg}}' $ | Denoised images of foreground and background at time $ t-1 $.   |
| $ I_{t-1}' $                                    | Combined denoised image at time $ t-1 $.                          |
| $ \text{fea}_0 $, $ \text{fea}_1 $            | Feature maps from local (student) and global (teacher) models.      |
| $ \text{Sim} $                                  | Adjusted feature similarity matrix.                                 |
| $ \text{FFT}(\cdot) $, $ \text{IFFT}(\cdot) $ | Fourier Transform and Inverse Fourier Transform.                    |
| $ \alpha $                                      | Coefficient adjusting frequency domain response.                    |
| $ L_{\text{pair}} $                             | Feature similarity loss between local and global models.            |
| $ \text{KL}(\cdot, \cdot) $                     | Kullback-Leibler divergence function.                               |
| $ \text{Softmax}(\cdot) $                       | Softmax function for normalization.                                 |
| $ S_{\text{sim}} $, $ T_{\text{sim}} $        | Similarity matrices from student and teacher models.                |
| $ T $                                           | Temperature parameter in the softmax function.                      |
| $ B $                                           | Batch size in training.                                             |
| $ L_{\text{CE}} $                               | Cross-entropy loss for the segmentation task.                       |
| $ L_{\text{total}} $                            | Total loss including $ L_{\text{CE}} $ and $ L_{\text{pair}} $. |
| $ \beta $                                       | Hyperparameter controlling the weight of $ L_{\text{pair}} $.     |
| $ \log(\cdot) $                                 | Natural logarithm function.                                         |



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



