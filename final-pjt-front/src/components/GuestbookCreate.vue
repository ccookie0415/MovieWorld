<!-- <template>
  <div class="comment-create">
    <hr>
    <form @submit.prevent="createGuestbook">
      <input type="text" v-model.trim="guestbook" maxlength="50">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'GuestbookCreate',
  props: {
    userId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      guestbook: '',
    }
  },
  methods: {
    createGuestbook() {
      const content = this.guestbook
      const userId = this.userId

      if (!content) {
        alert('내용을 입력하세요')
        return
      }
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/user/profiles/${userId}/guestbooks/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
        data: { content: content },
      })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
          console.log(error.response.data)
        })

      this.guestbook = ''
    },
  }
}
</script> -->

<template>
  <div>
    <div class="content" v-if="!update">
      <p>{{ guestbook.content }}</p>
      <span>{{ guestbook.author }}</span>
      <span>{{ guestbook.created_at.substr(0, 10) }}</span>
    </div>

    <div class="comment-create" v-else>
      <form @submit.prevent="changeGuestbook(guestbook.id)">
        <input type="text" v-model.trim="newGuestbook" maxlength="50">
        <input type="submit" value="작성">
      </form>
    </div>

    <div @click="popSelector" class="dot" v-show="guestbook.author === this.$store.state.username">
      <font-awesome-icon icon="fa-solid fa-ellipsis-vertical" style="width:5px"/>
      <div v-show="selector" class="pop">
        <p @click="changeInput" class="pop-name">수정</p>
        <hr>
        <p @click="deleteGuestbook(guestbook.id)" class="pop-name">삭제</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'GuestbookCard',
  props: {
    guestbook: Object,
  },
  data() {
    return {
      selector: false,
      update: false,
      newGuestbook: this.guestbook.content
    }
  },
  methods: {
    popSelector() {
      if (!this.selector) {
        this.selector = true
      } else {
        this.selector = false
      }
    },
    deleteGuestbook(guestbookId) {
      axios({
        method: 'delete',
        url: `${API_URL}/accounts/profiles/${guestbookId}/guestbooks/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.$emit('guestbookDeleted')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    changeInput() {
      this.update = true
    },
    changeGuestbook(id) {
      const content = this.newGuestbook
      const guestbookId = id

      if (!content) {
        alert('내용을 입력하세요')
        return
      }

      axios({
        method: 'put',
        url: `${API_URL}/accounts/profiles/${guestbookId}/guestbooks/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
        data: { content: content },
      })
        .then((response) => {
          this.$emit('guestbookUpdated')
        })
        .catch((error) => {
          console.log(error)
        })

      this.update = false
    }
  },
}
</script>
<style scoped>
div {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

p {
  margin-bottom: 3px;
  margin-left:8px;
  font-size: 10px;
  font-weight: bold;
}

span {
  margin-top: 0;
  margin-left:8px;
  margin-right: 15px;
  font-size: 13px;
}

hr {
  margin-bottom: 0;
  margin-top: 0;
}

.content {
  display: inline-block;
}

.content > p {
  font-size: 15px;
  margin-top: 5px;
  margin-bottom: 3px;
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

.comment-create {
  display: inline-block;
  width: 100%;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 20px;
  margin-top: 30px;
}

.comment-create > form > input[type='text'] {
  width: 35vw;
  height: 45px;
  border-radius: 10px;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  background-color: rgb(248, 241, 241);
  padding-left: 10px;
}

.comment-create > form > input[type='submit'] {
  color: black;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 40%;
  padding-left: 10px;
  padding-right: 10px;
  width: 50px;
  height: 45px;
  margin-left: 10px;
  font-size: 15px;
  text-decoration: none;
  background-color: rgb(218, 210, 210);
}
.heart {
  color: rgb(208, 93, 93);
}

</style>