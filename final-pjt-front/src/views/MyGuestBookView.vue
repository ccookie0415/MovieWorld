<template>
    <div>
    <div class="header news__header">
      <span>Guest book</span>
      <span>방명록</span>
    </div>

    <div class="sep-div">
      <GuestbookCreate :userId="userId" />
    </div>

    <hr>

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
</script>

<style>


.header {
  display: flex;
  align-items: flex-end;
  padding-bottom: 10px;
}

.news__header {
  border-bottom: 1.5px solid rgba(0, 0, 0, 0.5);
}

.header span:first-child {
  font-size: 15px;
  margin-right: 5px;
  font-weight: 600;
  color: #55B2D4;
}

.header span:last-child {
  font-size: 6px;
  font-weight: 600;
}


</style>