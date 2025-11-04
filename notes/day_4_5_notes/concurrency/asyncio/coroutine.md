## 🔹 What is a Coroutine?

A **coroutine** is a **special function** in Python declared with `async def` that can **pause execution** (`await`) and **resume later**.

It is the building block of **asynchronous programming** in Python.

---

## 🔹 Key Points

1. **Defined using `async def`:**

   ```python
   async def my_coroutine():
       await asyncio.sleep(1)
       print("Done")
   ```

2. **Run inside an event loop:**

   * You can’t just call it directly.
   * You must use `await` or `asyncio.run()`.

3. **Difference from a normal function:**

   * A **normal function** runs top-to-bottom without pausing.
   * A **coroutine** can **suspend itself** at `await` and let other coroutines run.

---

## 🔹 Simple Example

```python
import asyncio

async def say_hello():
    print("Hello ...")
    await asyncio.sleep(2)   # Pause here, let others run
    print("... World!")

async def main():
    await say_hello()

asyncio.run(main())
```

👉 Output:

```
Hello ...
(wait 2 seconds)
... World!
```

Here, `say_hello` is a **coroutine**. The line `await asyncio.sleep(2)` pauses execution and gives control back to the **event loop**.

---

## 🔹 Why Coroutines?

✅ Efficient for **I/O-bound tasks** (network requests, database calls, file reads/writes).
✅ No need for multiple threads or processes → saves memory & CPU.
✅ Lets you write **concurrent code** in a sequential style.

❌ Not suitable for **CPU-heavy tasks** (like image processing, ML training). For that, use multiprocessing or threads.

---

⚡ In short:
**Coroutines = functions that can pause (`await`) and resume, enabling concurrency inside a single-threaded event loop.**
