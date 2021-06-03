<template lang="pug">
div.d-flex.align-items-baseline.mb-1
  b-form-checkbox(size="lg" :checked="done" @input="check")
  input.borderless(:value="name" type="text" @input="rename")
  b-button.ml-auto(variant="outline-danger" size="sm" @click="destroy") ⨯
</template>

<script>
import _ from 'lodash'

export default {
  props: {
    parent: { required: true, type: Number },
    id: { required: true, type: Number },
    name: { required: true, type: String },
    done: { required: true, type: Boolean },
  },
  methods: {
    async check(value) {
      await this.$axios.patch(`items/${this.id}/`, { done: value })
      this.$emit('itemChanged')
    },
    rename: _.debounce(async function(e) {
      const value = e.target.value
      if (value) {
        await this.$axios.patch(`items/${this.id}/`, { name: value })
        this.$emit('itemChanged')
      } else {
        await this.destroy()
      }
    }, 500),
    async destroy() {
      await this.$axios.delete(`items/${this.id}/`)
      this.$emit('itemChanged')
    },
  },
}
</script>
