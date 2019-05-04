# Red Black Tree with Order Statistic
Using Introduction to Algorithm (CLRS 2nd Edition) Pseudocode to create a Red Black Tree with Order Statistic Feature

# Goal of code
Write a program that supports the following operations on order- statistic trees. An order-statistic tree is a red-black tree with size information stored in each node. We maintain a dynamic set of integers in an order-statistic tree. Assume that integers are in the range of [1::9999] and initially tree T is empty.

* OS-Insert(T; x) returns x if integer x is not already in order-statistic tree T (i.e., x is inserted); 0 otherwise.
* OS-Delete(T; x) returns x if integer x is in T (i.e., x is deleted); 0 otherwise.
* OS-Select(T; i) returns the i-th smallest integer in T if the number of integers in T is >= i; 0 otherwise.
* OS-Rank(T; x) returns the rank of x among the integers in T if x is in T; 0 otherwise.

An input file contains a sequence of operations. In the input file OS-Insert(T; 17) is denoted by I 17, OS-Delete(T; 8) by D 8, OS-Select(T; 5) by S 5, and OS-Rank(T; 9) by R 9. Put a space between two operations.