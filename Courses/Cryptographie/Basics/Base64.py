"""
import meaning we take away something like a library with function inside herself
so here base64 is used for different things
we used to use base 64 because sometimes, system need to have data into 7 bits, however, most of the time, data are into 8 bits so it's not usable

but how base 64 works?
As we said previously we want to convert data which is made with 8 bits. So we will use spend less bits for the same data using more data but with less bits.
So here it's an example

We have the text ABC
In ASCII code ABC correspond to [65,66,67]
So in binary it's [0010 0001, 0010 0010, 0010 0011] and the whole data is  001000010010001000100011
Let's do the next operation, we will convert the data in packets of 24 bits so 3 bytes and we will create packets of 6 bits
So or data 001000010010001000100011 will become 001000 010010 001000 100011
Our file or whatever you want will take this data and when we have to see the original file the invert will operate
"""

import base64
print(base64.b64decode('V2VsbCBwbGF5ZWQ='))