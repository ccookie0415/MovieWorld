<template>
  <div>
    <div class="guestbook-list" v-for="guestbook in guestbooks.slice().reverse()" :key="guestbook.id">
      <div v-if="guestbook.id === selectedGuestbookId">
        <div class="guestbook-card">
          <textarea class="card-textarea" v-model="editedContent"></textarea>
          <div class="guestbook-actions">
            <button @click="updateGuestbook">저장</button>
            <button @click="cancelEdit">취소</button>
          </div>
        </div>
      </div>
      <div v-else>
        <div class="guestbook-card">
          <div class="guestbook-actions">
            <div v-if="user.id === user_Id || guestbook.author === user_Id">
              <button @click="editGuestbook(guestbook.id)">수정</button>
              <button @click="deleteGuestbook(guestbook.id)">삭제</button>
            </div>
          </div>
          <p class="day-name2">{{ guestbook.content }}</p>
          <span class="day">작성일</span>
          <span class="day">{{ guestbook.created_at.substr(0, 10) }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'GuestbookList',
  computed: {
    // 얘는 프로필주인인듯
    user() {
      return this.$store.state.user;
    },
    // 얘는 로그인한사람인듯
    user_Id() {
      return this.$store.state.userId;
    },
  },
  props: {
    userId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      guestbooks: [],
      selectedGuestbookId: null,
      editedContent: '',
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
    editGuestbook(guestbookId) {
      this.selectedGuestbookId = guestbookId;
      const guestbook = this.guestbooks.find((guestbook) => guestbook.id === guestbookId);
      this.editedContent = guestbook.content;
    },
    updateGuestbook() {
      const guestbookId = this.selectedGuestbookId;
      const updatedContent = this.editedContent;

      axios
        .put(`${API_URL}/accounts/user/profiles/${this.userId}/guestbook/${guestbookId}/`, {
          content: updatedContent,
        })
        .then((response) => {
          const updatedGuestbook = response.data;
          const index = this.guestbooks.findIndex((guestbook) => guestbook.id === guestbookId);
          this.guestbooks.splice(index, 1, updatedGuestbook);
          this.cancelEdit();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    cancelEdit() {
      this.selectedGuestbookId = null;
      this.editedContent = '';
    },
    deleteGuestbook(guestbookId) {
      axios
        .delete(`${API_URL}/accounts/user/profiles/${this.userId}/guestbook/${guestbookId}/`)
        .then((response) => {
          this.guestbooks = this.guestbooks.filter((guestbook) => guestbook.id !== guestbookId);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>

.guestbook-list {
  display: inline-block;
  width: 420px;
  text-align: left;
  margin-left: 5px;
  margin-right: 5px;
  margin-bottom:3px;
  border-radius:  0 15px 15px 0  ;
  background:#55b2d467;
  padding-left: 5px;
  padding-bottom: 10px;
}

.guestbook-card {
  background-color : white;
  width: 400px;
  height: 100px;
  border-radius: 4px;
  padding: 10px;
  margin-top : 10px;
  position: relative;
}

.card-textarea {
  width: 100%;
  height: 100%;
  resize: none;
}

.guestbook-actions {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  flex-direction: column;
}

.day-name2 {
  text-align: left;
  font-size: 18px;
  font-weight: 600;
}

.day {
  display: inline-block;
  margin-right: 50px;
  font-size: 12px;
}


</style>