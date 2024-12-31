<template>
    <div class="post-item">
      <img :src="post.Poster" :alt="post.Title" class="poster" />
      <div class="details">
        <h2>{{ post.Title }} ({{ post.Year }})</h2>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "PostItem",
    props: {
      post: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .post-item {
    display: flex;
    flex-direction: column;
    border: 1px solid #ccc;
    padding: 20px;
    margin: 15px;
    border-radius: 10px;
    background-color: #fff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }
  
  .post-item:hover {
    transform: translateY(-5px);
  }
  
  .poster {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 15px;
  }
  
  .details {
    flex: 1;
  }
  
  .details h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .details p {
    font-size: 1rem;
    margin: 5px 0;
  }
  
  .details strong {
    font-weight: bold;
  }
  </style>
  