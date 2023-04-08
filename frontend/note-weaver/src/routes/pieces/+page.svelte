<script>
  import { onMount } from 'svelte';

  let pieces = {};
  let link = '/';

  const burl = 'http://localhost:5000';
  
  async function get() {
    const response = await fetch(`${burl}/get`);
    pieces = await response.json()
    console.log(pieces);
    link = `/pieces/${Object.keys(pieces)[0]}`
  }
  onMount(async() => {
    get()
  });
</script>

<main>
  <button on:click={get}>reload</button>
  <p>loaded</p>
  <pre>{JSON.stringify(pieces, null, 2)}</pre>
  <a href={link}>
    <button>go to ex-maple</button>
  </a>
</main>

<style>
</style>
