<!-- <template>
  <div>
    <div class="sep-div">
      <GuestbookCreate :userId="userId" />
    </div>
    <div class="sep-div">
      <GuestbookList :userId="userId" />
    </div>
  </div>
</template>

<script>
import GuestbookCreate from '@/components/GuestbookCreate';
import GuestbookList from '@/components/GuestbookList';

export default {
  name: 'MyGuestbookView',
  components: {
    GuestbookCreate,
    GuestbookList,
  },
  computed: {
    userId() {
      return this.$route.params.userId;
    },
  },
};
</script> -->

<template>
  <div>
    <div class="sep-div">
      <GuestbookCreate :userId="userId" @guestbookCreated="fetchGuestbooks" />
    </div>
    <div class="sep-div">
      <GuestbookList :userId="userId" :guestbooks="guestbooks" />
    </div>
  </div>
</template>

<script>
import GuestbookCreate from '@/components/GuestbookCreate';
import GuestbookList from '@/components/GuestbookList';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'MyGuestbookView',
  components: {
    GuestbookCreate,
    GuestbookList,
  },
  computed: {
    userId() {
      return this.$route.params.userId;
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
        .get(`${API_URL}/accounts/profiles/${userId}/guestbooks/`)
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