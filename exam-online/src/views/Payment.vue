<!--报名缴费页面-->
<template>
  <div>
    <h1>CET报名缴费</h1>
    <form @submit.prevent="submitForm">
      <label>姓名：</label>
      <input type="text" v-model="name" /><br />
      <label>邮箱：</label>
      <input type="email" v-model="email" /><br />
      <label>金额：</label>
      <input type="number" v-model="amount" /><br />
      <button type="submit">提交</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: "",
      email: "",
      amount: 0,
    };
  },
  methods: {
    submitForm() {
      // 在这里处理表单提交
      console.log(this.name, this.email, this.amount);

      // 使用 AJAX 提交表单数据到后端服务器
      axios.post('/submit-form/', {
        name: this.name,
        email: this.email,
        amount: this.amount
      })
      .then(response => {
        // 处理响应数据
        console.log(response.data);
      })
      .catch(error => {
        // 处理错误
        console.error(error);
      });
    },
  },
};
</script>
