A matrix-encoding implementation for an arbitrary stucture neural network.

Lets take the following network.

```
|   |   |
N1  N2  N3
|   |   |
N4  |   |
 \  |  /|
  \ | / |
    N5 /|
    | / |
    N6  N7
```

The process of getting the outputs is:
1. **Base representation**
2. **Layerization** (splitting it up into sepratate layers)
   1. Get output layer (output nodes are pre-defined)
   2. Build out-1 layer, by looking at nodes needed for the output layer
   3. Build out-2 layer, by looking at nodes needed for out-1 layer
   4. ...
3. 