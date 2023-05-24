<template>
  <div class="comment-create">
    <h5></h5>
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
          setTimeout(()=>{ // 받아오는건 정상이니까 조금 느리게 받아와서 새고하는 기분
            this.$router.go(0)
          }, 10)
        })
        .catch((error) => {
          console.log(error)
          console.log(error.response.data)
        })

      this.guestbook = ''
    },
  }
}
</script>

<style>
.comment-create > p {
  font-size:14px;
}

.comment-create > form {
  display: flex;
}
.comment-create > form > input[type='text'] {
  width: 380px;
  height: 35px;
  border-radius: 10px;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  
}

.comment-create > form > input[type='submit'] {
  color: black;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 40%;
  padding-right: 10px;
  width: 45px;
  height: 35px;
  text-decoration: none;
  background-color: 55b2d4;
}

</style>
