<template>
  <div id="app">
    <PostList />
  </div>
</template>

<script>
import PostList from './components/PostList';

export default {
  name: 'App',
  components: {
    PostList,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
</style>
