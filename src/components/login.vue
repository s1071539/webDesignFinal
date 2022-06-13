<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.title{
    text-align:center; 
    font-size:30px;
}
.caption{
    text-align:left; 
    font-size:20px;
}
.input{
    width:400px;
    border-color:black;
}
.button{
    font-size:30px;
    width:400px;
    background-color:#439EFF;
    color:black;
}
.src{
    border: none;
    color: black;
    background-color: white;
    cursor: pointer;
    text-decoration:underline;
    font-size:20px;
}

</style>

<template>
  <div style="margin-top:-50px">
    <img src="../assets/logo.png">
    <el-card style="margin:100px auto; width:500px;">
        <div style="margin:0 auto; width:400px; font-size:20px">
            <br><br>
            <div class="title">Log in to your account</div><br><br>
            <div class="caption">Account</div>
            <el-input class="input" v-model="user[0]" placeholder="請輸入帳號(使用者名稱)"></el-input><br><br>
            <div class="caption">Password</div>
            <el-input class="input" v-model="user[1]" placeholder="請輸入密碼" show-password></el-input><br><br><br>
            <el-button class="button"  plain @click="login">Log in</el-button><br><br>
            <button  class="src" @click="signup"> Sign Up </button><br>
            <br>
           
        </div>
    </el-card>
  </div>
</template>

<script>
import * as THREE from 'three'
export default {
  name: 'login',
  data: function() {
        return { 
            user:["",""],
        }
  },
  created(){
        this.$router.replace({query: ''}).catch(()=>{});
  },
  mounted() {//監聽enter 若按enter則觸發login
    let _this = this;
    document.onkeydown = function(e) {
        if (_this.$route.name == "login") {
            let key = window.event.keyCode;
            if (key == 13) 
                _this.login();
            }
    }
    
  },
  methods:{
    login(){
        this.axios.get("/login",{
            params:{
                user: JSON.stringify(this.user),
                mode:'login'
            }
        }).then((response)=>{
            let res = response.data;
            if(res.msg == '登入成功!'){
                this.$message({message: res.msg, type: 'success'});
                sessionStorage.setItem("user", JSON.stringify(this.user[0]));//驗證器
                sessionStorage.setItem("token", "ImLogin");//驗證器
                this.$router.push({name: 'Show_All'});
            }
            else 
                this.$message({message: res.msg, type: 'error'});
        });
    },
    signup(){
        this.$router.push({name: 'signup'});
    },
    resetPassword(){
        this.$router.push({name: 'resetPassword'});
    },
  }
}
</script>