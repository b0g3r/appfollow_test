<template>
  <div class="hello">
    <template v-for="(block, key) in blocks">
      <img
        height="20px"
        width="20px"
        :src="`/static/${block.picture}`"
      >
      <span>{{ key }}</span>
      <ul v-for="permission in block.permissions">
        <li>{{ permission }}</li>
      </ul>
    </template>
  </div>
</template>

<script>
export default {
  name: 'Permissions',
  props: {
    blocks: Object
  }
}
</script>

<style scoped>
  img {
    float: left;
  }
  span {
    margin-left: 6px;
  }
</style>
