# Day 01 - Python Practice

## 📌 Topics Covered

* while loop
* for loop
* prime number logic

---

## 🔁 Loop Code

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

---

## 🔢 Prime Number Code

```python
num = int(input("Enter a number: "))
i = 2

while i < num:
    if num % i == 0:
        print(num, "is not a prime number")
        break
    i += 1
else:
    print(num, "is a prime number")
```

---

## 🧠 What I Learned

* How loops work
* Prime number logic
* while-else concept

---

## ❗ Mistakes

* Used wrong starting value of `i`
* Forgot increment (`i += 1`)
