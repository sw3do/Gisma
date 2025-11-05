# Time and space complexity analysis 

## OUTLINE
- What is algorithm analysis
- why algoritm analysis
- Types of complexities
-- Time Complexity of Algoritms
-- Space Complexity of Algoritms
- Summary
- Examples

````
Why do we need algoirthm analysis?

There are multiple approaches to solve one problems algorithm analysis is performed to gigure out which is the optimum approaches
```



# Sum of numbers (0-N)

Example

1. Get the value of N --> 1m-sec

2. SUM = (N*(N+1)) / 2 ---> 2m-sec

3. Print SUM ---> 1m-sec


## The formule T = 1 + 2 + 1 = 4

```
   Time
    |
    |
    |    
    |----------------
    |
    |
    |
    |-----------------------

      Space
```


1. Get the value of N ----> 1m-sec
2. Initlaze SUM to 0 ----> 1m-sec
3. for(i=0 to N) ----> 1m-sec
  1. SUM = SUM + 1 ----> n m-sec
4. Print SUM ----> 1m-sec

T = 1 + 1 + 1 + n + 1 = n + 4


              ^.     ^ 
Size of Input | Time |


```
   
  |                /
  |.             /
  |            / 
  |.         / 
  |.       /
  |.     /
  |.   / 
  |. / 
  |/
  |--------------------------

```

``` # Finding the avarage of n numbers

1. Get the value of N ---> 1m-sec
2. Initilaze SUM to 0 ----> 1m-sec
3. Till N > 0 ----> 1m-sec

```

Asymptotic Algorithms Analysis(Time complexity)


Big O notaion
Omega notation
-----

Big O Notation


Constant time: O(1)
Linear time: O(n)
Logaritmich: O(log n)
Quadratic: O(n2)
Cubic: O(n3)
-------

Example find the best, worst and avarage

Find 5 ----> 1 iteration --> best case omega(1)

Find value 100 ---> n iteration --> worst case: O(n)

avarage case tetra(n)










































## ✅ **Time Complexity (Zaman Karmaşıklığı)**

Bir algoritmanın **çalışma süresinin**, giriş verisinin boyutuna (**n**) göre nasıl değiştiğini gösterir.

➡️ Yani **n büyüdükçe** algoritma **ne kadar yavaşlar?**

Zaman karmaşıklığı genelde **Big-O Notasyonu** ile ifade edilir:

| Big-O          | Adı                 | Örnek                                      |
| -------------- | ------------------- | ------------------------------------------ |
| **O(1)**       | Sabit zaman         | Diziye index ile erişim                    |
| **O(log n)**   | Logaritmik          | Binary Search                              |
| **O(n)**       | Doğrusal            | Tek döngü                                  |
| **O(n log n)** | Logaritmik çarpımlı | Efficient sortlar (Merge Sort, Quick Sort) |
| **O(n²)**      | Karesel             | İç içe 2 döngü (Bubble Sort)               |
| **O(2ⁿ)**      | Üstel               | N-queens brute force                       |
| **O(n!)**      | Faktöriyel          | Tüm permütasyonları deneme                 |

📌 Big-O **kötü senaryoyu** gösterir (genellikle worst case analiz edilir).

---

### 🔹 Döngü Örnekleri

```python
# O(n)
for i in range(n):
    print(i)
```

```python
# O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j)
```

```python
# O(log n)
while n > 1:
    n = n // 2
```

```python
# O(n log n)
for i in range(n):
    n2 = n
    while n2 > 1:
        n2 //= 2
```

---

## ✅ **Space Complexity (Alan Karmaşıklığı)**

Algoritmanın çalışması için **ne kadar bellek kullanıyor?**

Yine **giriş boyutuna göre** hesaplanır.

| Big-O     | Ne demek?                        |
| --------- | -------------------------------- |
| **O(1)**  | Ekstra bellek yok / sabit        |
| **O(n)**  | Dizi/list işlemlerinde ek bellek |
| **O(n²)** | Matris kullanan algoritmalar     |

---

### Alan Karmaşıklığı Örneği

```python
# O(1) - sabit alan
x = 10
y = 20
```

```python
# O(n) - n elemanlı liste
arr = [0] * n
```

---

## 🔥 Özet Görsel Mantık

| Complexity      | Performans  | Örnek             |
| --------------- | ----------- | ----------------- |
| ✅ O(1)          | En iyi      | Hash table lookup |
| ✅ O(log n)      | Çok iyi     | Binary Search     |
| ⚠️ O(n)         | İyi         | Tek döngü         |
| ❌ O(n²)         | Kötüleşiyor | Nested loops      |
| 💀 O(2ⁿ), O(n!) | Çok kötü    | Backtracking      |





# What is space complexity

- Definition: the amount of memory space required to solve an instance of the computational problem as a function of the size of the input

- Simple words: It is the memory reqyired by an algoritm to execuute a program and produce output

- similar to time complexlity, space complexity is often expres ...


# For any algoirtm, memory is reqyired for the following purposes

- to store program insturctions
- to sotre constant values
- to store varible values
- and for few other things like functions calls, jumping, statements etc.

- Auxiliary space: is the temporary space (excluding the input size) allocated by your algorithm to solve the problem, with respect to input size

- Space complexity includes both ....


-----


Example

Space complexity = Input size + auxiliary space


n1 --> 4 bytes
n2 ---> 4 bytes
------

