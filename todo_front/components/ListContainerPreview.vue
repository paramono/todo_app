<template lang="pug">
div
  n-link(:to="{ name: 'lists-id', params: { id } }")  {{ name }}
</template>

<script>
export default {
  props: {
    id: { required: true, type: Number },
    name: { required: true, type: String },
    items: { required: false, type: Array, default: () => [] },
  },
}
</script>
