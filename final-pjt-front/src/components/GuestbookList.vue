<template>
  <div class="guestbook-list">
    <h2>Guestbook List</h2>
    <ul>
      <li v-for="guestbook in guestbooks" :key="guestbook.id">
        내용 : {{ guestbook.content }}
        작성자 : {{ guestbook.author }}
        작성시간 : {{ guestbook.created_at }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'GuestbookList',
  props: {
    userId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      guestbooks: [],
    };
  },
  created() {
    this.fetchGuestbooks();
  },
  methods: {
    fetchGuestbooks() {
      const userId = this.userId;

      axios
        .get(`${API_URL}/accounts/user/profiles/${userId}/guestbooks/`)
        .then((response) => {
          this.guestbooks = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
