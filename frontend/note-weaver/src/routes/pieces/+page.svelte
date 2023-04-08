<script>
  import { onMount } from 'svelte';

  let pieces = {};
  let piece_ids = [];

  const burl = 'http://localhost:5000';


  onMount(async() => {
    get();
  })
  
  async function get() {
    const response = await fetch(`${burl}/get`);
    pieces = await response.json();
    piece_ids = Object.keys(pieces);
  }

  async function delete_one(id) {
    console.log(id);
    const response = await fetch(`${burl}/pieces/${id}`, {
      method: 'DELETE'
    });
    console.log(response);
    get();
  }
</script>

<main>
  <button on:click={get}>reload</button>
  <h1>PIECES</h1>
  <hr/>
  <ul>
    {#each piece_ids as key, i}
      <li>
        {pieces[key]['content']} |
        <a href={`/pieces/${key}`}><button>Edit</button></a>
        <button on:click={() => delete_one(key)}>Delete</button>
      </li>
    {/each}
  </ul>
  
</main>

<style>
</style>
