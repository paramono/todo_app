<template lang="pug">
div
  .d-flex.align-items-baseline.mb-3
    h1.d-inline
      input.borderless(v-model="name" type="text" @input="debounceInput")
    b-button.ml-auto(variant="outline-danger" @click="destroy") Delete&nbsp;list
  div.mb-3
    ListItem(v-for="item in items" :key="item.id" v-bind="item" @itemChanged="$fetch")
  ListItemAdd(:parent="id" @itemChanged="$fetch")
</template>

<script>
import _ from 'lodash'

export default {
  props: {
    id: { required: true, type: Number },
    // name: { required: true, type: String },
    // items: { required: false, type: Array, default: () => [] },
  },
  data() {
    return {
      name: '',
      items: [],
    }
  },
  methods: {
    debounceInput: _.debounce(async function(value) {
      await this.$axios.patch(`containers/${this.id}/`, { name: this.name })
      // this.$fetch()
    }, 500),
    async destroy() {
      await this.$axios.delete(`containers/${this.id}/`)
      this.$router.push({ name: 'lists' })
    },
  },
  async fetch() {
    const data = await fetch(
      `http://127.0.0.1:8000/api/containers/${this.id}/`
    ).then(res => res.json())

    this.name = data.name
    this.items = data.items
    // Object.assign(this.$data, data)
  },
}
</script>
