import tensorflow as tf 


print ("tensorflow version: ", tf._version_)
import tensorflow_datasets as tensorflow_datasets
 
 datos, metadatos = tfds.load(
    'fashion_mnist', 
    as_superdvised=True, 
    with_info=True
    )