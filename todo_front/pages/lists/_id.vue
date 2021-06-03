<template lang="pug">
div
  ListContainer.mb-3(:id="id")

  n-link.btn.btn-primary(type="button" to="/lists") Back to all lists
</template>

<script>
import ListContainer from '~/components/ListContainer'

export default {
  components: { ListContainer },
  computed: {
    id() {
      const id = parseInt(this.$route.params.id)
      return !isNaN(id) ? id : 1
    }
  }
}
</script>
