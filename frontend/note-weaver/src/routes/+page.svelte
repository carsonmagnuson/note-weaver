<main>
  <label>
    CONTENT:
    <textarea rows='4' bind:value={content}></textarea>
  </label>
  <p>loaded</p>
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
  <button on:click={handleClick}>Save Piece</button>
  <hr>
  <button on:click={get}>GET PIECES</button>
</main>


<script>
//  import { Link } from 'sveltekit-navigator';
  let type = 'type';
  let world = 'world';
  let characters = 'et al.';
  let content = '';

  const burl = 'http://localhost:5000';
  
  async function get() {
    const response = await fetch(`${burl}/get`);
    const data = await response.json()
    console.log(data);
  }

  async function save(type, world, characters, content) {
    const piece = {
      'type': type,
      'world': world,
      'characters': characters,
      'content': content
    }
    const response = await fetch(`${burl}/create`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(piece)
    });
    const data = await response.json()
    console.log(data);

  }
  
  function handleClick() {
    console.log('handled')
    save(type, world, characters, content)
  }
</script>
