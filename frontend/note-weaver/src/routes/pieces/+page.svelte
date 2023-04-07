<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  let pieces = {};

  const burl = 'http://localhost:5000';
  
  async function get() {
    const response = await fetch(`${burl}/get`);
    pieces = await response.json()
    console.log(pieces);
  }
  onMount(async() => {
    get()
  })
</script>

<main>
  <button on:click={get}>reload</button>
  <p>loaded</p>
  <pre>{JSON.stringify(pieces, null, 2)}</pre>
</main>

<style>
</style>
