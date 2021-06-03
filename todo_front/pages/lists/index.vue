<template lang="pug">
div
  h1 Todo lists
  ListContainers(:page="page")
</template>

<script>
import ListContainers from '~/components/ListContainers'
// import ListContainer from '~/components/ListContainer'

export default {
  watchQuery: true,
  components: { ListContainers },
  computed: {
    page() {
      const page = parseInt(this.$route.query.page)
      return !isNaN(page) ? page : 1
    }
  }
  // async asyncData({ query, params, $axios }) {
  //   const res = await $axios.get('containers', {
  //     params,
  //     // paramsSerializer: function (params) {
  //     //   return qs.stringify(params, { arrayFormat: 'repeat' })
  //     // },
  //   })

  //   console.log(res.data)

  //   return {
  //     page: parseInt(query.page) || 1,
  //     results: res.data.results,
  //     total: res.data.count,
  //   }
  // },
}
</script>
