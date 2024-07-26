import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

async def main(x):
    # Loop 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        # Simulate thinking time without blocking the event loop
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        # Here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made a move.")
    print(f"BOARD-{x+1} - >>>>>>>>>> Finish move in {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
