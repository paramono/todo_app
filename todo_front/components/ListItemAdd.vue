<template lang="pug">
div
  b-input-group
    b-form-input(v-model="name" placeholder="Item name" type="text" v-on:keyup.enter="add")
    b-input-group-append
      b-button(variant="success" @click="add") Add item
</template>

<script>
export default {
  props: {
    parent: { required: true, type: Number },
  },
  data() {
    return {
      name: '',
    }
  },
  computed: {
    form() {
      return {
        ...this.$props,
        ...this.$data,
      }
    }
  },
  methods: {
    async add() {
      await this.$axios.post('items/', this.form)
      this.name = ''
      this.$emit('itemChanged')
    }
  },
  // async fetch() {
  //   const data = await fetch(
  //     `http://127.0.0.1:8000/api/containers/${this.id}`
  //   ).then(res => res.json())

  //   this.name = data.name
  //   this.items = data.items
  //   // Object.assign(this.$data, data)
  // },
}
</script>
