<template lang="pug">
div
  h1 Todo test project
  p Normally, some kind of landing page would be here, with proper navbar, Sign Up and Sign In buttons
  p As of now, you can only work with todo lists and items using REST API

  n-link.btn.btn-primary(:to="{ name: 'lists' }") Start creating todo lists!
</template>

<script>
export default {}
</script>
