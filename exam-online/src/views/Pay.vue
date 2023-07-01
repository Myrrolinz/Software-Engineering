<template>
  <div class="pay">
    <img src="@/assets/qr.jpg">
    <div class="start" @click="handleStart">开始答题</div>
  </div>
</template>

<script>
export default {
    methods:{
        handleStart(){
            	this.$router.push({
					path: '/answer',
					query: {}
				})
        }
    }
}
</script>

<style lang="scss" scoped>
.pay{
    position: relative;
    height: 100vh;
    width: 100vw;
}
img{
    height: 100%;
    width: 100%;
}
.start{
    position: absolute;
    top: 56%;
    transform: translate(-6%,-56%);
    right: 6%;
    margin-right: -10px;
    font-size: 1.2rem;
    z-index:100;
    color:#fff;
    cursor: pointer;
}
</style>