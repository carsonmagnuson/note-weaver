<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  const pieces = writable ({});

  async function reload() {
    const response = await fetch('http://localhost:5000/pieces', {mode: 'cors'});
    const data = await response.json();
    pieces.set(data)
    console.log(pieces)
  }
  onMount(async() => {
    reload()
  })
</script>

<main>
   
  <button >reload</button>
  <p>loaded</p>
  {#each Object.keys($pieces) as key}
    <div>{key} : {JSON.stringify($pieces[key])}</div>
  {/each}
</main>

<style>
</style>
