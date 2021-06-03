<template lang="pug">
div
  .mb-4
    ListContainerPreview(v-for="item in items" :key="item.id" v-bind="item")

  .mb-4
    ListContainerAdd(@created="onListCreated")

  b-pagination(
    :value="page"
    :total-rows="totalRows"
    :per-page="perPage"
    @change="changePage"
  )
</template>

<script>
import ListContainerPreview from '~/components/ListContainerPreview'

export default {
  components: { ListContainerPreview },
  props: {
    page: { required: false, default: 1, type: Number },
  },
  data() {
    return {
      perPage: 3,
      items: [],
      totalRows: 0,
    }
  },
  methods: {
    changePage(page) {
      this.$router.push({ name: 'lists', query: { page } })
    },
    onListCreated() {
      this.totalRows += 1
      const page = Math.ceil(this.totalRows / this.perPage)
      if (page !== this.page) {
        this.changePage(page)
      } else {
        this.$fetch()
      }
    }
  },
  watch: {
    '$route.query': '$fetch'
  },
  async fetch() {
    const data = await fetch(`http://127.0.0.1:8000/api/containers?page=${this.page}`).then(
      res => res.json()
    )

    this.totalRows = data.count
    this.items = data.results
  },
}
</script>
