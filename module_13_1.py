import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    n = 1
    while n < 6:
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {n} шар')
        n += 1
    print(f'Силач {name} закончил соревнования.')
    
async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Inokentiy', 3))
    task2 = asyncio.create_task(start_strongman('Veniamin', 4))
    task3 = asyncio.create_task(start_strongman('Evkratiy', 5))
    await task1
    await task2
    await task3
    
asyncio.run(start_tournament())
    