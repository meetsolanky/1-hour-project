<template>
    <div>
      <div class="post-list">
        <div v-for="post in posts" :key="post.imdbID" class="post-item-container">
          <PostItem :post="post" />
        </div>
      </div>
      <button v-if="nextPage" @click="loadMore" class="load-more-btn">Load More</button>
      <p v-else>No more posts to load.</p>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import PostItem from "@/components/PostItem.vue";
  
  export default {
    components: {
      PostItem,
    },
    data() {
      return {
        posts: [], // Stores movie data
        nextPage: null, // Placeholder for next page URL (if applicable)
        error: null, // Error message
      };
    },
    created() {
      this.fetchPosts();
    },
    methods: {
      async fetchPosts(url = "https://www.omdbapi.com/?s=Guardians&apikey=d2132124") {
        try {
          const response = await axios.get(url);
          console.log(response.data);
          if (response.data.Search) {
            this.posts = [...this.posts, ...response.data.Search];
            // Update `nextPage` logic based on API's pagination (if supported)
            this.nextPage = null; // Replace with actual next page logic if API provides it
          } else {
            this.error = "No posts found.";
          }
        } catch (error) {
          this.error = "Error fetching posts. Please try again later.";
          console.error(error);
        }
      },
      loadMore() {
        if (this.nextPage) {
          this.fetchPosts(this.nextPage);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .post-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
  }
  
  .post-item-container {
    display: flex;
    justify-content: center;
  }
  
  .load-more-btn {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .load-more-btn:hover {
    background-color: #0056b3;
  }
  
  .error {
    color: red;
    font-weight: bold;
    text-align: center;
  }
  </style>
  