<template lang="pug">
div
  // ListContainer(v-bind="item")
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
  // async asyncData({ query, params, $axios }) {
  //   const res = await $axios.get(`containers/${params.id}`)

  //   console.log(res.data)

  //   return {
  //     page: parseInt(query.page) || 1,
  //     item: res.data,
  //   }
  // },
}
</script>
