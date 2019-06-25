# Chapter 2: Representing and Manipulating Information

## Problem 2.1

Perform the following number conversions:

0x39A7F8

>1110011010011111111
>1100 1001 0111 1011

1100 1001 0111 1011

>C97B

0xD5E4C

>1101 0101 1110 0100 1100

1001 1011 1001 1110 1101 0101

>9B9ED5

---

## Problem 2.2

When a value x is a power of two, that is, x = 2n for some nonnegative integer
n, we can readily write x in hexadecimal form by remembering that the binary
representation of x is simply 1 followed by n zeros. The hexadecimal digit 0
represents four binary zeros. So, for n written in the form i + 4j , where 0 ≤ i ≤ 3,
we can write x with a leading hex digit of 1 (i = 0), 2 (i = 1), 4 (i = 2), or 8
(i = 3), followed by j hexadecimal 0s. As an example, for x = 2048 = 211, we have
n = 11 = 3 + 4 . 2, giving hexadecimal representation 0x800.

dec = 2^n

leading hex = 2^(n % 4)
subsequent 0s = floor(n/4)

Fill in the blank entries in the following table, giving the decimal and hexadecimal
representations of different powers of 2:

| n     | dec       | hex       |
| ---   | ---       | ---       |
| 9     | 512       | 0x200     |
| 19    | 524288    | 0x80000   |
| 15    | 16384     | 0x8000    |
| 16    | 32768     | 0x10000   |
| 17    | 65536     | 0x20000   |
| 5     | 32        | 0x20      |
| 7     | 128       | 0x80      |

---

## Problem 2.3

A single byte can be represented by two hexadecimal digits. Fill in the missing
entries in the following table, giving the decimal, binary, and hexadecimal values
of different byte patterns:

| Decimal           | Binary            | Hexadecimal       |
| ---               | ---               | ---               |
| 0                 | 0000 0000         | 0x00              |
| 167               | 1010 0111         | 0xA7              |
| 62                | 0011 1110         | 0x3E              |
| 188               | 1011 1100         | 0xBC              |
| 55                | 0011 0111         | 0x37              |
| 136               | 1000 1000         | 0x88              |
| 243               | 1111 0011         | 0xF3              |
| 82                | 0101 0010         | 0x52              |
| 172               | 1010 1100         | 0xAC              |
| 231               | 1110 0111         | 0xE7              |

---

## Problem 2.4

Without converting the numbers to decimal or binary, try to solve the following arithmetic problems, giving the answers in hexadecimal. Hint: Just modify
the methods you use for performing decimal addition and subtraction to use
base 16.

0x503c + 0x8
> 0x5045

0x503c - 0x40
> 0x4FFC

0x503c + 64
> 0x507c

0x50ea - 0x503c
> 0xAE

---

## Problem 2.5

```
#include <stdio.h>

typedef unsigned char *byte_pointer;

void show_bytes(byte_pointer start, int len) {
    int i;
    for (i = 0; i < len; i++)
	printf(" %.2x", start[i]);
    printf("\n");
}

void show_int(int x) {
    show_bytes((byte_pointer) &x, sizeof(int));
}

void show_float(float x) {
    show_bytes((byte_pointer) &x, sizeof(float));
}

void show_pointer(void *x) {
    show_bytes((byte_pointer) &x, sizeof(void *));
}
```

Consider the following three calls to show_bytes:
```
int val = 0x87654321;
byte_pointer valp = (byte_pointer) &val;
show_bytes(valp, 1); /* A. */
show_bytes(valp, 2); /* B. */
show_bytes(valp, 3); /* C. */
```

Indicate which of the following values will be printed by each call on a little-endian machine and on a big-endian machine:

Hex = 0x87654321  
Bin = 1000 0111 0110 0101 0100 0011 0010 0001

|       | Little-Endian     | Big-Endian        |
| ---   | ---               | ---               |
| A     | 21                | 87                |
| B     | 21 43             | 87 65             |
| C     | 21 43 65          | 87 65 43          |

---

## Problem 2.6

Using `show_int` and `show_float`, we determine that the integer 3510593 has hexadecimal representation 0x00359141, while the floating-point number 3510593.0
has hexadecimal representation 0x4A564504.

A. Write the binary representations of these two hexadecimal values.  
B. Shift these two strings relative to one another to maximize the number of
matching bits. How many bits match?  
C. What parts of the strings do not match?

### A

0x00359141  
> 0000 0000 0011 0101 1001 0001 0100 0001

0x4A564504  
> 0100 1010 0101 0110 0100 0101 0000 0100

### B

<pre>
0x00359141
0000 0000 0011 0101 1001 0001 0100 0001
0x4A564504
0100 1010 0101 0110 0100 0101 0000 0100

0x4A564504 with 2 bits shifted to the right
0001 0010 1001 0101 1001 0001 0100 0001

0x00359141 diff 0x4A564504 with 2 bits shifted to the right
0000 0000 0011 0101 1001 0001 0100 0001
             **************************
0001 0010 1001 0101 1001 0001 0100 0001
</pre>
21 matching bits.

### C

0001 0010 1001 0101 1001 0001 0100 0001
= 12 959141

We find all bits of the integer embedded in the floating-point number, except
for the most significant bit having value 1. Such is the case for the example
in the text as well. In addition, the floating-point number has some nonzero
high-order bits that do not match those of the integer.

---

## Problem 2.7

What would be printed as a result of the following call to show_bytes?

```
const char *s = "abcdef";
show_bytes((byte_pointer) s, strlen(s));
```

Note that letters ‘a’ through ‘z’ have ASCII codes 0x61 through 0x7A

61 62 63 64 65 66

---

## Problem 2.8

Fill in the following table showing the results of evaluating Boolean operations on
bit vectors.

| Operation     | Result        |
| ---           | ---           |
| a             | [01101001]    |
| b             | [01010101]    |
| ~a            | [10010110]    |
| ~b            | [10101010]    |
| a&b           | [01000001]    |
| a\|b          | [01111101]    |
| a^b           | [00111100]    |

---

## Problem 2.9

| R     | G     | B     | Color     |
| ---   | ---   | ---   | ---       |
| 0     | 0     | 0     | Black     |
| 0     | 0     | 1     | Blue      |
| 0     | 1     | 0     | Green     |
| 0     | 1     | 1     | Cyan      |
| 1     | 0     | 0     | Red       |
| 1     | 0     | 1     | Magenta   |
| 1     | 1     | 0     | Yellow    |
| 1     | 1     | 1     | White     |

A. The complement of a color is formed by turning off the lights that are on and
turning on the lights that are off. What would be the complement of each of
the eight colors listed above?

| Color     | RGB Complement |
| ---       | ---            |
| Black     | 111            |
| Blue      | 110            |
| Green     | 101            |
| Cyan      | 100            |
| Red       | 011            |
| Magenta   | 010            |
| Yellow    | 001            |
| White     | 000            |

B. Describe the effect of applying Boolean operations on the following colors:  
Blue | Green = 011, Cyan  
Yellow & Cyan = 010, Green  
Red ^ Magenta = 001, Blue

---

## Problem 2.10

```
void inplace_swap(int *x, int *y) {
    *y = *x ^ *y; /* Step 1 */
    *x = *x ^ *y; /* Step 2 */
    *y = *x ^ *y; /* Step 3 */
}
```

Starting with values a and b in the locations pointed to by x and y, respectively,
fill in the table that follows, giving the values stored at the two locations after each
step of the procedure. Use the properties of ^ to show that the desired effect is
achieved. Recall that every element is its own additive inverse (that is, a ^ a = 0).

| Step      | *x            | *y                 | Notes                |
| ---       | ---           | ---                | ---                  |
| Initially | a             |  b                 |                      |
| Step 1    | a             |  a^b               |                      |
| Step 2    | a ^ (a^b)     |  a^b               | a ^ (a^b) = b        |
| Step 3    | a ^ (a^b)     |  a ^ (a^b) ^ (a^b) |                      |

Example:

if a = 1001, b = 1000:

a, b

* Step 1
  * 1001, 1001 ^ 1000 = 0001

* Step 2
  * 1001 ^ 0001 = 1000, 0001

* Step 3
  * 1000, 0001 ^ 1000 = 1001

End result: a = 1000, b = 1001

---

## Problem 2.11



---