This single-node setup basically solves for a line: Y = m*x + b

In more professional terms, it solves linearly separable problems.
That means problems, where the "solution space" can be separated by a single line (or a plane, if we are in 3D).

Linearly separabel problems are, for example, the AND and OR gates.

|AND  |T|F|
|-    |-|-|
|**T**|T|F|
|**F**|F|F|

|OR   |T|F|
|-    |-|-|
|**T**|T|T|
|**F**|T|F|

A line can be drawn, that separates the T\F values in the solution, in both cases.

However the same can't be done for the XOR gate.

|XOR  |T|F|
|-    |-|-|
|**T**|F|T|
|**F**|T|F|

This is why we need multi-layer nodes.