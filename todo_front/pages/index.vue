<template lang="pug">
div
  h1 Todo test project
  p Normally, some kind of landing page would be here, with proper navbar, Sign Up and Sign In buttons
  p As of now, you can only work with todo lists and items using REST API

  n-link.btn.btn-primary(:to="{ name: 'lists' }") Start creating todo lists!

  <!-- <div class="container"> -->
  <!--   <div> -->
  <!--     <Logo /> -->
  <!--     <h1 class="title">todo_front</h1> -->
  <!--     <div class="links"> -->
  <!--       <a -->
  <!--         href="https://nuxtjs.org/" -->
  <!--         target="_blank" -->
  <!--         rel="noopener noreferrer" -->
  <!--         class="button--green" -->
  <!--       > -->
  <!--         Documentation -->
  <!--       </a> -->
  <!--       <a -->
  <!--         href="https://github.com/nuxt/nuxt.js" -->
  <!--         target="_blank" -->
  <!--         rel="noopener noreferrer" -->
  <!--         class="button--grey" -->
  <!--       > -->
  <!--         GitHub -->
  <!--       </a> -->
  <!--     </div> -->
  <!--   </div> -->
  <!-- </div> -->
</template>

<script>
export default {}
</script>
