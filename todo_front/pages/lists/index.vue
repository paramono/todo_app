<template lang="pug">
div
  h1 Todo lists
  ListContainers(:page="page")
</template>

<script>
import ListContainers from '~/components/ListContainers'

export default {
  watchQuery: true,
  components: { ListContainers },
  computed: {
    page() {
      const page = parseInt(this.$route.query.page)
      return !isNaN(page) ? page : 1
    }
  }
}
</script>
