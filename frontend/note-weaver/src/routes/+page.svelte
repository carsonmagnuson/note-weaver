<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  
  let type = '';
  let world = '';
  let content = '';
  let characters = '';

  const data = {
    'type': 'quote',
    'content': 'Universe runs on drunkin',
    'world': world,
    'characters': 'NA', 
    'date': 'today'}

  async function handleSubmit() {
    const response = await fetch('http://localhost:5000/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    console.log(data)
    const result = await response.json(); // The response from the backend
    console.log(result); // Handle the response accordingly
  }
</script>

<main>
  <form on:submit|preventDefault={handleSubmit}>
    <label>
      Type:
      <input bind:value={type} />
    </label>
    <label>
      Content:
      <input bind:value={content} />
    </label>
    <label>
      World:
      <input bind:value={world} />
    </label>
    <label>
      Characters:
      <input bind:value={characters} />
    </label>
    <button type="submit">Submit</button>
  </form>
</main>

<style>
</style>
