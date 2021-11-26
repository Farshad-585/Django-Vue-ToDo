<template>
  <section class="app">
    <Header/>
    <Tasks/>
  </section>
</template>

<script>
import Tasks from './components/Tasks.vue'
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Tasks,
    Header
  }
}
</script>

<style scoped>
.app {
  background-color: #f0efeb;
  height: 100vh;
}
</style>