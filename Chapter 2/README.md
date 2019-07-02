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

Armed with the function inplace_swap from Problem 2.10, you decide to write
code that will reverse the elements of an array by swapping elements from opposite
ends of the array, working toward the middle.  
You arrive at the following function:

``` C
void reverse_array(int a[], int cnt) {
    int first, last;
    for (first = 0, last = cnt-1;
        first <= last;
        first++,last--)
        inplace_swap(&a[first], &a[last]);
}
```

When you apply your function to an array containing elements 1, 2, 3, and 4, you
find the array now has, as expected, elements 4, 3, 2, and 1. When you try it on
an array with elements 1, 2, 3, 4, and 5, however, you are surprised to see that
the array now has elements 5, 4, 0, 2, and 1. In fact, you discover that the code
always works correctly on arrays of even length, but it sets the middle element to
0 whenever the array has odd length.

A. For an array of odd length cnt = 2k + 1, what are the values of variables  
first and last in the final iteration of function reverse_array?
B. Why does this call to function xor_swap set the array element to 0?  
C. What simple modification to the code for reverse_array would eliminate
this problem?

A
* Context: first, last
* First iteration: 0, 2k
* Last iteration: k+1, k-1

B  
Because swapping a variable by itself would reduce itself to 0, and the subsequent steps would read from the same variable and therefore 0^0 = 0. (a^a = 0)

Example:

if a = 1001, b = &a:

a, b

* Step 1
  * 1001, 1001 ^ 1001 = 0000
    * However, since b -> a, a = b.
    * 0000, 0000

* Step 2
  * 0000 ^ 0000 = 0000, 0000

* Step 3
  * 0000, 0000 ^ 0000 = 0000

```
int test = 5;
int *test2 = &test;
int test3 = 5;

*test2 = test ^ *test2;

printf("%d, %d", test, *test2); // Same address, -> 0, 0.
printf("\n");

test = 5;
test3 = test ^ test3;

printf("%d, %d", test, test3); // Diff address, -> 5, 0.
printf("\n");
```

**Adjusting a pointer variable sets value to the address it's pointing to.**

C
``` C
for (first = 0, last = cnt-1;
    first < last;
    first++,last--)
```

---

## Problem 2.12

Write C expressions, in terms of variable x, for the following values. Your code
should work for any word size w ≥ 8. For reference, we show the result of evaluating the expressions for x = 0x87654321, with w = 32.

A. The least significant byte of x, with all other bits set to 0. [0x00000021].  
B. All but the least significant byte of x complemented, with the least significant
byte left unchanged. [0x789ABC21].  
C. The least significant byte set to all 1s, and all other bytes of x left unchanged.
[0x876543FF].

x = 1000 0111 0110 0101 0100 0011 0010 0001  
0xFF = 0000 0000 0000 0000 0000 0000 1111 1111  

A  
x & 0xFF = 0000 0000 0000 0000 0000 0000 0010 0001 = 0x00000021

B  
~x = 0111 1000 1001 1010 1011 1100 1101 1110  
~x ^ 0xFF = 0111 1000 1001 1010 1011 1100 0010 0001 = 0x789ABC21

C  
x | 0xFF = 1000 0111 0110 0101 0100 0011 1111 1111 = 0x876543FF

---

## Problem 2.13

https://www.nayuki.io/page/boolean-algebra-laws this link may prove useful...

The Digital Equipment VAX computer was a very popular machine from the late
1970s until the late 1980s. Rather than instructions for Boolean operations And
and Or, it had instructions bis (bit set) and bic (bit clear). Both instructions take
a data word x and a mask word m. They generate a result z consisting of the bits of
x modified according to the bits of m. With bis, the modification involves setting
z to 1 at each bit position where m is 1. With bic, the modification involves setting
z to 0 at each bit position where m is 1.

To see how these operations relate to the C bit-level operations, assume we
have functions bis and bic implementing the bit set and bit clear operations, and
that we want to use these to implement functions computing bit-wise operations
| and ^, without using any other C operations. Fill in the missing code below.  
**Hint: Write C expressions for the operations bis and bic.**

``` C
/* Declarations of functions implementing operations bis and bic */
int bis(int x, int m);
int bic(int x, int m);

/* Compute x|y using only calls to functions bis and bic */
int bool_or(int x, int y) {
    int result = ________;
    return result;
}

/* Compute x^y using only calls to functions bis and bic */
int bool_xor(int x, int y) {
    int result = ________;
    return result;
}
```

`bis(x, m)`
* If x = 0001, m = 1111
* z = x | m = 1111
* return z

`bic(x, m)`
* If x = 0001, m = 1111
* z = x & ~m = 0000
* return z

`bool_or(x, y)`
* If x = 0001, y = 1000
* x|y = 1001
* result = bis(x, y) = 1001

`bool_xor(x, y)`
* If x = 0101, y = 1011
* x^y = 1110
* bis(x, y) = 1111
* bic(x, y) = 0100
* bic(y, x) = 1010
* result = bis(bic(x, y), bic(y, x)) = 1110

---

## Problem 2.14

Suppose that x and y have byte values 0x66 and 0x39, respectively. Fill in the
following table indicating the byte values of the different C expressions:

| Expression | Value | Expression | Value |
| ---        | ---   | ---        | ---   |
| x & y      | 0x20  | x && y     | 0x01  |
| x \| y      | 0x7F  | x \|\| y     | 0x01  |
| ~x \| ~y    | 0xDF  | !x \|\| !y   | 0x00  |
| x & !y     | 0x00  | x && ~y    | 0x01  |

x = 0110 0110  
y = 0011 1001  

x & y = 0010 0000  
x && y = 0001  
x | y = 0111 1111  
x || y = 0001  
~x | ~y = 1101 1111  
!x || !y = 0000  
x & !y = 0000  
x && ~y = 0001  

---

## Problem 2.15

Using only bit-level and logical operations, write a C expression that is equivalent 
to x == y. In other words, it will return 1 when x and y are equal, and 0 otherwise.

> (x ^ y) && 0x01

---

## Problem 2.16

Fill in the table below showing the effects of the different shift operations on singlebyte quantities. The best way to think about shift operations is to work with binary
representations. Convert the initial values to binary, perform the shifts, and then
convert back to hexadecimal. Each of the answers should be 8 binary digits or 2
hexadecimal digits.

| x      |        | x << 3 |        | x >> 2 | (Logical) | x >> 2 | (Arithmetic) |
| ---    | ---    | ---    | ---    | ---    | ---       | ---    | ---          |
| Hex    | Binary | Hex    | Binary | Hex    | Binary    | Hex    | Binary       |
| 0xC3   | ______ | ______ | ______ | ______ | ______    | ______ | ______       |
| 0x75   | ______ | ______ | ______ | ______ | ______    | ______ | ______       |
| 0x87   | ______ | ______ | ______ | ______ | ______    | ______ | ______       |
| 0x66   | ______ | ______ | ______ | ______ | ______    | ______ | ______       |

x  
0xC3 = 1100 0011  
0x75 = 0111 0101  
0x87 = 1000 0111  
0x66 = 0110 0110  

x << 3  
0xC3 << 3 = 0001 1000 = 0x18  
0x75 << 3 = 1010 1000 = 0xA8  
0x87 << 3 = 0011 1000 = 0x38  
0x66 << 3 = 0011 0000 = 0x30  

x >> 2 (Logical)  
0xC3 >> 2 = 0011 0000 = 0x30  
0x75 >> 2 = 0001 1101 = 0x1D  
0x87 >> 2 = 0010 0001 = 0x21  
0x66 >> 2 = 0001 1001 = 0x19  

x >> 2 (Arithmetic)  
0xC3 >> 2 = 1111 0000 = 0xF0  
0x75 >> 2 = 0001 1101 = 0x1D  
0x87 >> 2 = 1110 0001 = 0xE1  
0x66 >> 2 = 0001 1001 = 0x19  

---

## Problem 2.17

Assuming w = 4, we can assign a numeric value to each possible hexadecimal
digit, assuming either an unsigned or a two’s-complement interpretation. Fill in
the following table according to these interpretations by writing out the nonzero
powers of two in the summations shown in Equations 2.1 and 2.3:

| $\vec{x}$ |        |                            |                             |
| ---       | ---    | ---                        | ---                         |
| Hex       | Binary | B2U$_4(\vec{x})$           | B2T$_4(\vec{x})$            |
| 0xE       | [1110] | $2^3$ + $2^2$ + $2^1$ = 14 | $-2^3$ + $2^2$ + $2^1$ = -2 |
| 0x0       | ______ | ______                     | ______                      |
| 0x5       | ______ | ______                     | ______                      |
| 0x8       | ______ | ______                     | ______                      |
| 0xD       | ______ | ______                     | ______                      |
| 0xF       | ______ | ______                     | ______                      |

0x0 = 0000  
B2U$_4(\vec{x})$ = 0  
B2T$_4(\vec{x})$ = 0  

0x5 = 0101  
B2U$_4(\vec{x})$ = $2^2$ + $2^0$ = 5  
B2T$_4(\vec{x})$ = $2^2$ + $2^0$ = 5  

0x8 = 1000  
B2U$_4(\vec{x})$ = $2^3$ = 8  
B2T$_4(\vec{x})$ = $-2^3$ = -8  

0xD = 1101  
B2U$_4(\vec{x})$ = $2^3$ + $2^2$ + $2^0$ = 13  
B2T$_4(\vec{x})$ = $-2^3$ + $2^2$ + $2^0$ = -3  

0xF = 1111  
B2U$_4(\vec{x})$ = $2^3$ + $2^2$ + $2^1$ + $2^0$ = 15  
B2T$_4(\vec{x})$ = $-2^3$ + $2^2$ + $2^1$ + $2^0$ = -1  

---

## Problem 2.18

In Chapter 3, we will look at listings generated by a disassembler, a program that
converts an executable program file back to a more readable ASCII form. These
files contain many hexadecimal numbers, typically representing values in two’s complement form. Being able to recognize these numbers and understand their significance (for example, whether they are negative or positive) is an important skill.

For the lines labeled A–J (on the right) in the following listing, convert the
hexadecimal values (in 32-bit two’s-complement form) shown to the right of the
instruction names (sub, mov, and add) into their decimal equivalents:

|          |                    |     |                         |       |
| ---      | ---                | --- | ---                     | ---   |
| 8048337: | 81 ec b8 01 00 00  | sub | $0x1b8,%esp             | A.    |
| 804833d: | 8b 55 08           | mov | 0x8(%ebp),%edx          |       |
| 8048340: | 83 c2 14           | add | $0x14,%edx              | B.    |
| 8048343: | 8b 85 58 fe ff ff  | mov | 0xfffffe58(%ebp),%eax   | C.    |
| 8048349: | 03 02              | add | (%edx),%eax             |       |
| 804834b: | 89 85 74 fe ff ff  | mov | %eax,0xfffffe74(%ebp)   | D.    |
| 8048351: | 8b 55 08           | mov | 0x8(%ebp),%edx          |       |
| 8048354: | 83 c2 44           | add | $0x44,%edx              | E.    |
| 8048357: | 8b 85 c8 fe ff ff  | mov | 0xfffffec8(%ebp),%eax   | F.    |
| 804835d: | 89 02              | mov | %eax,(%edx)             |       |
| 804835f: | 8b 45 10           | mov | 0x10(%ebp),%eax         | G.    |
| 8048362: | 03 45 0c           | add | 0xc(%ebp),%eax          | H.    |
| 8048365: | 89 85 ec fe ff ff  | mov | %eax,0xfffffeec(%ebp)   | I.    |
| 804836b: | 8b 45 08           | mov | 0x8(%ebp),%eax          |       |
| 804836e: | 83 c0 20           | add | $0x20,%eax              | J.    |
| 8048371: | 8b 00              | mov | (%eax),%eax             |       |

> A  
$0x1b8      = $16^2 + 11 * 16^1 + 8 = 440$  

> B  
$0x14       = $16^1 + 4 = 20$  

> C  
$0xfffffe58 = $15 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 5 * 16 + 8 = 4,294,966,872$  (Unsigned)  
$0xfffffe58 = $-2^{31} + 7 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 5 * 16 + 8 = -424$  (Signed)  

> D  
$0xfffffe74 = $15 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 7 * 16 + 4 = 4,294,966,900$  (Unsigned)  
$0xfffffe74 = $-2^{31} + 7 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 7 * 16 + 4 = -396$  (Signed)  

> E  
$0x44 = $4 * 16 + 4 = 68$

> F  
$0xfffffec8 = $15 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 12 * 16 + 8 = 4,294,966,984$  (Unsigned)  
$0xfffffec8 = $-2^{31} + 7 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 12 * 16 + 8 = -312$  (Signed)  

> G  
$0x10 = $1 * 16 = 16$  

> H  
$0xc = $12 = 12$  

> I  
$0xfffffeec = $15 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 14 * 16 + 12 = 4,294,967,020$  (Unsigned)  
$0xfffffeec = $-2^{31} + 7 * 16^7 + 15 * 16^6 + 15 * 16^5 + 15 * 16^4 + 15 * 16^3 + 14 * 16^2 + 14 * 16 + 12 = -276$  (Signed)  

> J  
$0x20 = $2 * 16 = 32$  

In this context, we only take the signed value if it exists, because in two's complement form, the sign bit is negative.

---

Problem 2.19

Using the table you filled in when solving Problem 2.17, fill in the following table
describing the function $T2U_4$:

| $x$      | $T2U_4(x)$         |
| ---      | ---                |
| -8       | ___________        |
| -3       | ___________        |
| -2       | ___________        |
| -1       | ___________        |
|  0       | ___________        |
|  5       | ___________        |

-8 = 1000 = 8  
-3 = 1101 = 13  
-2 = 1110 = 14  
-1 = 1111 = 15  
0 = 0000 = 0  
5 = 0101 = 5 

---

Problem 2.20

Explain how Equation 2.6 applies to the entries in the table you generated when
solving Problem 2.19.

> For the first four entries, the values of x are negative and $T2U_4(x) = x + 2^4$.

> For the remaining two entries, the values of x are nonnegative and $T2U_4(x) = x$.

---

Problem 2.21

Assuming the expressions are evaluated on a 32-bit machine that uses two’scomplement arithmetic, fill in the following table describing the effect of casting
and relational operations, in the style of Figure 2.18:

| Expression                    | Type          | Evaluation    |
| ---                           | ---           | ---           |
| -2147483647-1 == 2147483648U  | ___________   | ___________   |
| -2147483647-1  <  2147483647  | ___________   | ___________   |
| -2147483647-1U <  2147483647  | ___________   | ___________   |
| -2147483647-1  < -2147483647  | ___________   | ___________   |
| -2147483647-1U < -2147483647  | ___________   | ___________   |

-2147483647-1  == 2147483648U = Unsigned, 0x01  
-2147483647-1  <  2147483647 = Signed, 0x01  
-2147483647-1U <  2147483647 = Unsigned, 0x00  
-2147483647-1  < -2147483647 = Signed, 0x01  
-2147483647-1U < -2147483647 = Unsigned, 0x01  

T2U(-2147483647) = T2U(-2^31+1) = -2147483647 + 2^32 = 2147483649  
T2U(-2147483647-1) = T2U(-2^31) = 2147483648  
T2U(-2147483647-1U) = T2U(2147483649-1) = 2147483648  

---

Problem 2.22

AHHHHHHHHHHHHHHH

---