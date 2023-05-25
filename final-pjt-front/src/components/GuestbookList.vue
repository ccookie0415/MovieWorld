<template>
  <div>
    <div class="guestbook-list" v-for="guestbook in paginatedGuestbooks" :key="guestbook.id">
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
          <div @click="popSelector" class="guestbook-actions" v-show="user.id === user_Id || guestbook.author === user_Id">
            <font-awesome-icon icon="fa-solid fa-ellipsis-vertical" style="width:20px; height:25px" @click="toggleSelector(guestbook.id)"/>
            <div v-show="isSelected(guestbook.id)" class="pop">
              <p @click="editGuestbook(guestbook.id)" class="pop-name value">수정</p>
              <hr>
              <p @click="deleteGuestbook(guestbook.id)" class="pop-name value">삭제</p>
            </div>
          </div>

          <p class="day-name2">{{ guestbook.content }}</p>

            <div class="guestbook-info">
              <div class="guestbook-author">
                <a class="value" style="text-decoration: none; color: black;" @click="redirectToUserHome(guestbook.author)">{{ guestbook.username }}</a>
                <span class="day">작성일 {{ guestbook.created_at.substr(0, 10) }}</span>
              </div>
            </div>

        </div>
      </div>
    </div>
    <div class="pagination-buttons">
      <button @click="previousPage" :disabled="currentPage === 1">이전</button>
      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'GuestbookList',
  computed: {
    user() {
      return this.$store.state.user;
    },
    user_Id() {
      return this.$store.state.userId;
    },
    paginatedGuestbooks() {
    const startIndex = (this.currentPage - 1) * this.perPage;
    const endIndex = startIndex + this.perPage;
    const reversedGuestbooks = this.guestbooks.slice().reverse(); // guestbooks 배열을 역순으로 변환
    return reversedGuestbooks.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.guestbooks.length / this.perPage);
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
      selector: false,
      guestbooks: [],
      selectedGuestbookIds: [],
      selectedGuestbookId: null,
      editedContent: '',
      currentPage: 1,
      perPage: 5,
    };
  },
  created() {
    this.fetchGuestbooks();
  },
  methods: {
    toggleSelector(guestbookId) {
      const index = this.selectedGuestbookIds.indexOf(guestbookId);
      if (index > -1) {
        this.selectedGuestbookIds.splice(index, 1);
      } else {
        this.selectedGuestbookIds.push(guestbookId);
      }
    },
    isSelected(guestbookId) {
      return this.selectedGuestbookIds.includes(guestbookId);
    },
    popSelector() {
      if (! this.selector) {
        this.selector = true
      } else { 
        this.selector = false
      }
    },
    redirectToUserHome(author) {
      const path = `/${author}/main/myhome`;
      this.$router.push(path).catch((err) => {
        if (err.name !== 'NavigationDuplicated') {
          throw err;
        }
      });
      setTimeout(() => {
        this.$router.go(0);
      }, 10);
    },
    fetchGuestbooks() {
      const userId = this.userId;
      const page = this.currentPage;
      const limit = this.perPage;

      axios
        .get(`${API_URL}/accounts/user/profiles/${userId}/guestbooks/`, {
          params: {
            page: page,
            limit: limit,
            sort: 'desc', // 요청 시 역순 정렬 옵션 추가
          },
        })
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
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.fetchGuestbooks();
      }
    },
    nextPage() {
      const totalPages = this.totalPages;

      if (this.currentPage < totalPages) {
        this.currentPage++;
        this.fetchGuestbooks();
      }
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
  height: 80px;
  border-radius: 4px;
  padding: 10px;
  margin-top : 8px;
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
  margin-left: auto;
  font-size: 12px;
}

.dot {
  display: inline-block;
  margin-right: 17px;
  font-size: 20px;
  background-color: transparent;
  border: none;
  color: black;
  position: relative;
}

.dot:hover {
  background-color: transparent;
}

/* .dot {
  background-color: transparent;
} */

.pop {
  display: inline-block;
  position: absolute;
  z-index: 999;
  background-color: 55b2d4;
  border-radius: 10px;
  top: 8px;
  left: -50px;
  width: 50px;
  text-align: center;
}

.pop-name {
  font-size: 15px;
  margin: 0;
  margin-top: 3px;
  margin-bottom: 3px;
  padding: 0;
}


.pop-name:hover {
  font-weight: bold;
}

.value {
  font-size: 14px;
  background-color: #55b2d467;
  border-radius: 10px;
  padding-left: 10px;
  padding-right: 10px;
}

.value:hover {
  color: rgb(73, 44, 44);
  font-weight: bold;
}

.guestbook-info {
  /* display: flex; */
  align-items: center;
  justify-content: space-between;
}

.guestbook-author {
  display: flex;
  align-items: center;
}

.guestbook-author .value {
  margin-right: 5px;
}

</style>