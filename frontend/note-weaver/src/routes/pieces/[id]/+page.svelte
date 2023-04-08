<main>
  <h1>{data.id}</h1>
  <label>
    CONTENT:
    <textarea rows='4' bind:value={content}></textarea>
  </label>
  <hr>
  <label>
    TYPE:
    <input type='text' bind:value={type} />
  </label>
  <label>
    WORLD:
    <input type='text' bind:value={world} />
  </label>
  <label>
    CHARACTERS:
    <input type='text' bind:value={characters} />
  </label>
  <button on:click={() => save(type, world, characters, content)}>SAVE PIECE</button>
  <hr>
  <button on:click={delete_one}>DELETE PIECE</button>
</main>


<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  export let data;

  let type = 'whatever';
  let world = 'world';
  let characters = 'et al.';
  let content = '';
  let created = '';

  const burl = 'http://localhost:5000';

  onMount(async() => {
    get_one();
  })

  async function get_one() {
    const response = await fetch(`${burl}/pieces/${data.id}`);
    const piece = await response.json()
    content = piece['content']
    type = piece['type']
    world = piece['world']
    characters = piece['characters']
    created = piece['date']

    console.log(piece);
  }

  async function save(type, world, characters, content, created) {
    const piece = {
      'type': type,
      'world': world,
      'characters': characters,
      'content': content,
      'date': created
    }
    const response = await fetch(`${burl}/pieces/${data.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(piece)
    });
    const log = await response.json()
    console.log(log);

  }
  
  async function delete_one() {
    const response = await fetch(`${burl}/pieces/${data.id}`, {
      method: 'DELETE'
    });
    console.log(response)
    goto('/pieces');
    
  }
</script>
