import asyncio
import time
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return 1
async def main():
    print(time.strftime("%X"))
    print(await say_after(1, "hello"))
    return
    await say_after(1, "world")
    print(time.strftime("%X"))
asyncio.run(main())

print("asdfa"[5:] == "")