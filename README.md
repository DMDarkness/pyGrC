# pyGrC
A set of methods about granular computing which is realized by python 3
基于Python 3 实现的一系列粒计算方法
## methods
### fuzzy c-means (模糊c均值聚类)
The code is in fcm.py

[U, V] = fcmAO(data, c, m, threshold) 
* data: list of lists where every list is a point
* c: the number of clusters
* m: the parameter to control fuzziness
* threshold: the stop condition
* U: the membership of every point belonging to every center
* V: list of lists where every list is a center 

代码见fcm.py

[U, V] = fcmAO(data, c, m, threshold) 
* data: list的list，其中每个list是一个点
* c: 聚类个数
* m: 控制模糊程度的参数
* threshold: 迭代停止条件
* U: 每个点隶属于每个类别的隶属度矩阵
* V: list的list，其中每个list是一个类别中心
### k-means (k均值聚类)
The code is in kmeans.py

[U, V] = kmeans(data, k, threshold)
* data: list of lists where every list is a point
* k: the number of clusters
* threshold: the stop condition
* U: the membership of every point belonging to every center which is 0 or 1
* V: list of lists where every list is a center 

代码见kmeans.py

[U, V] = kmeans(data, k, threshold)
* data: list的list，其中每个list是一个点
* k: 聚类个数
* threshold: 迭代停止条件
* U: 每个点隶属于每个类别的隶属度矩阵，属于为1，不属于为0
* V: list的list，其中每个list是一个类别中心
### k-medians (k中位数聚类)
The code is in kmedian.py

[U, V] = kmedians(data, k, threshold)
* data: list of lists where every list is a point
* k: the number of clusters
* threshold: the stop condition
* U: the membership of every point belonging to every center which is 0 or 1
* V: list of lists where every list is a center 

代码见kmedian.py

[U, V] = kmedians(data, k, threshold)
* data: list的list，其中每个list是一个点
* k: 聚类个数
* threshold: 迭代停止条件
* U: 每个点隶属于每个类别的隶属度矩阵，属于为1，不属于为0
* V: list的list，其中每个list是一个类别中心
### rough set (粗糙集近似) 
The code is in rs.py

Roughset = rs(classes, Set)
* classes: list of sets or list of lists, where every sets or list is a class
* Set: the targer set which needs to be approximated
* Roughset: list of two sets, which are lower approximation and upper approximation

代码见rs.py


Roughset = rs(classes, Set)
* classes: set的list或list的list, 其中每个set或list是一个类
* Set: 需要被近似的集合 
* Roughset: 下近似与上近似组成的list
### decision theoretic rough set (决策粗糙集近似)
I am coding
正在开发中
### principle of justifiable granularity (合理粒度原则)
The code is in pojg.py

granule = pojgMedE(data, alpha)
* data: list of numbers which are used to form information granule
* alpha: the parameter to adjust the importance of specificity
* granule: the information granule which is [lower bound, median, upper bound]

代码见pojg.py

granule = pojgMedE(data, alpha)
* data: 需要被粒化的数字list
* alpha: 控制specificity的参数
* granule: 信息粒，形式为 [下界, 中位数, 上界]
