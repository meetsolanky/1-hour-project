<template>
  <div class="post-list">
    <div class="post-row">
      <!-- Loop through posts and display them -->
      <div v-for="post in posts" :key="post.id" class="post-card">
        <div class="post-header">
          <h3>{{ post.text }}</h3>
          <p class="post-meta">
            <strong>By:</strong> {{ post.user.username }} |
            <strong>Posted at:</strong> {{ formatDate(post.timestamp) }}
          </p>
        </div>

        <!-- Comments Section -->
        <div class="comments-section" v-if="post.comments.length > 0">
          <p class="comments-title"><strong>Comments ({{ post.comments.length }})</strong></p>
          <div v-for="comment in post.comments" :key="comment.id" class="comment">
            <div class="comment-header">
              <strong>{{ comment.user.username }}</strong>
              <span class="comment-meta"><em>Posted at: {{ formatDate(comment.timestamp) }}</em></span>
            </div>
            <p>{{ comment.text }}</p>
          </div>
        </div>
        <div v-else>
          <p class="no-comments">No comments yet.</p>
        </div>
      </div>
    </div>

    <!-- Loading Indicator (appears when new posts are being fetched) -->
    <div v-if="loading" class="loading-indicator">Loading...</div>

    <!-- Invisible element used to trigger loading of new posts -->
    <div ref="scrollTrigger" class="scroll-trigger"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],         // Holds the list of posts
      nextPage: 1,       // Tracks the next page to load
      loading: false,    // To show loading indicator
    };
  },
  mounted() {
    this.loadPosts();   // Load initial posts
    this.setupScrollListener();  // Set up the infinite scroll trigger
  },
  methods: {
    async loadPosts() {
      if (this.loading || !this.nextPage) return;  // Prevent loading if already in progress

      this.loading = true;

      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/posts?page=${this.nextPage}&format=json`);
        const data = response.data;

        // Append the posts at the end to simulate continuous scrolling
        this.posts = [...this.posts, ...data];

        // Update the nextPage if there is more content to load
        this.nextPage = data.next ? this.nextPage + 1 : null;
      } catch (error) {
        console.error("There was an error loading the posts:", error.response ? error.response.data : error);
      } finally {
        this.loading = false;
      }
    },
    setupScrollListener() {
      const observer = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting && !this.loading) {
          this.loadPosts();  // Load more posts when bottom is reached
        }
      }, {
        rootMargin: '200px',  // Load when the trigger is near the bottom of the viewport
      });

      observer.observe(this.$refs.scrollTrigger);  // Observe the scroll trigger
    },
    formatDate(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString();  // Customize as needed
    },
  },
};
</script>

<style scoped>
/* Main container styling */
.post-list {
  margin: 30px auto;
  max-width: 1200px;
  padding: 0 15px;
  font-family: 'Arial', sans-serif;
}

/* Flex container for posts */
.post-row {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-between;
}

/* Styling individual post cards */
.post-card {
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 48%;  /* Two posts per row */
  transition: all 0.3s ease;
  box-sizing: border-box;
  overflow: hidden;
  margin-bottom: 30px;
  background-color: #f4f6f9;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

/* Add gradient backgrounds to posts */
.post-card:nth-child(odd) {
  background: linear-gradient(145deg, #0036d9, #4864b1);  /* Soft blue gradient */
}

.post-card:nth-child(even) {
  background: linear-gradient(145deg, #0d0a01, #210202);  /* Soft yellow gradient */
}

/* Styling for post header */
.post-header {
  border-bottom: 2px solid #ddd;
  margin-bottom: 15px;
}

.post-header h3 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: bold;
  color: #ecf2f8;
}

.post-meta {
  font-size: 0.9rem;
  color:rgb(255, 255, 255);
}

/* Comment section styling */
.comments-title {
  margin-top: 15px;
  font-size: 1.1rem;
  font-weight: bold;
  color: #34495e;
}

.comment {
  background-color: #e9f3fc;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.comment-header strong {
  font-size: 1rem;
  color: #34495e;
}

.comment-meta {
  font-size: 0.85rem;
  color: #7f8c8d;
}

.comment p {
  margin: 0;
  font-size: 1rem;
  color: #2c3e50;
}

/* Styling for the 'no comments' text */
.no-comments {
  color: #888;
  font-style: italic;
}

/* Loading indicator */
.loading-indicator {
  text-align: center;
  font-size: 1.2rem;
  color:rgb(106, 162, 199);
  padding: 20px;
  font-weight: bold;
}

/* Invisible trigger element for infinite scrolling */
.scroll-trigger {
  height: 1px;
}

/* Responsive design */
@media (max-width: 768px) {
  .post-card {
    width: 48%;  /* Two posts per row on smaller screens */
  }
}

@media (max-width: 480px) {
  .post-card {
    width: 100%;  /* One post per row on very small screens */
  }
}
</style>
