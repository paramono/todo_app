<template lang="pug">
div
  b-input-group
    b-form-input(v-model="name" placeholder="List name" type="text" v-on:keyup.enter="add")
    b-input-group-append
      b-button(variant="success" @click="add") Create list
</template>

<script>
export default {
  data() {
    return {
      name: '',
    }
  },
  computed: {
    form() {
      return {
        ...this.$data,
      }
    }
  },
  methods: {
    async add() {
      if (!this.name) {
        return
      }
      await this.$axios.post('containers/', this.form)
      this.name = ''
      this.$emit('created')
    }
  },
}
</script>
