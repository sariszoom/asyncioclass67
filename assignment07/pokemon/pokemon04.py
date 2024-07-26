import aiofiles
import asyncio
import json
import os

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    # List all JSON files in the pokemonapi directory
    files = [f for f in os.listdir(pokemonapi_directory) if f.endswith('.json')]

    # Loop through each file and process them one by one
    for file_name in files:
        async with aiofiles.open(os.path.join(pokemonapi_directory, file_name), mode='r') as f:
            contents = await f.read()

        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        async with aiofiles.open(os.path.join(pokemonmove_directory, f'{name}_moves.txt'), mode='w') as f:
            await f.write('\n'.join(moves))

# Run the main coroutine
asyncio.run(main())
