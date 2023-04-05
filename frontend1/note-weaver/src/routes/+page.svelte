<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  const pieces = writable ({});

  onMount(async () => {
    const response = await fetch('http://localhost:5000/pieces', {mode: 'cors'});
    const data = await response.json();
    pieces.set(data)
    console.log(pieces)

  })
</script>

<main>
  <p>loaded</p>
  {#each Object.keys($pieces) as key}
    <div>{key} : {JSON.stringify($pieces[key])}</div>
  {/each}
</main>

<style>
</style>
